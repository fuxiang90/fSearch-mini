# encoding:utf-8
"""
.text 文件整理成 doc -- termid 的形式，
然后再建立 termid  和 docid 的倒排表

"""
import os
import fstd
import fmmseg
import fhash
def tidyTextfile():
    fm = fmmseg.fmmseg()
    fm.loadTermfile()
    filenames = os.listdir(fstd.rootpat+'file')
    os.chdir(fstd.rootpat+'file')
    for filename in filenames:
        if filename.find('.tmp') != -1:
            fp = open(filename,'r')
            fout = open(filename[:filename.find('tmp')]+'term','w')
            sw = ''
            for each in fp:
                if each == '\n':
                    continue
                s = each[:each.find('\n')]
                print s,filename
                while s != '':
                    pos = s.find('###')
                    if pos == -1:
                        break
                    s1 = s[:pos]
                    if s1 == '':
                        break
                    print str(s1),pos
                    if s1 not in fm.termdict:
                        s = s[pos+3:]
                        continue
                    id = fm.termdict[s1]
                    sw = sw + str(id) + '#'
                    print id
                    s = s[pos+3:]
                    
                sw=sw+'\n'
            
            fout.write(sw)
            fp.close()
            fout.close()

def loadUrlfile(filename):
    fp = open(filename,'r')
    hashkeyToid = {}
    for each in fp:
        if each == '\n' :
            continue
        pos = each.find('#')
        hashkey = each[:pos]
        pos2 = each.find('#',pos+1)
        id = each[pos2+1:len(each)-1]
        hashkeyToid[hashkey] = int(id);
    return hashkeyToid
            
 
def creatInvert():
    filenames = os.listdir(fstd.rootpat+'file')
    os.chdir(fstd.rootpat+'file')
    docidTotermid = {}
    fhashkeyToid = loadUrlfile(fstd.rootpat+'url')
    print fhashkeyToid
    docid = 0
    ######################################################
    for filename in filenames:
        if filename.find('.term') != -1:
#            print filename
            fp = open(filename,'r')
#            hashkey = fhash.calcSha1(filename)
            hashkey = filename[:filename.find('.term')]
            if hashkey not in fhashkeyToid.keys():
                print hashkey ,'not in'
                docid = docid + 1
            else :
                docid = fhashkeyToid[hashkey]
            if docid not in docidTotermid:
                docidTotermid[docid] = []
            for each in fp:
                if each.find('\n') != -1:
                    s = each
                else :
                    s = each[:each.find('\n')]       
                
                while s != '': 
                    pos = s.find('#')
                    if pos == -1:
                        break
                    termid = s[:pos]
                    print docidTotermid[docid]
                    docidTotermid[docid].append(int(termid))
                    s = s[pos+1:]
            fp.close()

    print docidTotermid                
    #上面的代码是建立docid 到 termid 的映射                    
    ###################################################3
    termidTodocid = {}
    for docid in docidTotermid.keys():
        print "docid",docid
        for termid in docidTotermid[docid]:
            print termid
            if termid not in termidTodocid:
                termidTodocid[termid] = set()
            termidTodocid[termid].add(docid)
    
    fout = open(fstd.rootpat+'file/termid','w')
    for termids in termidTodocid.keys():
        s = str(termids)+'##'
        for termid in termidTodocid[termids]:
            s = s+str(termid) +'#'
        fout.write(s+'\n')
    fout.close()      
    ################################################   
            
    
if __name__ == '__main__':
#    print loadUrlfile(fstd.rootpat+'url')
    tidyTextfile()
#    s = '12'
#    print s.find('2')
#    print len(s)
#    print s[1+1:]
    creatInvert()
    print "done it"
    
    