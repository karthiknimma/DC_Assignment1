#ASSIGNMENT 1 (PART 1)
#AUTHOR1: Karthik Nimma (101650589)
#AUTHOR2: Maheen Tanveer (101673264)
#SUBMITTED TO : DR. ZHONGMEI YAO
#COURSE: DATA COMMUNICATIONS (CPS-570)




from Ass1Tcpsocket import TCPsocket
from Ass1Request import Request
from urllib.parse import urlparse
from URLparse import URLparse

import sys

def main():

    #Checking number of arguments
    if(len(sys.argv) != 2):
        print("Expecting one argument: URL")
        exit(0)
    hostname = sys.argv[1]
    # print(hostname)

    mysocket = TCPsocket() # create an object of TCP socket
    mysocket.createSocket()

    p = URLparse()
    host, path, query, port = p.parse(hostname)
    # print ('port:', port)

    #Resolve Ip address using dns
    ip = mysocket.getIP(host)

    mysocket.connect(ip, port)

    # build our request
    myrequest = Request()
    msg = myrequest.getRequest(host,path,query)

    # send out request
    mysocket.send(msg)
    data = mysocket.receive() # receive a reply from the server
    print('\nResponse content length: ', len(data), '\n')

    print(data)
    mysocket.close()

# call main() method:
if __name__ == "__main__":
   main()

