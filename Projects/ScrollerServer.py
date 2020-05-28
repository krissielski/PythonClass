# Top Module
#
import socket
import sys
import time
import select
import serial
import queue
from time import sleep



#Sockets list
input_list = []

#Message Queue
msg_queue = queue.Queue(32)

#Ready?
ready = False

#Local
LOCALHOST = "0.0.0.0"                   #localhost
LOCALPORT = 4004


    
##************************************************
## Def: CloseAllSockets
## Close all open sockets
def CloseAllSockets():

    print("CloseAllSockets")
    
    #Close all attached inputs
    for sock in input_list:
        sock.close()

##************************************************
## Def: DataHandler
## Parse and operate on received data
##   
def DataHandler( sock, ip, data ):

    data = data[:100]
        
    print("RecData >>>", data.upper() )

    txstr = b'@ ' + data.upper()  + b'\n'


    msg_queue.put(txstr)
    #ser.write(txstr)        

    
##** End DataHandler *****************************



#######################
####     MAIN      ####
#######################
print("****************************************")
print("ScrollerServer Application Starting.....")

ser = serial.Serial('COM4',115200,timeout=0)  # open serial port
if( ser.is_open ):
    print("Serial Port opened")


#Create server socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created")

#Add socket to Input list
input_list.append(serversocket)

#Bind Socket
bind_try = 1
while(True):
    try:
        serversocket.bind((LOCALHOST, LOCALPORT))
        break
    except socket.error as msg:
        print("Bind failed. Try #" + str(bind_try)  )
        pass
   
    bind_try +=1
    if( bind_try>100):
        print("Binding Failure.  Giving up!")
        serversocket.close()
        sys.exit()     
    sleep(5)

print("Socket Bind Successful")


#Start Listening
serversocket.listen(20)
serversocket.setblocking(0)
print("Socket now listening")



#Infinite loop to accept and handle all connections
while(True):


    #***********  Socket Handler ***********************************

    #Use SELECT to cycle through all open sockets in the lists
    try:
        rd_socks, wr_socks, err_socks = select.select(input_list, [], [], 1.0 )

        for sock in rd_socks:
            if sock == serversocket:
                conn,addr = sock.accept()
                conn.setblocking(0)
                input_list.append(conn)
                #Log Connection
                print( "Connected " + addr[0] + "    (S#" + str(len(input_list)) +")")

            else:
                #Get Ip Status
                try:
                    ip,port = sock.getpeername()
                except:
                    input_list.remove(sock)                    
                    sock.close()
                    print("***GetPeerName Exception")
                    continue

                #Try to get received data packet
                try:
                    data = sock.recv(4096)
                except ConnectionResetError:
                    #Connection error.  Remove and close
                    input_list.remove(sock)                    
                    sock.close()
                    print("***ConnectionResetError from " + str(ip))
                    continue

                if data:
                    #Data received
                    DataHandler( sock,ip, data )
                else:
                    #Closed connection
                    #For the Gas Transmitters, this in not an error.
                    #They may or may not close connections inbetween data dumps.
                    print("Closed from " + str(ip) )
                    input_list.remove(sock)                    
                    sock.close()
                    print("Num Sockets open = " + str(len(input_list)) )

    except KeyboardInterrupt:
        #Break from Infinite loop if exception occurs
        print("KeyboardInterrupt!")
        break

    #***************************************************************


    #***********  Process Queue ************************************

    if( not msg_queue.empty() and ready ):

        ser.write( msg_queue.get() )
        ready = False
        print("> BUSY!")

                    
    #***************************************************************



    #***********  Process Return **********************************

    rx_str = b''
    while( ser.in_waiting > 0 ):
            rx_byte = ser.read(1)

            if( rx_byte == b'\n' ):
                print("ser >",rx_str )


                if( b'Ready' in rx_str ):
                    ready = True
                    print("> READY!")
                    
                if( b'Done' in rx_str ):
                    ready = True
                    print("> READY!")
                
                break
            else:
                rx_str += rx_byte
                    
    #***************************************************************

    sleep(0.010)    #sleep 10ms  ??
    #END Main Infinite while
    
#Close All open sockets for a clean exit
CloseAllSockets()
ser.close()             
print("Application Exiting")




