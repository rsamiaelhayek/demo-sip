#!/usr/bin/env python3

from __future__ import print_function

import json
import socket
import sys

# Parse file and load to memory
jsonList = []
print("Started reading file with multiple JSON objects")
with open('regs') as f:
    for jsonObj in f:
        jsonDict = json.loads(jsonObj)
        jsonList.append(jsonDict)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 9999)
print('Starting up on %s port %s' % server_address, file=sys.stderr)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('Waiting for a connection', file=sys.stderr)
    connection, client_address = sock.accept()
    print('Connection address:', client_address)

    # Receive and decode data
    data = connection.recv(1024)
    stringdata = data.decode('utf-8')
    nodata = 'Empty request'
    emptyline = ' '

    # If request empty
    if not data:
        connection.send(nodata.encode())
    print("Received data:", stringdata)

    # Lookup AOR received and return JSON line or empty line if not found
    for i in jsonList:
        if i["addressOfRecord"] == stringdata:
            print(i)
            output = json.dumps(i)
            reply = output.encode()
            connection.sendall(reply)
            break
    else:
        print ("AOR not found")
        connection.send(emptyline.encode())

    connection.close()
