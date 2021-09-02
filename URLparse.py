from urllib.parse import urlparse


class URLparse:
    def __init__(self):
        self.host = ""  # each object's instance variables
        self.port = ""
        self.path = ""  # remote host name
        self.query = ""
        self.path = ""

    def parse(self,url):
        o = urlparse(url)
        if(o.netloc) != '':
            self.host = o.netloc

        if(o.port != ''):
            self.port = o.port
        else:
            self.port = o.port

        if(o.path != ''):
            self.path=o.path
        else:
            self.path = '/'

        if(o.query != ''):
            self.query=o.query
        else:
            self.query=''

        print(self.host,self.path,self.query,self.port)
        return o
        # if(o.path)