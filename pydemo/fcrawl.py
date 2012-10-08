# encoding:utf-8
# 部分代码来源http://www.udacity.com/ 公开课
"""
功能：爬取网页，并抽取里面的正文，做一定的处理
结果：text 文件
"""
import sys
import re
import socket
import time
import os
import fhash
import fstd
import copy
socket.setdefaulttimeout(8) 


import urllib2

count = 1
def store_page(content,url):
#    print url
    urlhash = fhash.calcSha1(url);
    print urlhash
    
    fwrite = open (str(urlhash),'w')
    fwrite.write(content)
    fwrite.close()
    
    t = copy.deepcopy(content)
    print t[:30]
    fstd.creatText(t, str(urlhash))
#    t = content
#    text = fstd.filter_tags(t)
#    print text
#    fp = open(str(urlhash) + '.text','w')
#    fp.write(text)
#    fp.close()
def get_page(url):
    try :
        page = urllib2.urlopen(url)
        content = page.read()
        store_page(content, url)
        return content
    except :
        return ""
#    except urllib2.HTTPError as http_error:
#        print http_error
#        return ""

       
def get_url(page):
    
    end_pos = 0
    while end_pos <= len(page) -1:
        start_link = page.find('<a href=')
        start_pos = page.find('"',start_link)
        end_pos = page.find('"',start_pos+1)
        url = page[start_pos+1:end_pos]
        
        # print end_pos , len(page) -1
        if url == '':
            break
        page = page[end_pos:]

def lookup(index,keyword):
    for i in index:
        if i[0] == keyword:
            return i[1]
    return []

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):

    links= []
    end_pos = 0
    while end_pos <= len(page) -1:
#        start_link = page.find('<a href=')
        start_link = page.find('href=')
        start_pos = page.find('"',start_link)
        end_pos = page.find('"',start_pos+1)
        url = page[start_pos+1:end_pos]
        
        # print end_pos , len(page) -1
        if url :
            links.append(url)
        else:
            break
        page = page[end_pos:]
     
    print links
    return links

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    keywords = content.split()
    for keyword in keywords:
        add_to_index(index,keyword,url)

def crawl_web(seed,max_depth):
    tocrawl = [seed]
    print tocrawl
#    crawled = []
    fcrawled = fhash.fUrl()
    next_deep = []
    deep = 0
    index = []
    while tocrawl and deep <= max_depth:
        url = tocrawl.pop()
#        print url
        
#        if url not in crawled:
        if fcrawled.lookup(url) == True:
            print url
            content = get_page(url)
#            print url
            if content == '':
                print "content is none"
            print content[0:100]
            temp = get_all_links(content)
            
            union(next_deep, temp)
        if len(tocrawl) == 0:
                print "None\n"
                tocrawl = next_deep
                next_deep = []
#                tocrawl,next_deep = next_deep,[]
                deep = deep + 1
                print tocrawl
    fcrawled.writeBack()
    return fcrawled.addUrl
    
def test():
    url = 'http://grs.bupt.edu.cn/'
    import urllib2
    page = urllib2.urlopen(url)
    content = page.read()
#        print content
    store_page(content, url)
    print content
        
if __name__ == "__main__":

    os.chdir(fstd.rootpat + "file")
##    print get_all_links( get_page("http://www.bupt.edu.cn") )
    crawl_web("http://127.0.0.1/webfile/index.html",3)
#    s = ["2" ,"3"]www.bupt.edu.cn

#    test()
#    print s.pop()
#    print s
#    
#    urls = [ 'http://sice.bupt.edu.cn', 'http://see.bupt.edu.cn', 'http://scs.bupt.edu.cn', 'http://sa.bupt.edu.cn', 'http://sse.bupt.edu.cn', 'http://sem.bupt.edu.cn', 'http://sh.bupt.edu.cn', 'http://sci.bupt.edu.cn', 'http://www.is.bupt.cn', 'http://www.buptnu.com.cn', 'http://www.bupttc.com', 'http://seme.bupt.edu.cn']
#    for url in urls:
#        print get_page(url)[0:30]
        
    
