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

# parsing of arguments per assignment parameters
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=int, help='Is port set?', dest='port')
    parser.add_argument('-s', type=str, help='Is SSL checked?', dest='bleed')
    parser.add_argument('host', type=str, help='CCS address')
    parser.add_argument('nuid', type=str, help='NUID')


# math function for later
def mathy(a, b, o):
    if o == '+':
        c = a + b
    elif o == '-':
        c = a - b
    elif o == '*':
        c = a * b
    elif o == '/':
        c = a // b
    else:
        c = "error in your math"
    return c


# CONNECT -- connect to host
# set host & reserve port
# connect to CCS Server
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "HELLO WORLD! Sprocket Created."
    s.connect((host, port))
except socket.error as err:
    print "Connection fail!  Error %s" % (err)

# HELLO -- send NUID
s.send( crn + ' HELLO ' + nuid + '\n')
print "cs5700fall2016 HELLO ######574"

# STATUS -- receive sphynx equation


# SOLUTION -- answer sphynx
# Read message for "BYE"
# if found --> quest complete, set secret
# if not found --> quest continues, do math stuff
# -- convert to int --> pass to math fx
# -- pass back to socket

quest = True

while quest:
    msg = s.recv(256)
    print msg

    # parse the sphynx's riddle
    sphynx = msg.split(' ')

    # what is your quest?
    if sphynx[3] == "BYE":
        quest = False

        # found secret passcode
        secret = sphynx[2]

    # do math stuff ser gallahad
    else:
        a = int(sphynx[2])
        b = int(sphynx[4])
        o = sphynx[3]
        result = mathy(a, b, o)
        s.send(crn + str(result) + "\n")

# BYE -- close the connection
print secret
s.close
