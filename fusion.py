from BeautifulSoup import BeautifulSoup
import os
import re
import popen2
def reconstruct():
    homedir = os.getcwd()
    #tmp= homedir +  "/cache/result.html"
    #print "--------------" + tmp
    soup = BeautifulSoup(open(homedir +  "/cache/youdao.html"))
    head = BeautifulSoup(open(homedir +  "/cache/construction/head.html"))
    bodystart = BeautifulSoup(open(homedir +  "/cache/construction/body-start.txt"))
    bodyend = BeautifulSoup(open(homedir +  "/cache/construction/body-end.txt"))
    result = soup.body.extract()
    sousuo = soup.find('form',{"id":"f"})
    #sousuo  = str(sousuo).replace("action=\"/search\"","action=\"http://dict.youdao.com/search\"")
    #result  = str(result).replace("href=\"/example/","href=\"http://dict.youdao.com/example/")
    os.system("echo "" > cache/result.html")
    file=open('cache/result.html','w')
    print >>file,"<html>"
    print >>file,head
    print >>file,bodystart
    #print >>file,result
    print >>file,bodyend
    print >>file,"</html>"
    file.close()
    #sed -i 's/text/111/g' test 
    #sed -e "s:':kd:g" iii  
    #action="/search"  ------------action="http://dict.youdao.com/search"
    #href="/example/"-----href="http://dict.youdao.com/example/"
    #result  = str(result).replace("href=\"/example/","href=\"http://dict.youdao.com/example/")
    #os.system("sed -i -e 's/action=\"\/search/action=\"http:\/\/dict.youdao.com\/search/g' cache/result.html")
    #os.system("sed -i -e 's/href=\"\/example/href=\"http:\/\/dict.youdao.com\/example/g' cache/result.html")
    #os.system("sed -i -e 's/<\/div><\/div><\/div>/ /g' cache/result.html")
