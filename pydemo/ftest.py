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
    import jieba
    str = "我是   中国人"
    seg_list = jieba.cut(str,cut_all=True)
    s1 = ' '.join(seg_list)
    
    print s1
    return s1

#测试下 写一个函数判断是否是停用词 or 无意义的词
def test4():
    
    fp = open("data/fterms.dic")
    
    fout = open("data/fterms.1" ,"w")
    for i in fp:
        s = i[:i.find('#')]
    
#        if re.match(u'^[\4e00-9fa5]+$',s): ##此处的u不能省去的哦
#            print 'yes'
#        else :
#            print " not chinese"
        n = 0
        for uu in s :
            if ord(uu) >= 233 :
                n = 1
                break
        
        if n == 1:
            fout.write(s+'\n')
     


def test5():
    fp = open("data/fterms.dic")
    
    fout = open("data/fterms.2" ,"w")
    for i in fp:
        s = i[:i.find('#')]

        for uu in s :
            fout.write(str (ord(uu) ) + '\t' )
        fout.write('\n')    
 
 
def judgeCharset(filename):
    
    import jieba
    
    
    fp = open(filename)
    
    import chardet
    
    str = fp.read()
    seg_list = jieba.cut(str ,cut_all=True)
    
    s1 = '###'.join(seg_list)
    print s1
    print chardet.detect(s1)
    print chardet.detect(str)
    
    fout = open("12-14","w")
    fout.write(s1+'\n') 

def testjieb():
    import sys
    sys.path.append("../")
    import jieba
    test_sent = "这是一个伸手不见五指的黑夜。我叫孙悟空，我爱北京，我爱Python和C++。"
    result = jieba.cut(test_sent,cut_all=True)
    for word in result:
        print word
    print ""

def testDict():
    import time
    d = {}
    t1 = time.clock()
    fp = open('./data/fterms.dic')
    pos = 1
    for i in fp:
        d[i] = pos
        pos = pos + 1
    fp.close()
    t2 = time.clock()
    print (t2 - t1)/1000000
    
    fp2 = open('./data/fterms.dic')
    for i in fp2:
#        if i in d.keys():
        if i in d:
#        if d.has_key(i):
            d[i] = d[i] + 1
    
    fp2.close()
    t3 =  time.clock()
    print (t3 - t2)/1000000
    
    
if __name__ == '__main__':
#    testjieb()
#    judgeCharset("file/5197f1a79f5adae1818ca6f9bb4b3375c809397b.text")
#    test5()
    import cProfile
    cProfile.run("testDict()")
    import pstats
    p = pstats.Stats("prof.txt")
    p.sort_stats("time").print_stats()
    print "done it"
