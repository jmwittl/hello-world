# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:39:48 2019

@author: jmwittl
"""

import socket
import sys

def main001():

    print("Start main001")

    data=""
    #create 256 byte line "001------...---\n"
    data="001"
    count=252
    while count:
        count=count-1
        data=data+"-"
    data=data+"\n"
#    while len(data)<1024:
#        data=data+aline
    print("sending data, length=%d"% len(data))

    print("1")
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("2")
    clientName="Linux-jmwittl-80GB"
    clientIp= socket.gethostbyname(clientName)

    print("3")
    serverName="raspberrypi-B"
    serverIp=socket.gethostbyname(serverName)
    serverPort=12345
    serveraddress=(serverIp,serverPort)

    print("4")
    print("Connect to %s from %s"%(serverName,clientName))
    print("           %s      %s"%(serverIp,clientIp))

    print("5")
    try:
        soc.connect((serverIp, serverPort))
    except:
        print("Connection error")
        sys.exit()
 
#   print("6")
#   print("Set blocking")
#   try:
#       soc.setblocking(0)
#       rint("No blocking set")
#   except:
#       print("blocking errro")
#       sys.exit()

    print("7")
    print("Send data")
    
    print("total to send=%d"%sys.getsizeof(data))
#   while len(data) :#and totalsent<1:
#
    try:
        print("sending data")
        sent=soc.send(str.encode(data))

#            chunks=[]
#            bytesread=0
#            print("total read=%d"%bytesread)
#            while bytesread<len(data):
#                chunk=soc.recv(min(len(data)-bytesread,len(data)))
#                if chunk=='':
#                    raise RuntimeError("socket connection broken")
#                chunks.append(chunk)
#                bytesread=bytesread+len(chunk)
#                print ("bytes read = %d\n",bytesread)
#                if bytesread>1:
#                    break
#
        print("total sent=%d"%sent)
        print("8")
        print("sending data")
        sent=soc.send("--quit--\n")
        print("total sent=%d"%sent)

        print("9")
        print("sending data")
        sent=soc.send(b'--quit--\n')
        print("total sent=%d"%sent)

        print("10")
        print("shutting down socket")
        sent=soc.shutdown(socket.SHUT_RDWR)

        print("11")
        print("close socket")
        sent=soc.close()


    except:
        print ("Unexpected error:", sys.exc_info()[0])
        raise

if __name__ == "__main__":

    main001()
