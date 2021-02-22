from socket import socket, AF_INET, SOCK_STREAM, SO_RCVBUF, SOL_SOCKET
import json
from threading import Thread
import random

HOST = "localhost"
PORT = 8888
QUEUE_LEN = 11
CODING = "utf-8"

def read_from_socket(s: socket) -> bytearray:
    buff_size =s.getsockopt(SOL_SOCKET, SO_RCVBUF)
    data = s.recv(buff_size)
    return data

def client(a,n,b) :
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((HOST, PORT))
    client.send(json.dumps(a[n]).encode(CODING))
    b.append(read_from_socket(client).decode(CODING))
    client.close()

def create():
    a=[]
    for i in range(QUEUE_LEN):
        a.append(random.randint(1,15))
    return a


def print_list(lst):
    for i in range(len(lst)):
        print(f"{i+1} : {lst[i]}")



def main() -> None:
    a = create()
    print_list(a)
    b = []
    print("")

    for i in range(QUEUE_LEN):
        potok = Thread(target= client, args=(a,i,b))
        potok.start()
        potok.join()


    print_list(b)


if __name__ == '__main__':
    main()