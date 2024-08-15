#IMPORTANT
#REQUIRES EugenesFunctions to run
#Code for this is in file titled "Webscraping"
#
import requests
from bs4 import BeautifulSoup as bs
import regex as re
from EugenesFunctions import eugURL as ul
#this is a file that needs to be imported. The file name is defaulted to EugenesFunctions, but if you download and copy the code under "EugenesFunctions"
#in this rep, and name the file that the class is on "EugenesFunctions", it will work. You can also change the name of the file and import that name instead.
from io import BytesIO
import urllib.request
from time import sleep

def showImage(URL):#shows image given URL
    urllib.request.urlretrieve(URL, "sample_photo.jpg")#finds data from URL and stores it to new file called "sample_photo.jpg"
    sleep(0.08)#wikipedia recommends delay of 100ms between requests, so I oblige.
    img = Image.open("sample_photo.jpg")#opens the file which is already formatted as a jpg
    img.show()#shows the image (on mac, opens preview)
    
def searchWikipedia(query):#given any query, returns URL of photos 
    URL = "".join(["https://en.wikipedia.org/wiki/",str(query)])
    page = requests.get(URL)
    soup = bs(page.content, "html.parser")
    contents = soup.findAll("a")#finds all places where tag = "a"
    linksList = []
    URLlist = []
    #testFile = open("images.txt", "r+")#testFile used to see and check links, URLs, or anything necessary
    #testFile.truncate(0)
    for content in contents:
        link = content.get("href")#finds all text assocaited with "href"
        if link != None:#filters out any times content contains no "href"
            linksList.append(link)
            #testFile.write(link)
            #testFile.write("\n")
    finalList = []
    
    for x, link in enumerate(linksList):
        raw = ul(link)#converts link to ul object
        if raw.check("jpg") == True:#checks if the link's suffix is jpg
            finalList.append(link)
            #print(link, "\n\n")#making sure there are some links that end with jpg
    for link in finalList:
        URL = "https://en.wikipedia.org/" + str(link)#creating the URL for the site where image is displayed
        URLlist.append(URL)
        
    for i, URL in enumerate(URLlist):
        page = requests.get(URL)
        sleep(0.08)
        soup = bs(page.content, "html.parser")#searches site with image for the image file
        content = soup.find(class_ = "fullMedia")
        if content != None:#filter
            links = content.findAll("a")
        for link in links:
            if link != None:#more filter
                URL = link.get("href")
                URLlist[i] = URL
    for URL in URLlist:
        link = URL = "https:" + str(URL)#creates final link that is directly linked to the picture
        showImage(link)
#======================================= Main =======================================

query = str(input("What are you searching (_ for spaces)?" ))
searchWikipedia(query)
