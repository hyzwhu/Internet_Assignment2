import select
import sys
import time

import socket
address = ('localhost',8092)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(address)

socket_list = [client, sys.stdin]
close_connection = 'close connection'
while True:
    print(">>>>>>>>>>>please type in<<<<<<<<<<:")
    input_data, out_data, except_data = select.select(socket_list, [], [])

    for receive_data in input_data:
        if receive_data == client:
            data = client.recv(512)
            data = data.decode()
            if (data == 'quit()'):
                client.send(data.encode())
                receive_data.close()
                print ("server exits, chat is over")
                client.close()
                exit()
            print(data)
        else:
            client_data = input()
            if (client_data == 'quit()'):
                client.send(client_data.encode())
                receive_data.close()
                print("client exits, chat is over")
                client.close()
                exit()
            send_msg = "<Client>: %s:\n%s"%(time.ctime(),client_data)
            client.send(send_msg.encode())
