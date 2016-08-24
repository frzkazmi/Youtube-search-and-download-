'''
Created on Aug 23, 2016

@author: laptop
'''
import urllib2, socket, requests
from bs4 import BeautifulSoup

from subprocess import call
url1="https://www.youtube.com/results?search_query="
base_url="https://www.youtube.com"
url_page2="https://www.youtube.com/results?sp=SBTqAwA%253D&q="
while True:
       
    query1=raw_input("Enter search query: ")
    query=query1.replace(" ", "+")
    url_page1=url1+query
    print "Search url: "
    print url_page1
    hdr = {'User-Agent': 'Mozilla/5.0'}
    urls=[]
    def parse(url):
           
        #req = urllib2.Request(url,headers=hdr)
        req = requests.get(url)
        timeout = 10
        socket.setdefaulttimeout(timeout)
        #homePage = urllib2.urlopen(req)
        #homePageSoup = BeautifulSoup(homePage,'lxml')
        homePageSoup = BeautifulSoup(req.content,'html.parser')
        vid=homePageSoup.findAll(attrs={'class':'yt-lockup-title '})
        print "Search Results"
        print "------------------------------------------"
        for i in range(len(vid)):
            try:
                
                print str(i)+" "+vid[i].a['title'].encode('utf-8')
                
                urls.append(base_url+vid[i].a['href'])
                
            except KeyError, e:
                pass  
        print "------------------------------------------" 
             
        
    def download():
        index=int(raw_input("Enter the video index : "))
        ch=int(raw_input("Enter 1 for video and 2. for audio "))
        if ch==1:
                    
            command1 = "youtube-dl" +" -F"+" "+urls[index]
            print "Getting all available qualities for this video"
            print command1     
            call(command1.split())
            code = int(raw_input("Select the desired video quality by specifying the exact format code "))
            command2 = "youtube-dl" +" -f"+" "+str(code)+" "+urls[index]
            print "Downloading..."
            print command2
            call(command2.split())
        elif ch==2:
            call(['youtube-dl',"-x","--extract-audio","--audio-format","mp3",urls[index]])
        else:
            print "Wrong choice"             
        
    def Again():
          
        print 'Do you want to search again? (yes or no)'
        return raw_input().lower().startswith('y')    
    
    parse(url_page1)
    choice=raw_input("Enter s to skip and move to next 20 results else enter any other thing to download any of these results ")
    if choice == 's':
        urls=[]
        url3=url_page2+query
	parse(url3)
	download()
	urls=[]
    else:
        download()
        urls=[]
        		
		
		
    
    if not Again():
        
        break    
    
