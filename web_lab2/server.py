import json
import socket
import select

HOST = 'localhost'
PORT = 1234
BACKLOG_SIZE = 10
SELECT_TIMEOUT = None
RECEIVE_BUFF_SIZE = 1024



def calculation(payload):
    res = str(int(payload) ** 2)
    return res


def http_creator(mes,host,port,version):
    content_type="text/html"
    http = ""

    http += f"POST HTTP/{version} 200 OK\n"
    http += f"Host: {host}:{port}\n"
    http += f"Content-Type: {content_type}\n"
    http += f"Content-Length: {len(str(mes))}"
    http += '\n\n'
    http += f"{mes}"
    return http

def deparsing_header(http):
    a = json.loads(http.decode())
    Headlines, body = a.split('\n\n')
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
    a=json.loads(http.decode())
    Headlines, body = a.split('\n\n')
    return body

def main():
    serverSocket = socket.socket()
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(BACKLOG_SIZE)


    readList = [serverSocket]
    writeList = []
    exceptionalList = [serverSocket]


    responsesMap = {}

    while True:

        readChanges, writeChanges, exceptionalChanges = select.select(readList, writeList, exceptionalList, SELECT_TIMEOUT)

        for rSocket in readChanges:

            if rSocket is serverSocket:

                client, _ = rSocket.accept()

                readList.append(client)
                exceptionalList.append(client)
            else:
                payload = rSocket.recv(RECEIVE_BUFF_SIZE)

                if payload is not None:
                    readList.remove(rSocket)
                    response = calculation(deparsing_body(payload))
                    deparsing_header(payload)
                    responsesMap[rSocket] = json.dumps(http_creator(response,HOST,PORT,"Marochkanych")).encode()
                    writeList.append(rSocket)


        for wSocket in writeChanges:

            response = responsesMap.get(wSocket)
            if response is not None:
                wSocket.send(response)
                responsesMap.pop(wSocket)
                writeList.remove(wSocket)
                exceptionalList.remove(wSocket)
                wSocket.close()


        for eSocket in exceptionalChanges:
            if eSocket in readList:
                readList.pop(eSocket)
            if eSocket in writeList:
                responsesMap.pop (eSocket)
                writeList.remove(eSocket)

            if eSocket is serverSocket:
                break
            else:
                exceptionalList.remove(eSocket)


if __name__ == '__main__':
    main()