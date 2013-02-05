# encoding:utf-8
import sys
import logging
import time
import fstd
def initLog():
    logger=logging.getLogger()
    handler=logging.FileHandler("Log_test.txt")
    logger.addHandler(handler)
    logger.setLevel(logging.NOTSET)
    

def writeLog(message):
    logger=logging.getLogger()
    filename = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    
    handler=logging.FileHandler(fstd.rootpat+"/log/"+filename+"error")
    logger.addHandler(handler)
    logger.setLevel(logging.NOTSET)
    logger.info(message)

def debug(message):
    logger=logging.getLogger()
    filename = time.strftime('%Y-%m-%d %H-%M',time.localtime(time.time()))
    
    handler=logging.FileHandler(fstd.rootpat+"/log/"+filename+"debug")
    logger.addHandler(handler)
    logger.setLevel(logging.NOTSET)
    logger.info(message)
        
    
if __name__ == '__main__':
    
    debug("hello")