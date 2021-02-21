from socket import socket, AF_INET, SOCK_STREAM, SO_RCVBUF, SOL_SOCKET
import json
import random

HOST = "localhost"
PORT = 1234
CODING = "utf-8"

def read_from_socket(s: socket) -> bytearray:
    buff_size =s.getsockopt(SOL_SOCKET, SO_RCVBUF)
    data = s.recv(buff_size)
    return data


def create():
    a=[]
    for i in range(11):
        a.append(random.randint(1,10))
    return a


def print_list(lst):
    for i in range(len(lst)):
        print(f"{i+1} : {lst[i]}")


def main() -> None:
    a = create()
    b=[]
    print_list(a)
    print("\n")

    client0 = socket(AF_INET, SOCK_STREAM)
    client0.connect((HOST, PORT))

    client1 = socket(AF_INET, SOCK_STREAM)
    client1.connect((HOST, PORT))

    client2 = socket(AF_INET, SOCK_STREAM)
    client2.connect((HOST, PORT))

    client3 = socket(AF_INET, SOCK_STREAM)
    client3.connect((HOST, PORT))

    client4 = socket(AF_INET, SOCK_STREAM)
    client4.connect((HOST, PORT))

    client5 = socket(AF_INET, SOCK_STREAM)
    client5.connect((HOST, PORT))

    client6 = socket(AF_INET, SOCK_STREAM)
    client6.connect((HOST, PORT))

    client7 = socket(AF_INET, SOCK_STREAM)
    client7.connect((HOST, PORT))

    client8 = socket(AF_INET, SOCK_STREAM)
    client8.connect((HOST, PORT))

    client9 = socket(AF_INET, SOCK_STREAM)
    client9.connect((HOST, PORT))

    client10 = socket(AF_INET, SOCK_STREAM)
    client10.connect((HOST, PORT))


    client0.send(json.dumps(a[0]).encode(CODING))
    client1.send(json.dumps(a[1]).encode(CODING))
    client2.send(json.dumps(a[2]).encode(CODING))
    client3.send(json.dumps(a[3]).encode(CODING))
    client4.send(json.dumps(a[4]).encode(CODING))
    client5.send(json.dumps(a[5]).encode(CODING))
    client6.send(json.dumps(a[6]).encode(CODING))
    client7.send(json.dumps(a[7]).encode(CODING))
    client8.send(json.dumps(a[8]).encode(CODING))
    client9.send(json.dumps(a[9]).encode(CODING))
    client10.send(json.dumps(a[10]).encode(CODING))

    b.append(read_from_socket(client0).decode(CODING))
    b.append(read_from_socket(client1).decode(CODING))
    b.append(read_from_socket(client2).decode(CODING))
    b.append(read_from_socket(client3).decode(CODING))
    b.append(read_from_socket(client4).decode(CODING))
    b.append(read_from_socket(client5).decode(CODING))
    b.append(read_from_socket(client6).decode(CODING))
    b.append(read_from_socket(client7).decode(CODING))
    b.append(read_from_socket(client8).decode(CODING))
    b.append(read_from_socket(client9).decode(CODING))
    b.append(read_from_socket(client10).decode(CODING))

    client0.close()
    client1.close()
    client2.close()
    client3.close()
    client4.close()
    client5.close()
    client6.close()
    client7.close()
    client8.close()
    client9.close()
    client10.close()

    print_list(b)


if __name__ == '__main__':
    main()