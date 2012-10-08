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
    def loadIndexFile(self,filename):
        fp = open(fstd.rootpat+'file/termid','r')
        for each in fp:
            pos = each.find('##')
            termid = int (each[:pos])
            self.index[termid] = set()
            t = each[pos+2:]
            while t != '':
                if t == ' ':
                    break
                pos1 = t.find('#')
                if pos1 == -1:
                    break
                docid = int(t[:pos1])
                self.index[termid].add(docid)
                t = t[pos1+1:]
        fp.close()
    #这个函数对query 做了一个假设：查询词在term表中
    def query(self,q):
        self.loadIndexFile('file/termid')
        fm = fmmseg.fmmseg()
        fm.loadTermfile()
        print self.index
        docs = [] 
        if q  in fm.termdict:
            termid = (fm.termdict[q])
            print termid
            docs = self.index[termid]
            print docs

if __name__ == '__main__':
    f = fquery()
    f.query('你好')