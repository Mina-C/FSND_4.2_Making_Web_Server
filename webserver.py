from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi                                                       # decipher the message that was sent from the server
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/delete'):
                restaurantIDPath = self.path.split('/')[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                if myRestaurantQuery != []:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body><h1>Are you sure you want to delete %s?</h1>" % myRestaurantQuery.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurant/%s/delete'><input type='submit' value='Delete'></form>" % restaurantIDPath
                    output += "</body></html>"
                    self.wfile.write(output)
                    print output
                    return

            if self.path.endswith("/edit"):
                restaurantIDPath = self.path.split('/')[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body><h1>"
                output += myRestaurantQuery.name
                output += "</h3>"
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurant/%s/edit'>" % restaurantIDPath
                output += "<input name='newRestaurantName' type='text' placeholder='%s'>" % myRestaurantQuery.name
                output += "<input type='submit' value='Rename'></form>"
                output += "</html></body>"
                self.wfile.write(output)
                print output
                return

            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output =""
                output +="<html><body>"
                output +="<h1>Make a New Restaurant</h1>"
                output +="<form method='POST' enctype='multipart/form-data' action='/restaurants/new'><input name='newRestaurantName' type='text' placeholder='New Restaurant Name'><input type='submit' value='Create'></form>"
                output +="</html></body>"
                self.wfile.write(output)
                print output
                return

            if self.path.endswith("/restaurants"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                restaurants = session.query(Restaurant).all()
                output = ""
                output += "<html><body>"
                output += "<a href = '/restaurants/new'><h3> Make a New Restaurant Here </h3></a>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br><a href='/restaurants/%s/edit'>Edit</a>" % restaurant.id
                    output += "</br><a href='/restaurants/%s/delete'>Delete</a>" % restaurant.id
                    output += "</br></br>"
                output += "</html></body>"
                self.wfile.write(output)
                print output
                return

            if self.path.endswith("/hello"):                     # find URL ends with '/hello'
                self.send_response(200)                          # if yes, send 200; successful GET request
                self.send_header('Content-type', 'text/html')    # telling to client that we will reply text in the form of HTML
                self.end_headers()                               # sends blank line, end of HTTP headers in the response

                output = ""                                      # empty for now
                output += "<html><body>Hello!"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text'><input type='submit' value='Submit'> </form>"
                output += "</body></html>"
                self.wfile.write(output)                         # sending a message back to the client
                print output                                     # print for myself
                return                                           # to exit if statement

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>&#161Hola!  <a href = '/hello'>Back to Hello</a>"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text'><input type='submit' value='Submit'> </form>"
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

        except IOErrors:
            self.send_error(404, "File Not Found %s" % self.path)    # to notify me error

    def do_POST(self):
        try:
            if self.path.endswith('/delete'):
                # Delete Restaurant Class
                restaurantIDPath = self.path.split('/')[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                if myRestaurantQuery != []:
                    session.delete(myRestaurantQuery)
                    session.commit()

            if self.path.endswith('/edit'):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields=cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')

                # Update Restaurant class
                restaurantIDPath = self.path.split('/')[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                if myRestaurantQuery != []:                    
                    myRestaurantQuery.name = messagecontent[0]
                    session.add(myRestaurantQuery)
                    session.commit()

            if self.path.endswith('/restaurants/new'):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields=cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')

                # Create new Restaurant class
                newRestaurant = Restaurant(name = messagecontent[0])
                session.add(newRestaurant)
                session.commit()
                
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.send_header('Location', '/restaurants')  # create redirect
            self.end_headers()

#            self.send_response(301)                                                    # send 301 ; successful POST request
#            self.end_headers()
#            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))    # parses an HTML form header
#            if ctype == 'multipart/form-data':                                         # check if the form-data is received
#                fields=cgi.parse_multipart(self.rfile, pdict)                          # collect all of the fields in a form
#                messagecontent = fields.get('message')                                 # call a filed named 'message'
#            output = ""
#            output += "<html><body>"
#            output += "<h2>OK, how about this: </h2>"
#            output += "<h1> %s </h1>" % messagecontent[0]
#            output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text'><input type='submit' value='Submit'> </form>"
#            output += "</body></html>"
#            self.wfile.write(output)
#            print output

        except:
            pass

def main():
    try:
        port = 8080 # port number is integer
        server = HTTPServer(('', port), webserverHandler) # host as an empty string
        print "Web Server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()

if __name__ == '__main__':
    main()
