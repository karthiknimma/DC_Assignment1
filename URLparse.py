from urllib.parse import urlparse


class URLparse:
    def __init__(self):
        self.url = ""  # each object's instance variables
        self.port = ""
        self.path = ""  # remote host name
        self.query = ""
        self.path = ""
        print("create an object of TCPsocket")


def parse(self,url):
    o = urlparse(url)
    return o
    # if(o.path)