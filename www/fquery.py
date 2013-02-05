# encoding:utf-8
"""
读取倒排表，直接查询
"""


import fstd

#import finverted
import fredis


class fquery(object):
    def __init__(self):
        self.index = {}
        self.docidTohash = {}
        self.termdict = {}
        self.redis = fredis.fredis()
        
        self.loadIndexFile(fstd.rootpat+'file/termid')
        
        self.loadUrlfile(fstd.rootpat+'file/termid')
        
        self.loadTermfile()
    def loadTermfile(self):
        fp = open(fstd.rootpat+'data/fterms.dic','r')
        for each in fp:
            pos = each.find('###')
            if pos == -1:
                continue
            term = each[:pos]
            pos2 = each.find('\n')
            if pos2 == -1:
                continue
            id = each[pos+3:pos2]
            self.termdict[term] = int(id)
        fp.close()
    def loadIndexFile(self,filename):
        
        try:
#            print fstd.rootpat
            fp = open(fstd.rootpat+'file/termid','r')
        except IOError:
            print "can not open" ,str(IOError)
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
            pos2 = each.find('###',pos+3)
            url = each[pos+3:pos2]
            s = each[pos2 +3 : ]
            docid = int (s )
            self.docidTohash[docid] = [hashkey,url]
        fp.close()
    #这个函数对query 做了一个假设：查询词在term表中
    def query(self,q):
        
        option = 1 
        try:
            if self.redis.isOnlie() == True :
                option = 2
        except :
            pass
    
#        print self.index
        docs = [] 
        re = []
        if q  in self.termdict:
            termid = (self.termdict[q])
            docs = self.index[termid]
            
            if option == 2:
                for docid in docs:
                    c = self.redis.getRedis(str(docid))
                    re.append([c,self.docidTohash[docid][1]])
            else:
                for docid in docs:
                    fp = open(fstd.rootpat + 'file/'+self.docidTohash[docid][0]+'.text')
                    c =  fp.read()
#                print '----------------------------------------------------'
#                print c
                    re.append([c,self.docidTohash[docid][1]])
                    fp.close()
        return re

if __name__ == '__main__':
    f = fquery()
    print f.query('linux')
    print "done it"