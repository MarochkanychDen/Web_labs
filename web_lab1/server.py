from socket import socket, AF_INET, SOCK_STREAM, SO_RCVBUF, SOL_SOCKET
from threading import Thread

HOST = "localhost"
PORT = 1234
QUEUE_LEN = 11
CODING = "utf-8"

def read_from_socket(s: socket) -> bytearray:
    buff_size =s.getsockopt(SOL_SOCKET, SO_RCVBUF)
    data = s.recv(buff_size)
    return data

def calculation(num: bytearray,client_socket:socket):
    new_num=num.decode(CODING)
    res=str(int(new_num)**2)
    client_socket.send(res.encode(CODING))



def main() -> None:
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(QUEUE_LEN)
    print("Ready, Daddy")
    while True:
        (client_socket, client_info) = sock.accept()
        raw_payload = read_from_socket(client_socket)

        potok =Thread(target= calculation,args=(raw_payload,client_socket))
        potok.start()
        potok.join()
        client_socket.close()

if __name__ == '__main__':
    main()