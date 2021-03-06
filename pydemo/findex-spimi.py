#encoding:utf-8
"""
建立倒排表
采用单遍扫描索引建立的方法

"""
import os
import fstd
import fmmseg
import fstopword
class findexspimi(object):
    def __init__(self):
        self.mainindex = {}
        self.index = {}
        self.termdict = self.loadTermfile()
        self.mmseg = fmmseg.fmmseg()  
        self.k = 500
        self.pos = 0
        self.filename = []
        self.fhashkeyToid = self.loadUrlfile(fstd.rootpath+'file/url')
        os.chdir(fstd.rootpath+'file')
        
        self.fstop = fstopword.fstopword()
    
    def loadTermfile(self):
        fp = open(fstd.rootpath+'data/fterms.dic')
        termdict = {}
        for each in fp:
            if each == '\n' :
                continue
            if each == '' :
                continue
            pos = each.find('###')
            if pos == -1 :
                continue
            term = each[:pos]
            id = int(each[pos+3:len(each)-1])
            termdict[term] = id
        return termdict
            
    def loadUrlfile(self,filename):
        fp = open(filename,'r')
        hashkeyToid = {}
        for each in fp:
            if each == '\n' :
                continue
            pos = each.find('###')
            hashkey = each[:pos]
            pos2 = each.find('###',pos+3)
            id = each[pos2+3:len(each)-1]
            hashkeyToid[hashkey] = int(id)
        return hashkeyToid
    def getfilename(self):
        filenames = open(fstd.rootpath+'file/newurl')
#        lenfile = len(self.fhashkeyToid)
        for filename in filenames:
            pos = filename.find('\n')
            if pos != -1:
                filename = filename[:pos]
            self.filename.append(filename)
#            lenfile = lenfile + 1
#            self.fhashkeyToid[filename] = lenfile
    def getKfile(self):
        tempfile = []
        for i in range(0,self.k):
            t = []
            if self.pos == len(self.filename):
                break
            fp = open(self.filename[self.pos]+'.text')
            t.append(fp.read())
            t.append(self.fhashkeyToid[self.filename[self.pos]])
            self.pos = self.pos + 1
            tempfile.append(t)
        return tempfile
    
    #将中间生成的temp index 写进文件里面去
    def writeTempIndex(self,indexid ,index):
        fout = open("index."+str(indexid),"w")
        for i in index:
#            s = ' '.join(index[i])
            s = ''
            for ii in index[i]:
                s = s + str(ii) + ' '
            fout.write(str(i)+':'+s+'\n')
        fout.close()
        
        
        
    def spimi(self):
        self.getfilename()
        
        import jieba
        indexid = 0
        while True:
            
            indexid = indexid + 1 
            print "now is ",indexid
            files = self.getKfile()
            if files == [] :
                break
            
            for file in files:
#                s1 = self.mmseg.cutWord(file)
                cutstr = jieba.cut(file[0], cut_all = True)
                docid = file[1]
                for term in cutstr:
                    if term == '':
                        continue
                    if self.fstop.isStop(term) == True:
                        continue
                    pos= 0
                    if term  in self.termdict:
                        pos = self.termdict.get(term)
                        if pos == None :
                            continue
                        pos = int( self.termdict[term] )
                        
                    else:
                        lendict = len(self.termdict)
                        self.termdict[term] = lendict + 1
                        pos = lendict + 1
#                       
                    termid = pos
                    if termid not in self.index:
#                            self.index[termid] = set()
                            self.index[termid] = []
#                    self.index[termid].add(docid)
                    self.index[termid].append(docid)
                
            
#            print self.index
            
        
        self.mergeIndex(indexid)
    
    def getIndexfile(self,filename):
        fin = open(filename)
        tempindex = {}
        for terms in fin :
            if terms == "\n":
                continue
            pos = terms.find('\n')
            t = []
            if pos != -1 :
                terms = terms[:pos]
            if terms  == "":
                continue
            pos2 = terms.find(':')
            termid = int(terms[:pos2])
            terms = terms[pos2 +1:]
#            tempindex[termid] = set()
            tempindex[termid] = []
            for docid in  str(terms).split():
#                tempindex[termid].add(int(docid))
                tempindex[termid].append(int(docid))
        return tempindex
    
    def mergeList(self,a,b):
        c = a+b 
        return list(set(c))     
    def mergeIndex(self,indexcount):
     
        indexmain = self.getIndexfile("index.main")
        newindex = {}
        
#        print indexmain ,"---------------\n",self.index
        for i in self.index:
            if i not in indexmain:
                newindex[i] = self.index[i]
            else:
#                newindex[i] = self.index[i] | indexmain[i]
                 newindex[i] = self.mergeList(self.index[i] ,indexmain[i])
#            print newindex[i]
#        print newindex
        self.storeMainIndex(newindex)
        self.storeTermfile()
        
    
    def storeTermfile(self):
        print "store Termfile" ,len(self.termdict)
        fout = open(fstd.rootpath + 'data/fterms.dic','w')
        pos = 0
        for i in self.termdict:
            if i == '':
                continue
            pos = pos + 1
            if pos == 1:
                continue
            
#            print str(i)
            try:
                s = str(i)  + '###' + str(self.termdict[i])
            
                fout.write(s+'\n')
            except:
                print "error ",i
                continue
        fout.close()
            
        
    def storeMainIndex(self,index):
        fout = open("index.main","w")
        for i in index:
#            s = ' '.join(index[i])
            s = ''
            for ii in index[i]:
                s = s + str(ii) + ' '
            fout.write(str(i)+':'+s+'\n')
        fout.close()
            
        
            
 
def run():
    import time
 
    t1 = time.clock()
    f = findexspimi()
    
#    print f.fhashkeyToid
#    t =  f.getKfile()
#    print len(t)
    
#    print f.getIndexfile("index.main")
    f.spimi()
    t2 = time.clock()
    print (t2 - t1)      
        

def runWithProfie():
    pass




if __name__ == "__main__":
    
    run()
    print "done it"
    
    