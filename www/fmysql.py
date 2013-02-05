# encoding:utf-8
import sys
import MySQLdb
import random


import time

class MysqlProcess(object):
    def __init__ (self):
#        self.conn = self.connConnect()
        self.conn = None
    def connConnect(self,dbstr = "indexdb",hoststr = "localhost",userstr = "osqa",passwdstr = "osqa"):
#        conn = MySQLdb.connect(host = str(hoststr),user = str(userstr),passwd = str(passwdstr) ,db = str(dbstr), charset='utf8')
        conn = MySQLdb.connect(host = 'localhost',user = 'osqa',passwd = 'osqa' ,db = 'indexdb', charset='utf8')
        return conn


    def getAll(self):
        self.conn = self.connConnect()
        cur = self.conn.cursor()
        cur.execute('select id,text from bbsindex')
        all = cur.fetchall()
        index = []
        for i in all :
            t = []
            t.append(i[0])
            t.append(i[1])
            index.append(t)
    
        cur.close()
        self.conn.close()
        return index
    
    
if __name__ == "__main__":
#    index = [ ['test2','test','test','test']]
    index = [ ['test45','test222','test','test']]
    db = MysqlProcess()
    db.insertBbsDb(index)
    
    print "done it"
        
    
