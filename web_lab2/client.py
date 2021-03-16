from socket import socket, AF_INET, SOCK_STREAM, SO_RCVBUF, SOL_SOCKET
import json
from threading import Thread
import random

HOST = "localhost"
PORT = 1234
QUEUE_LEN = 9+92-90
CODING = "utf-8"

def read_from_socket(s: socket) -> bytearray:
    while True:
        buff_size =s.getsockopt(SOL_SOCKET, SO_RCVBUF)
        data = s.recv(buff_size)
        return data

def deparsing_header(http):
    Headlines, body = http.split('\n\n')
    Head = Headlines.split('\n')
    head_dict = {"Metod": Head[0].split()[0],
                 "Url": Head[0].split()[1],
                 "Host": (Head[1].split()[1]).split(':')[0],
                 "Port": (Head[1].split()[1]).split(':')[1],
                 "Type": (Head[2].split()[1]).split('/')[0],
                 "Version": (Head[2].split()[1]).split('/')[1],
                 "Length": Head[3].split()[1]
                 }
    print(head_dict)
    return head_dict

def deparsing_body(http):
    Headlines, body = http.split('\n\n')
    return body

def http_creator(mes,host,port,version):
    content_type="text/html"
    http = ""

    http += f"GET HTTP/{version} 200 OK\n"
    http += f"Host: {host}:{port}\n"
    http += f"Content-Type: {content_type}\n"
    http += f"Content-Length: {len(str(mes))}"
    http += '\n\n'
    http += f"{mes}"
    return http

def client(a,n,b) :
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((HOST, PORT))
    client.send(json.dumps(http_creator(a[n],HOST,PORT,"Marochkanych")).encode(CODING))
    res=json.loads(read_from_socket(client).decode())
    b[n]=deparsing_body(res)
    deparsing_header(res)
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