# csS5700-proj1
CS5700 Project 1 - Sockets + Sprockets

This project is to test knowledge of sockets.
If successful *fingers crossed*...

1) Connect to a ccs.neu.edu server through a specific HOST and Port.
2) HELLO: Send message with NUID
3) STATUS: Receive Sphynx riddle from the server with a math equation [ num num operator ]
4) SOLUTION: Return answer to server
5) This process will repeat an unknown number of times with question --> answer.
6) Once answer is accepted it will return a secret code specific to the NUID
7) BYE: secret_flag and Connection terminated

HELLO --> connection made | send NUID
STATUS --> sphynx riddle
SOLUTION --> send solution [repeat riddle/solution]
BYE --> secret code | connection terminated

COGNITIVE DISSONANCE:
- Version management for Python —> 2 vs 3 have major differences in layout and usage
- Final version is built for 2.7.15
- Most difficult part was figuring out how to parse input and convert data types