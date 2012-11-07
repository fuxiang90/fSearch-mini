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
        self.fhashkeyToid = finverted.loadUrlfile(fstd.rootpat+'file/url')
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
            s = str(termids)+'###'
            for termid in self.index[termids]:
                s = s+str(termid) +'###'
            fout.write(s+'\n')
        fout.close()   
    #===========================================================================
    # 合并索引  下次要把各自的依赖关系理清才行
    #===========================================================================
    def MergeIndex(self):
        self.fhashkeyToid = finverted.loadUrlfile(fstd.rootpat+'file/url')
        
        fp = open(fstd.rootpat+'file/termid','r')
        for each in fp:
            pos1 = each.find('###')
            termid = int(each[:pos1])
            self.index[termid] = set()
            s = each[pos1 + 3:]
            pos2 = s.find('###')
            while pos2 != -1 :
                docid = int(s[:pos2])
                self.index[termid].add(docid)
                s = s[pos2+3:]
                pos2 = s.find('###')
            
        fp.close()
        
        
        #对新的文件进行分词
        os.chdir(fstd.rootpat+'file')
        fm = fmmseg.fmmseg()
        fm.loadTermfile()
        furl = open(fstd.rootpat+'file/newurl','r')
        for url in furl:
            url = url[:url.find('\n')]
            fm.segmentAFile(url+'.text')
            self.fhashkeyToid[url] = docid
 
        
        fm.mergeTermJieba()
        
        furl.close()
        #进行索引
        furl = open(fstd.rootpat+'file/newurl','r')
        
        for filename in furl:
            
            filename = filename[:filename.find('\n')]
            filename = filename+'.tmp'
            if True:
                print filename
                fp = open(filename,'r')
                hashkey = filename
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
        
        print self.index[2] 
        print '索引建好了'
        fout = open(fstd.rootpat+'file/termid','w')
        for termids in self.index.keys():
            s = str(termids)+'###'
            for termid in self.index[termids]:
                s = s+str(termid) +'###'
            fout.write(s+'\n')
        fout.close()   
        
if __name__ == '__main__':
    f = findex()
#    f.creatIndex()
    f.MergeIndex()
    print "done it"
        
        
        
    