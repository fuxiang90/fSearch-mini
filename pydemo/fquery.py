# encoding:utf-8
"""
读取倒排表，直接查询
"""

import os
import fstd
import fmmseg
import fhash
import finverted

class fquery(object):
    def __init__(self):
        self.index = {}
        self.docidTohash = {}
    def loadIndexFile(self,filename):
        fp = open(fstd.rootpat+'file/termid','r')
        for each in fp:
            pos = each.find('###')
            termid = int (each[:pos])
            self.index[termid] = set()
            t = each[pos+3:]
            while t != '':
                if t == ' ':
                    break
                pos1 = t.find('###')
                if pos1 == -1:
                    break
                docid = int(t[:pos1])
                self.index[termid].add(docid)
                t = t[pos1+3:]
        fp.close()
    def loadUrlfile(self,filename):
        fp = open(fstd.rootpat+'file/url','r')
        
        for each in fp:
            pos = each.find('###')
            hashkey = each[:pos]
            s = each[each.find('###',pos+3) +3 : ]
            docid = int (s )
            self.docidTohash[docid] = hashkey
        fp.close()
    #这个函数对query 做了一个假设：查询词在term表中
    def query(self,q):
        self.loadIndexFile(fstd.rootpat+'file/termid')
        self.loadUrlfile(fstd.rootpat+'file/termid')
        fm = fmmseg.fmmseg()
        fm.loadTermfile()
#        print self.index
        docs = [] 
        re = []
        if q  in fm.termdict:
            termid = int(fm.termdict[q])
            print termid
            docs = self.index[termid]
            print docs
            for docid in docs:
                fp = open(fstd.rootpat + 'file/'+self.docidTohash[docid]+'.text')
                c =  fp.read()
                print '----------------------------------------------------'
                print c
                re.append(c)
                fp.close()

if __name__ == '__main__':
    f = fquery()
    f.query('linux')
    
    print "done it"