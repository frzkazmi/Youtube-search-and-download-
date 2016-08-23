'''
Created on Aug 23, 2016

@author: laptop
'''
import urllib2
from bs4 import BeautifulSoup

from subprocess import call
url1="https://www.youtube.com/results?search_query="
base_url="https://www.youtube.com"
while True:
       
    query1=raw_input("Enter search query: ")
    query=query1.replace(" ", "+")
    url2=url1+query
    print "Search url: "
    print url2
    hdr = {'User-Agent': 'Mozilla/5.0'}
    urls=[]
    def parse(url):
           
        req = urllib2.Request(url,headers=hdr)
        homePage = urllib2.urlopen(req)
        homePageSoup = BeautifulSoup(homePage,'lxml')
        vid=homePageSoup.findAll(attrs={'class':'yt-lockup-title '})
        for i in range(len(vid)):
            try:
                print str(i)+" "+vid[i].a['title'].encode('utf-8')
                urls.append(base_url+vid[i].a['href'])
                
            except KeyError, e:
				pass    
        index=int(raw_input("Enter the video index : "))
        command1 = "youtube-dl" +" -F"+" "+urls[index]
        print "Getting all available qualities for this video"
        print command1     
        call(command1.split())
        code = int(raw_input("Select the desired video quality by specifying the exact format code "))
        command2 = "youtube-dl" +" -f"+" "+str(code)+" "+urls[index]
        print "Downloading..."
        print command2
        call(command2.split())
    
    def Again():
          
        print 'Do you want to search again? (yes or no)'
        return raw_input().lower().startswith('y')    
    
    parse(url2)
    urls=[]
    if not Again():
        break    
