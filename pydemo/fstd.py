# encoding:utf-8

#设置一些参数 主要是一些路径 和一些常用函数

rootpath = '/home/fuxiang/python/fSearch-mini/pydemo/' # 程序运行的根目录
import re

def creatText(content,filename):
    text = ''
    while content != '':
        
        pos1 = content.find('<')
        if pos1 == -1:
            text = text + content
            break
        else:
            text = text + content[:pos1]
        pos2 = content.find('>',pos1+1)
        content = content[pos2+1:]
    text = text.replace(' ', '')
    fout = open(rootpath+'file/'+filename + '.text','w')
    fout.write(text)
    fout.close()
def filter_tags(htmlstr):
    #先过滤CDATA
    re_cdata=re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I) #匹配CDATA
    re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)#Script
    re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)#style
    re_br=re.compile('<br\s*?/?>')#处理换行
    re_h=re.compile('</?\w+[^>]*>')#HTML标签
    re_comment=re.compile('<!--[^>]*-->')#HTML注释
    s=re_cdata.sub('',htmlstr)#去掉CDATA
    s=re_script.sub('',s) #去掉SCRIPT
    s=re_style.sub('',s)#去掉style
    s=re_br.sub('\n',s)#将br转换为换行
    s=re_h.sub('',s) #去掉HTML 标签
    s=re_comment.sub('',s)#去掉HTML注释
    #去掉多余的空行
    blank_line=re.compile('\n+')
    s=blank_line.sub('\n',s)
    s=replaceCharEntity(s)#替换实体
    
    
##替换常用HTML字符实体.
#使用正常的字符替换HTML中特殊的字符实体.
#你可以添加新的实体字符到CHAR_ENTITIES中,处理更多HTML字符实体.
#@param htmlstr HTML字符串.
def replaceCharEntity(htmlstr):
    CHAR_ENTITIES={'nbsp':' ','160':' ',
                'lt':'<','60':'<',
                'gt':'>','62':'>',
                'amp':'&','38':'&',
                'quot':'"','34':'"',}
    
    re_charEntity=re.compile(r'&#?(?P<name>\w+);')
    sz=re_charEntity.search(htmlstr)
    while sz:
        entity=sz.group()#entity全称，如&gt;
        key=sz.group('name')#去除&;后entity,如&gt;为gt
        try:
            htmlstr=re_charEntity.sub(CHAR_ENTITIES[key],htmlstr,1)
            sz=re_charEntity.search(htmlstr)
        except KeyError:
            #以空串代替
            htmlstr=re_charEntity.sub('',htmlstr,1)
            sz=re_charEntity.search(htmlstr)
    return htmlstr

def repalce(s,re_exp,repl_string):
    return re_exp.sub(repl_string,s)

def changegbkToutf(filename):
    try :
        fp = open(filename)
        content = fp.read()
        gbk_content = content.decode('gbk')
        utf_content = gbk_content.encode('utf-8')
        fp.close()
        fout = open(filename,'w')
        fout.write(utf_content)
        fout.close()
        return utf_content
    except:
        return ""

if __name__ == "__main__":
#    import sys
    
    changegbkToutf('./data/fterms.dic')
