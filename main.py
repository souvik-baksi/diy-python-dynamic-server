#!/server/web server
# Souvik Baksi

import socket
import view
import re

def get_page(match): #returns the whole page link in the form of a dictionary
    page = ['home']
    if match:
        match = match.group()
        print match # prints complete GET request
        page_request=re.search('test/\S+',match);
        if page_request:
            page_request = page_request.group()
            page_request=re.search('/\S+',page_request).group()
            page=re.findall('\w+',page_request)
    return page

def startserver(socObj):
    print 'Server started at', TCP_IP,':',TCP_PORT
    while True:
        conn, addr = socObj.accept()
        print '---\nConnection Request from', addr
        request = conn.recv(BUFFER_SIZE)
        print request

        if request:
            get_request=re.search('GET \w+://www.bingo.test.+\r',request); #Seperate the Gate Request
            if get_request:
                query=re.search('\?\S+',get_request.group());
                if query:
                    print query.group()

                else:
                    page=get_page(get_request)
                    print page
                    view.respond(page,conn)

            else:
                view.respond(['404error'],conn)
        conn.close()



if __name__=='__main__':

    #/default server socket specifications
    TCP_IP = '127.0.0.1'
    TCP_PORT = 8000
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    startserver(s)