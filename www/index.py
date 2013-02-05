#! /usr/bin/env python

import sys
sys.path.append('/home/fuxiang/python/crawl-linux')
#import MysqlProcess     # this a wrong code 
import MySQLdb


"""
bbsindex -->
    id ,title ,link ,author ,content ,score ,b1 ; b1 
"""


try:

    print "Content-Type: text/html charset=utf-8"     # HTML is following
    print                               # blank line, end of headers


    reshtml = '''

    <H3>title: <I>%s</I></H3>
    link:<a href="%s">%s </a><br>
    author: %s -- date :%s <br> 
    <p>   %s  </p><br> <br>''' 

    print '''<html><head><title>Test CGI Python</title><meta http-equiv="Content-Type" content="text/html;charset=utf-8" /></head><body>'''
    
    conn =  conn_bbsindex()
    
    cur = conn.cursor()
    
    sql = "select id,title,link,author,date,content  from bbsindex   order by date desc  limit 0,50"#q ,id desc limit 0,50"
    cur.execute(sql)
    all = cur.fetchall()
    for m in all:
        # print str(m[1]) ,str(m[2]),str(m[4]),str(m[5]))
        print reshtml % (str(m[1]) ,str(m[2]),str(m[2]),str(m[3]),str(m[4]),str(m[5])[0:400])
#        print reshtml % (m[1].encode('utf-8') ,m[2].encode('utf-8'),m[3].encode('utf-8'),m[4].encode('utf-8'))

    print "</body></html>"

except Exception, e:
    print >> sys.stderr, "Exception: %s" % str(e)
    sys.exit(1)








#print "<html><header><title>Test CGI Python</title></header><body>Hello CGI!</body></html>"
