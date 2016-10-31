# Caitlin Riley
# CS 5700 - Fall 2016
# Project 1
# Sockets and Sprockets
# Valid for Python 2.7.12 | another built for 3.5

# import libraries
import socket
import argparse
import ssl


# customs declaration
host = ""
port = ""
secure = ""
crn = "cs5700fall2016"
nuid = ""


# math function for later
def mathy(a, b, m):
    if m == "+":
        c = a + b
    elif m == "-":
        c = a - b
    elif m == "*":
        c = a * b
    elif m == "/":
        c = a // b
    else:
        c = "error in your math"
    return c

# Parser for command line input
parser = argparse.ArgumentParser(description="this is an example")
parser.add_argument("-p" , dest="port", action="store", help="port to connect on server", default=27993, type=int)
parser.add_argument("-s", dest="secure", action="store_true", help="set ssl flag", default=False)
parser.add_argument("host")
parser.add_argument("nuid")

args = parser.parse_args()

print(args.port)
print(args.secure)


# HELLO -- create connection | check SSL | send init data
hello = "%s %s %s\n" % (crn, "HELLO", args.nuid)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if args.secure and args.port == 27993:
    args.port = 27994
    secureSocket = ssl.wrap_socket(s)

    try:
        secureSocket.connect((args.host, args.port))
        secureSocket.send(hello.encode('utf-8'))

    except socket.error as err:
        print("Connection fail!  Error %s" % (err))

else:
    try:
        s.connect((args.host, args.port))
        s.send(hello.encode('utf-8'))

    except socket.error as err:
        print("Connection nope!  Error %s" % err)

# STATUS + SOLUTION -- these dance with each other until Sphinx happy
# Read message for "BYE"
# if found --> quest complete, set secret
# if not found --> quest continues, do math stuff
# -- convert to int --> pass to math fx
# -- pass back to socket

quest = True

while quest:
    msg = s.recv(256)

    # parse the sphynx's riddle
    sphynx = msg.split()
    # what is your quest?
    if sphynx[2] == "BYE":
        quest = False

        # found secret passcode
        secret = sphynx[1]

    # do math stuff ser gallahad | SOLUTION
    else:
        a = int(sphynx[2])
        b = int(sphynx[4])
        m = sphynx[3]
        result = mathy(a, b, m)
        solution = "%s %s\n" % (crn, result)
        s.send(solution.encode('utf-8'))

# BYE -- close the connection
print(secret)
s.close
