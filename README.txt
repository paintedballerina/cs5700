# csS5700-proj1
CS5700 Project 1 - Sockets + Sprockets

This project is to test knowledge of sockets.
If successful *fingers crossed*...

1) Connect to a ccs.neu.edu server through a specific HOST and Port.
2) Send a NUID
3) Receive Sphynx riddle from the server with a math equation [ num num operator ]
4) Return answer to server
5) This process will repeat an unknown number of times with question --> answer.
6) Once answer is accepted it will return a secret code for the NUID
7) Connection terminated

HELLO --> connection made | send NUID
STATUS --> sphynx riddle
SOLUTION --> send solution [repeat riddle/solution]
BYE --> secret code | connection terminated
