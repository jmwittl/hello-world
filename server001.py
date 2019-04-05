# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:52:45 2019

@author: jmwittl
Source:https://gist.githubusercontent.com/kuntalchandra/38656a8242273edb69c39f40eb20f210/raw/e30e78ba50e89b8efb36e3676e51d6c9c6797fef/server.py

"""

import socket
import sys
import traceback
from threading import Thread


def main():
    start_server()


def start_server():
    clientName="Linux-jmwittl-80GB"
    clientIp= socket.gethostbyname(clientName)

    serverName="raspberrypi-B"
    serverIp=socket.gethostbyname(serverName)
    serverPort='12345'
    serveraddress=(serverIp,serverPort)
    
    print("Connect to %s from %s\n"%(serverName,"n/a"))
    print("           %s      %s\n"%(serverIp,"n/a"))

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire
    print("Socket created")

    try:
        #blank means listen to any computer on the network
        soc.bind(('', serverPort))
    except:
        print("Bind failed. Error : " + str(sys.exc_info()))
        sys.exit()

    soc.listen(5)       # queue up to 5 requests
    print("Socket now listening")

    # infinite loop- do not reset for every requests
    while True:
        connection, address = soc.accept()
        ip, port = str(address[0]), str(address[1])
        print("Connected with " + ip + ":" + port)

        try:
            Thread(target=client_thread, args=(connection, ip, port)).start()
        except:
            print("Thread did not start.")
            traceback.print_exc()

    soc.close()


def client_thread(connection, ip, port, max_buffer_size = 5120):
    is_active = True

    while is_active:
        client_input = receive_input(connection, max_buffer_size)

        if "quit" in client_input:
            print("Client is requesting to quit")
            connection.close()
            print("Connection " + ip + ":" + port + " closed")
            is_active = False
        else:
            print("Processed result: {}".format(client_input))
            connection.sendall("-".encode("utf8"))


def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)

    if client_input_size > max_buffer_size:
        print("The input size is greater than expected {}".format(client_input_size))

    decoded_input = client_input.decode("utf8").rstrip()  # decode and strip end of line
    result = process_input(decoded_input)

    return result


def process_input(input_str):
    print("Processing the input received from client")

    return "Hello " + str(input_str).upper()

if __name__ == "__main__":
    main()