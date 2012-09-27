# encoding:utf-8
import urllib2
import time
import socket


def test1():
    import httplib
    conn = httplib.HTTPConnection("www.g.com", 80, False)
    conn.request('get', '/', headers = {"Host": "www.google.com",
                                    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",
                                    "Accept": "text/plain"})
    res = conn.getresponse()
    print 'version:', res.version
    print 'reason:', res.reason
    print 'status:', res.status
    print 'msg:', res.msg
    print 'headers:', res.getheaders()
#html
#print '\n' + '-' * 50 + '\n'
#print res.read()
    conn.close()
    
def test2():
    #!/usr/local/bin/python
# -*- coding: utf-8 -*-

    import urllib2
    import zlib

    headers = { "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6",}
    try:
        req = urllib2.Request("http://www.fuxiang90.com/2012/09/python-%E5%86%99%E6%97%A5%E5%BF%97/", headers = headers)
        res = urllib2.urlopen(req)
        print res.read()
    except urllib2.HTTPError as http_error:
        print zlib.decompress(http_error.read(), 30)
    
if __name__ == '__main__':
    test2()