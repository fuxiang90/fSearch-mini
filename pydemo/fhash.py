# encoding:utf-8
import hashlib
import os,sys
 
def calcSha1(str):
    
    sha1obj = hashlib.sha1()
    sha1obj.update(str)
    hash = sha1obj.hexdigest()
    print(hash)
    return hash


if __name__ == '__main__':
    calcSha1('http://seme.bupt.edu.cn')