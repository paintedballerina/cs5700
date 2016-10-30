# Caitlin Riley
# CS 5700 - Fall 2016
# Project 1
# Sockets and Sprockets

# import libraries
import socket
import argparse
import sys
import ssl


# customs declaration
host = 'cs5700f16.ccs.neu.edu'
port = 27993

crn = 'cs5700fall2016'
nuid = '000547574'


# math function for later
# error handling: should have "else: math problem"
def mathy(a, b, m):
    if m == '+':
        c = a + b
    elif m == '-':
        c = a - b
    elif m == '*':
        c = a * b
    else:
        c = a // b
    return c


# HELLO -- create connection | check SSL | send init data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send( crn + ' HELLO ' + nuid + '\n')


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
        solution = "%s %d\n" % (crn, result)
        s.send(solution)

# BYE -- close the connection
print(secret)
s.close
