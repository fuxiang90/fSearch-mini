# encoding:utf-8
"""
建立倒排表
最初的程序写在finverted ，这里写成一个类的形式
"""
import os
import fstd
import fmmseg
import fhash
import finverted

class findex(object):
    def __init__(self):
        self.fhashkeyToid = {} # 每个url的hash 对应一个id（long 型）
        self.index = {}
    
    #直接从分词文件中，建立倒排表
    def creatIndex(self):
        self.fhashkeyToid = finverted.loadUrlfile(fstd.rootpat+'url')
        fm = fmmseg.fmmseg()
        fm.loadTermfile() #
        
        
        filenames = os.listdir(fstd.rootpat+'file')
        os.chdir(fstd.rootpat+'file')
        for filename in filenames:
            
            fpos = filename.find('.tmp')
            if fpos != -1:
                print filename
                fp = open(filename,'r')
                hashkey = filename[:fpos]
                if hashkey not in self.fhashkeyToid:
                    continue
                docid = self.fhashkeyToid[hashkey]
                for each in fp:
                    if each == '\n':
                        continue
                    s = each[:each.find('\n')]
                    while s != '':
                        pos = s.find('###')
                        if pos == -1:
                            break
                        s1 = s[:pos]
                        if s1 == '':
                            break
                        if s1 not in fm.termdict:
                            s = s[pos+3:]
                            continue
                        id = fm.termdict[s1]
                        if id not in self.index.keys():
                                self.index[id] = set()
                        self.index[id].add(docid)
                        s = s[pos+3:]
                    
                fp.close()
        print self.index
        fout = open(fstd.rootpat+'file/termid','w')
        for termids in self.index.keys():
            s = str(termids)+'##'
            for termid in self.index[termids]:
                s = s+str(termid) +'#'
            fout.write(s+'\n')
        fout.close()   

if __name__ == '__main__':
    f = findex()
    f.creatIndex()
    print "done it"
        
        
        
    