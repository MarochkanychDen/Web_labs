from socket import socket, AF_INET, SOCK_STREAM, SO_RCVBUF, SOL_SOCKET
import json
from threading import Thread
import random

HOST = "localhost"
PORT = 1235
QUEUE_LEN = 9+92-90
CODING = "utf-8"

def read_from_socket(s: socket) -> bytearray:
    while True:
        buff_size =s.getsockopt(SOL_SOCKET, SO_RCVBUF)
        data = s.recv(buff_size)
        return data

def deparsing(http):

    body=http.get("Body")
    head_dict = {
                 "Host": http.get("Host"),
                 "Port": http.get("Port"),
                 "Type": http.get("Content-Type"),
                 "Length": http.get("Content-Length")
                 }
    print(head_dict)
    return body

def http_creator(mes,host,port,version):
    content_type="text/html"
    http = {
     "Url": f"GET HTTP/{version} 200 OK\n",
     "Host": host ,
     "Port": port,
     "Content-Type": content_type,
     "Content-Length": len(str(mes)),
     "Body": mes
    }
    return http

def client(a,n,b) :
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((HOST, PORT))
    client.send(json.dumps(http_creator(a[n],HOST,PORT,"Marochkanych")).encode(CODING))
    res=json.loads(read_from_socket(client).decode())
    b[n]=deparsing(res)
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
    b = a
    c=[]
    print("")
    p=[]
    for i in range(QUEUE_LEN):
        potok = Thread(target= client, args=(a,i,b))
        potok.start()
        p.append(potok)

    for potok in p:
        potok.join()

    print_list(b)
    print_list(c)

if __name__ == '__main__':
    main()