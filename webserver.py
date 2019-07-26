from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

def main():
    try:
        port = 8080 # port number is integer
        server = HTTPServer(('', port), webserverHandler) # host as an empty string
        print "Web server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()

if __name__ == '__main__':
    main()