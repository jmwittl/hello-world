# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:39:48 2019

@author: jmwittl
"""

import socket
import sys

def getData(dataType):

    if dataType==1:    

        data = ""
        count=12
        while count>0:
            count=count-1
            data=data+"-"

    elif dataType==999:
        data="--quit--"
        
    else:
        data=""

    return data+"\n"

def prepData(rawdata):

    data = "||*"+str(len(rawdata))+"*||"+rawdata
    
    print(data)
    
    return data
    
def main001():

    print("Start main001")

    #get some data...
    #prepare some data for network processing...
#    rawdata=getData(1)
#    data="||"+len(""+(7+len(rawdata)))+"||"+rawdata
    
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

    try:
        print("7")
        print("sending data")
        sent=soc.send(prepData(getData(1)))
        print("total sent=%d"%sent)

        print("8")
        print("sending data")
        #prepare some data for network processing...
        #sent=soc.send(str.encode(data))
        sent=soc.send(prepData(getData(999)))
        print("total sent=%d"%sent)

        print("9")
        print("shutting down socket")
        sent=soc.shutdown(socket.SHUT_RDWR)

        print("10")
        print("close socket")
        sent=soc.close()

    except:
        print ("Unexpected error:", sys.exc_info()[0])
        raise

if __name__ == "__main__":

    main001()
