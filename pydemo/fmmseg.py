# encoding:utf-8
#  中文分词

import sys
import os
import fstd
class fmmseg(object):    
    def __init__(self):
        self.worddict = set() # 字典
        self.term = {} # 新文章的term词表
        self.termdict= {} # 原来所有单词的term表，对应id
    def loadWordFile(self,filename):
        
        fin1 = open('/home/fuxiang/python/fSearch-mini/pydemo/data/fchars.dic','rbU')
        for each in fin1:
            self.worddict.add(each[:each.find('\n')])
        fin1.close()
        fin2 = open('/home/fuxiang/python/fSearch-mini/pydemo/data/fwords.dic','rbU')
        for each in fin2:
            self.worddict.add(each[:each.find('\n')])
        fin2.close()
        fout = open('/home/fuxiang/python/fSearch-mini/pydemo/data/fout','w')
        for i in self.worddict:
            fout.write(i+'\r\n')
        
        fout.close()
    def segmentAFile(self,filename):
        fp = open(filename,'r')
        fout = open(filename[:filename.find('.')]+'.tmp','w')
#        fp = ['我是中国人','中国你好','沟通永不离线','精彩永不间断']
        i = 0
        for eachline in fp:
            print i ,":",eachline
            i = i +1
            if eachline.find('\n')!= -1:
                eachline = eachline[:eachline.find('\n')]
            if eachline == '' or eachline == '\n':
                continue
            s2 = self.cutWord(eachline)
            print s2
            fout.write(s2+'\n')
        fp.close()
        fout.close()
       
    
    def addTerm(self,word):
        if word in self.term:
            self.term[word]  = self.term[word] + 1
        else:
            self.term[word] = 1   
    def isAWord(self,word):
        if word in self.worddict:
            self.addTerm(word)
            return True
        return False
        
    
    def cutWord(self,line):
#        print line
        s1 = ''
        while line != '':
            if len(line) >= 8:
                w = line[0:12]
                line = line[12:]
            else:
                w = line
                line = ''
            
            s2 = ''
            while w != '':
#                print w
                if self.isAWord(w) == True:
                    s2 = w+'###'+s2
                    w = ''
                else:
                    self.addTerm(w[len(w)-3:])
                    s2 = w[len(w)-3:]+'###'+s2
                    w = w[:len(w)-3]
            s1 = s1 + s2
        return s1
            
                
                      
        
    #过滤掉非中文字符
    def preProcess(self,line):
        print line
    
    def loadTermfile(self):
        fp = open(fstd.rootpat+'data/fterms.dic','r')
        for each in fp:
            pos = each.find('#')
            if pos == -1:
                continue
            term = each[:pos]
            pos2 = each.find('\n')
            if pos2 == -1:
                continue
            id = each[pos+1:pos2]
            self.termdict[term] = int(id)
        fp.close()
    def mergeTerm(self):
        self.loadTermfile()
        fp = open('/home/fuxiang/python/fSearch-mini/pydemo/data/fterms.dic','a+')
       
        termcount = len(self.termdict.keys())
        for  t in self.term.keys():
            if t not in self.termdict:
                s = t + str('#') + str(termcount+1)
                termcount = termcount +1 
                fp.write(s+'\n')
        
        fp.close()     
        
def preFile():
    fp = open('/home/fuxiang/python/fSearch-mini/pydemo/data/chars.dic','r')
    fout = open('/home/fuxiang/python/fSearch-mini/pydemo/data/fchars.dic','w')
    for each in fp:
        fout.write(each[each.find(' ')+1:])  
        
#    fp = open('/home/fuxiang/python/fSearch-mini/pydemo/data/words.dic','r')
#    fout = open('/home/fuxiang/python/fSearch-mini/pydemo/data/fwords.dic','w')
#    for each in fp:
#        fout.write(each[each.find(' ')+1:])  
    
def test():
    fout = open('/home/fuxiang/python/fSearch-mini/pydemo/data/fout','rb')
    d = {}
    filenames = os.listdir(fstd.rootpat+'file')
    os.chdir(fstd.rootpat+'file')
    for each in fout:  
        if each in d :
            d[each] = d[each] +1
        else:
            d[each] = 1
        print each[:each.find('\n')]
if __name__ == "__main__":


    f = fmmseg()
    f.loadWordFile('none')
    s = f.worddict
    filenames = os.listdir(fstd.rootpat+'file')
    os.chdir(fstd.rootpat+'file')
    for filename in filenames:
        if filename.find('.text') != -1:
            f.segmentAFile(filename)
    f.mergeTerm()
    