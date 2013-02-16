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
        fin = open(filename)
        self.index = {}
        for terms in fin :
            if terms == "\n":
                continue
            pos = terms.find('\n')
            t = []
            if pos != -1 :
                terms = terms[:pos]
            pos2 = terms.find(':')
            termid = int(terms[:pos2])
            terms = terms[pos2 +1:]
            self.index[termid] = set()
            for docid in  str(terms).split():
                self.index[termid].add(int(docid))
        fin.close()
    def loadUrlfile(self,filename): 
        
        fp = open(filename,'r')
        
        for each in fp:
            pos = each.find('###')
            hashkey = each[:pos]
            s = each[each.find('###',pos+3) +3 : ]
            docid = int (s )
            self.docidTohash[docid] = hashkey
        fp.close()
    #这个函数对query 做了一个假设：查询词在term表中
    def query(self,q):
        self.loadIndexFile(fstd.rootpath+'file/index.main')
        self.loadUrlfile(fstd.rootpath+'file/url')
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
                fp = open(fstd.rootpath + 'file/'+self.docidTohash[docid]+'.text')
                c =  fp.read()
                print '----------------------------------------------------'
                print c
                re.append(c)
                fp.close()
    def getDocList(self,query):
        self.loadIndexFile(fstd.rootpath+'file/index.main')
        self.loadUrlfile(fstd.rootpath+'file/url')
        fm = fmmseg.fmmseg()
        fm.loadTermfile()
#        print self.index
        docs = [] 
 
        if query  in fm.termdict:
            termid = int(fm.termdict[query]) 
            print termid
            docs = self.index[termid]
        
        return docs

if __name__ == '__main__':
    f = fquery()
    f.query('linux')
    
    print "done it"
