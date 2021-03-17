import json
import socket
import select

HOST = 'localhost'
PORT = 1235
BACKLOG_SIZE = 10
SELECT_TIMEOUT = None
RECEIVE_BUFF_SIZE = 1024



def calculation(payload):
    res = str(int(payload) ** 2)
    return res


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


def deparsing(http):
    a=json.loads(http.decode())
    body=a.get("Body")
    head_dict = {
                 "Host": a.get("Host"),
                 "Port": a.get("Port"),
                 "Type": a.get("Content-Type"),
                 "Length": a.get("Content-Length")
                 }
    print(head_dict)
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
                    response = calculation(deparsing(payload))
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