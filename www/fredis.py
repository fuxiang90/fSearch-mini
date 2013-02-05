# encoding:utf-8


import fstd
import fmysql
import redis

class fredis():
    
    def __init__(self):
        self.r = redis.Redis(host='127.0.0.1', port=6379, db=0) 
        
#        if self.r.get()
        pass
    
    def setRedis(self):
        fm = fmysql.MysqlProcess()
        items = fm.getAll()
        for item in items :
            self.r.set(str(item[0]) ,item[1])
    def isOnlie(self):
        if self.r.set("foo", "bar") == True:
            return True
        return False
    def getRedis(self,str):
        return self.r.get(str)


def main():
    test = fredis()
#    test.setRedis()
    print test.getRedis("10333") 
if __name__ == '__main__':
    main()
    
    print "done it"
    


    
    

