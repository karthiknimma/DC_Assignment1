from Ass1Tcpsocket import TCPsocket
from Ass1Request import Request
from urllib.parse import urlparse

def main(): # function, method are the same

    mysocket = TCPsocket() # create an object of TCP socket
    mysocket.createSocket()
    host = 'www.yahoo.com'
    parse_result = urlparse(host)
    print(parse_result)
    print ('port    :', parse_result.port)
    ip = mysocket.getIP(host)
    port = 80
    mysocket.connect(ip, port)

    # build our request
    myrequest = Request()
    msg = myrequest.getRequest(host,parse_result.path,parse_result.query)
    # print(msg)
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

