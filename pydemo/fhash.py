# encoding:utf-8
import hashlib
import os,sys
 
def calcSha1(str):
    
    sha1obj = hashlib.sha1()
    sha1obj.update(str)
    hash = sha1obj.hexdigest()
    print(hash)
    return hash



class fUrl(object):
    def __init__(self):
        
        self.addUrl = {}
        self.doccount = 1
        self.newdoccount = 0 
        self.urlhash = self.readUrl()
    def readUrl(self):
        fp = open('/home/fuxiang/python/fSearch-mini/pydemo/url','a+')
        a = {}
        for each in fp:
            urlhash = each[0:each.find('#')]
            url = each[each.find('#')+1:]
            a[urlhash] = url
            self.doccount = self.doccount + 1
        fp.close()
        return a
    def lookup(self,url):
        hashkey = calcSha1(url)
        if hashkey in self.urlhash:
            return False
        else :
            if hashkey in self.addUrl:
                return False
            else:
                self.addUrl[hashkey] = url
                return True
        
    def writeBack(self):
        fp = open('/home/fuxiang/python/fSearch-mini/pydemo/url','a')
        count =  self.doccount
        for each in self.addUrl.keys():
            fp.write(each+'#'+self.addUrl[each]+'#'+str(count)+'\n')
            count = count +1 
            
        fp.close()
            
        
            
    
if __name__ == '__main__':
    calcSha1('http://www.bupt.edu.cn')
    furl = fUrl()
    print furl.urlhash