from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi                                                       # decipher the message that was sent from the server

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):                     # find URL ends with '/hello'
                self.send_response(200)                          # if yes, send 200; successful GET request
                self.send_header('Content-type', 'text/html')    # telling to client that we will reply text in the form of HTML
                self.end_headers()                               # sends blank line, end of HTTP headers in the response

                output = ""                                      # empty for now
                output += "<html><body>Hello!</body></html>"
                self.wfile.write(output)                         # sending a message back to the client
                print output                                     # print for myself
                return                                           # to exit if statement

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>&#161Hola!  <a href = '/hello'>Back to Hello</a>"
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return
            
        except IOErrors:
            self.send_error(404, "File Not Found %s" % self.path)    # to notify me error

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
