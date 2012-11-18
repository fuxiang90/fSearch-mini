# encoding:utf-8
import sys
import re
import socket
import time
import os
import fhash
import fstd

import fcrawl

def test1():
    
    
#    os.chdir(fstd.rootpat+'file')
    fp = open(fstd.rootpat+'file/6f33270959d5361662ec74a72e5ea7094b5f591f')
    
    t = fp.read()
    text = ''
    while t != '':
        
        pos1 = t.find('<')
        if pos1 == -1:
            text = text + t
            break
        else:
            text = text + t[:pos1]
        pos2 = t.find('>',pos1+1)
        t = t[pos2+1:]
    text = text.replace(' ', '')
#    text.replace('', '\n')
    
#    text = fstd.filter_tags(t)
    print text
    fout = open(fstd.rootpat+'file/6f33270959d5361662ec74a72e5ea7094b5f591f' + '.text','w')
    fout.write(text)
    fp.close()
    fout.close()
 
 

def test2():
    import zmq 
    context = zmq.Context()

    #  Socket to talk to server
    print "Connecting to hello world server"
    socket = context.socket(zmq.REQ)
    socket.connect ("tcp://localhost:5555")

    #  Do 10 requests, waiting each time for a response
    for request in range (10):
        print "Sending request ", request,"..."
        socket.send ("Hello")
    
     #  Get the reply.
        message = socket.recv()
        print "Received reply ", request, "[", message, "]"
    
def test3():
    
    str = "我是付翔"
    print len(str)
    for i in str:
        print int(i)
    
    
if __name__ == '__main__':
    
    test3()
#    test1()
#    s = "1234"
#    print s.find('1')
#    s1 = s[:s.find('1')]
#    s2 = s[s.find('1'):]
#    print s1
#    print s2
#    fp = open(fstd.rootpat+'data/fterms.dic','r')
#    for each in fp:
#        print each
#    s = '123'
#    s = s.replace('2', '4')
#    print s