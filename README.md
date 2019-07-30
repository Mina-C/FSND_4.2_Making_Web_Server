# FSND_4.2_Making_Web_Server
This is learning by coding for Full Stack Web Developer Nanodegree Program - 4. Servers, Authorization, and CRUD - 2. Making Web Server. </br>
There will be some errors in the previous commits. Because I made this commits after finished the course and written based on my notes, not during the course I was testing the code step by step.
Based on the restaurantmenu.db, web server is created. CRUD commands is included for this web page. </br>
This journey creates a web site purely from scratch, using a few internal libraries like BaseHTTPServer and external libraries like SQL Alchemy.

## How to run
You need Python(ver.3), SQL Alchemy and Linux-based virtual machine environment(Vagrant and VirtualBox).
  1. To make the virtual machine(VM) online, use the commands "vagrant up". Then log on it with "vagrant ssh".
    To download Vagrant : https://www.vagrantup.com/downloads.html </br>
    To download VirtualBox : https://www.virtualbox.org/wiki/Downloads
  2. To install SQL Alchemy, please visit this website : https://www.sqlalchemy.org/
  3. Please download "lotsofmenus.py", "database_setup.py", "webserver.py" "Vagrantfile". Then put this file into a shared directory.
	  Download "lotsofmenus.py" here - https://github.com/lobrown/Full-Stack-Foundations/blob/master/Lesson_1/lotsofmenus.py </br>
	  How to make shared directory? - https://www.howtogeek.com/189974/how-to-share-your-computers-files-with-a-virtual-machine/
  4. To make the database, "cd" into the shared directory and use the command "python lotsofmenus.py". Then, "restaurantmenu.db" file will be created.
  5. Please run the code with "python webserver.py". And to stop the server, please press Ctrl+C.
  6. Open the browser and type the address: http://localhost:8080/restaurants.
  
## Program's design
We used libraries: BaseHTTPServer is for server, sqlalchemy for database, cgi for deciphering the message that was sent from the server. And HTTP verbs, GET and POST, are used for CRUD functionality.</br>
If you run the server, open the browser and visit http://localhost:8080/restaurants, then you will see the list of restaurant name in the "restaurantmenu.db". You can create, edit and delete the restaurant list.
  
