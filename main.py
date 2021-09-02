from Ass1Tcpsocket import TCPsocket
from Ass1Request import Request
from urllib.parse import urlparse
from URLparse import URLparse

import sys





def main(): # function, method are the same
    #Checking number of arguments
    if(len(sys.argv) != 2):
        print("Expecting one argument: URL")
        exit(0)

    print('Argument List:', str(sys.argv))
    mysocket = TCPsocket() # create an object of TCP socket
    mysocket.createSocket()
    hostname = sys.argv[1]
    print(hostname)
    p = URLparse()
    host, path, query, port = p.parse(hostname)
    print ('port    :', port)
    ip = mysocket.getIP(host)

    mysocket.connect(ip, port)

    # build our request
    myrequest = Request()
    msg = myrequest.getRequest(host,path,query)
    print(msg)
    # msg = myrequest.headRequest(host)

    # send out request
    mysocket.send(msg)
    data = mysocket.receive() # receive a reply from the server

    # pop the first line so we only process headers
    headers = {}
    headers = data.split("\r\n")
    print(headers)
    # fields = data.split("\r\n")
    # fields = fields[1:]  # ignore the GET / HTTP/1.1
    # output = {}
    # for field in fields:
    #     key, value = field.split(':')  # split each line by http field name and value
    #     output[key] = value
    # print(output)

    # print("data received: ", data)

    mysocket.close()

# call main() method:
if __name__ == "__main__":
   main()

