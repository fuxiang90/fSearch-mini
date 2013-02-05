#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import cgi
import sys
import pprint  
import MySQLdb
import fquery
import datetime

def lookup(word):
    
   
    f = fquery.fquery()
    content = f.query(word)
#    print content
    return content
try:
    
    print "Content-Type: text/html charset=utf-8"     # HTML is following
    print                               # blank line, end of headers
    print

    reshtml = '''
    <br>
    link:<a href="%s" target="_blank" >%s </a><br>
    Content: <p> %s </p> <br>
    ---------------分割线----------------------------
    ''' 

    print '''<html><head><title>Test CGI Python</title><meta http-equiv="Content-Type" content="text/html;charset=utf-8" /></head><body>'''
    print "<p> 如有建议或想法，联系 fuxiang90@gmail.com </p>"

    
    form = cgi.FieldStorage()
    code = form['query'].value
   
#    code = 'linux' 
#    print code
#    fp = open('file/termid')
    starttime = datetime.datetime.now()
    content = lookup(code)
    endtime = datetime.datetime.now()
#    content = fp.read()
#    print content

    print "检索所用时间 ：" + str( (endtime-starttime).seconds) + "s <br>"
    if len(content) == 0:
        print "抱歉，没有结果，换个关键词，比如 征友"
    for item in content[:10]:
        print reshtml % (str(item[1]),str(item[1]) ,str(item[0] )[:400])
        
    
    print "</body></html>"

except Exception, e:
    print >> sys.stderr, "Exception: %s" % str(e)
    sys.exit(1)
 
