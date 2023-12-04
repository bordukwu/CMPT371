# CMPT371
CMPT 371 MINI PROJECT

1. run python3 -m Webserver.py
2. then go to http://localhost:8000/test.html , console will prompt a password to enter. password is 'password'
3. go about testing the messages codes for: 
Code 	Message
200 	OK
304 	Not Modified
400 	Bad request
403 	Forbidden
404 	Not Found

the below is still a work in progress
411 	Length required

to test the proxy server
1. open 2 terminal windows
2. run  python3 -m proxy_server.py on terminal 1
3. run python3 -m Webserver.py on terminal 2
4. then go to http://localhost:8080/test.html , terminal 2 will assk for password , which shows a succesful redirection from proxy server to webserver 
