import select
import sys
import time
import socket


address = ('localhost',8092)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

socket_list = [server, sys.stdin]
print('waiting for connecting')
client, address = server.accept()
print("connect to:", address)
socket_list.append(client)

while True:
    print(">>>>>>>>>>>please type in<<<<<<<<<<:")
    input_data, out_data, except_data  = select.select(socket_list,[],[])

    for receive_data in input_data:
        if receive_data == sys.stdin:
            data = input()
            if data == 'quit()':
                running = 0
                client.send(data.encode())
                client.close()
                server.close()
                print ("server exits, chat is over")
                exit()
            send_msg = "<server>: %s:\n%s"%(time.ctime(),data)
            client.send(send_msg.encode())
        else:
            data = receive_data.recv(512)
            data = data.decode()
            if data == 'quit()':
                running = 0
                client.send(data.encode())
                client.close()
                server.close()
                print ("client exits, chat is over")
                exit()
            print(data)


