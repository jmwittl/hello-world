# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:52:45 2019

@author: jmwittl
Source:
	https://kuntalchandra.wordpress.com
	/2017/08/23/python-socket-programming-server-client-application-using-th
reads/

	Python: Socket programming server-client application using threads
	IMPLEMENTING BRUTE FORCE
	A weblog about programming and my rando thoughts

	Posted in Python by Kuntal Chandra
"""
import os
import socket
import sys
import traceback
from threading import Thread


def main():
    start_server(pid=os.getpid())


def start_server(pid):

    myState="SERVER_START"
    print("Me (Server) process id=%d"%pid)

    clientName="Linux-jmwittl-80GB"
    clientIp= socket.gethostbyname(clientName)

    serverName="raspberrypi-B"
    serverIp=socket.gethostbyname(serverName)
    serverPort=12345
    serveraddress=(serverIp,serverPort)

    print("Server %s"%serverName)
    print("       %s"%serverIp)
    print("")
    print("Purpose:\n\tThe purpose of this code is to perform Notes Backup!")
    print("")

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # SO_REUSEADDR f
lag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting
 for its natural timeout to expire
    #print("Server socket created")

    try:
        #blank means listen to any computer on the network
        soc.bind(('', serverPort))
	#print("\tBind to any computer on the network")
    except:
        print("\tBind failed. Error : " + str(sys.exc_info()))
        sys.exit()

    print("Listening for connections")
   myState="LISTEN"
    try:

	print("1")
    	soc.listen(5)       # queue up to 5 requests

        # infinite loop- do not reset for every requests
        while True:

	    print("2")
            connection, address = soc.accept()
            ip, port = str(address[0]), str(address[1])
            print("Connection open")
            print("      ip="+ip)
            print("    port="+port)

            try:
                print("Initiate client thread using connection information")
		print("3")
                Thread(target=client_thread, args=(pid, connection, ip, port)).s
tart()
            except:
                print("Client thread failed!")
                traceback.print_exc()
	        break

    except:
        print("Listen failed!")
        traceback.print_exc()

    print("Listen complete!")
    print("Exit!")
    soc.close()
    sys.exit()

def client_thread(pid, conn, ip, port, maxbs = 5120):

    #######################################
    #Stay in loop until "quit" received!  #
    #Stay in loop while connection exists!#
    #######################################

    #setup conditional loop count:

    count=0
    maxcount=5

    is_active=True

    while conn!=None:

	count=count+1

	print("4")
        client_input=receive_input(conn,maxbs)
	print("7")
        if sys.getsizeof(client_input)==0:
                print("No data received!")
                break
        else:
	        ackmessage="(%d) ack-OK"%pid
               break
        else:
	        ackmessage="(%d) ack-OK"%pid
	        print(("Server sends \"%s\"")% ackmessage)
	        connection.sendall(ackmessage)
                break

        #print("Echo client input back to client.")
        #connection.sendall(client_input)
	#
        #print("Process client input.")
	#
        #if "quit" in client_input.lower():
        #	print("Client is requesting to quit")
        #	connection.close()
        #	connection = None
        #	print("Connection closed")
        #	print("      ip="+ip)
        #	print("    port="+port)
        #	print("Connection is \"None\"")
        #	is_active = False
        #else:
	#
	#	ackmessage="ack-"+client_input
        #	if "backup" in client_input.lower():
	#		print("Execute backup process")
        #        	connection.sendall(ackmessage.decode('ASCII'))
        #    	else:
	#		print("\"UNKNOWN\" process")
	#		connection.sendall(("ack-???").decode('ASCII'))
	#

def receive_input(conn, maxbs):

	buff="";
	try:
		print("5")
		data=conn.recv(maxbs)
	        while sys.getsizeof(data)>0:
			print("data size %d"%sys.getsizeof(data)+".\t"+data)
			buff=buff.join(data)
			if sys.getsizeof(data)<22:
				break
			if (sys.getsizeof(buff)+sys.getsizeof(data))>maxbs:
				raise exception("The input is greated than %d"%m
axbs)
			data=conn.recv(maxbs)
			print("6")
	except:
		raise 

	return buff.decode('ASCII').rstrip()

def process_input(input_str):

	print("Processing the input received from client")

	return "Hello " + str(input_str).upper()

def receive_input(conn, maxbs):

        buff="";
        try:
                print("5")
                data=conn.recv(maxbs)
                while sys.getsizeof(data)>0:
                        print("data size %d"%sys.getsizeof(data)+".\t"+data)

                        dataAnalyser(data)

                        buff=buff.join(data)
                        if sys.getsizeof(data)<22:
                                print("6.5")
                                break
                        if (sys.getsizeof(buff)+sys.getsizeof(data))>maxbs:
                                raise exception("The input is greated than %d"%$
                        data=conn.recv(maxbs)
                        print("6")
        except:
                raise 

        return buff.decode('ASCII').rstrip()

def dataAnalyser(data):

        print(' '.join(format(ord(x), 'b') for x in data))

if __name__ == "__main__":
    main()
