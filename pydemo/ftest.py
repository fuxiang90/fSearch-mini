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
    
if __name__ == '__main__':
    test1()
#    s = '123'
#    s = s.replace('2', '4')
#    print s