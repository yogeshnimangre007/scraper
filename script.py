# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:53:29 2018

@author: OptimusPrime
"""
import lxml.html
import requests
from lxml.cssselect import CSSSelector
url="http://jobwik.com/page/free-epaper-the-hindu/"
r = requests.get(url)
#responce_initial=r.text
#print(r.text)
tree=lxml.html.fromstring(r.text)
#print(lxml.html.tostring(tree))
sel=CSSSelector('article>div:first-child a[class^=\'color-\']')
matchedlinks=sel(tree)
#print(matchedlinks)
matchedlinks_html=[lxml.html.tostring(item) for item in matchedlinks]
#print("total matched objects",len(matchedlinks_html))
for i in range(0,len(matchedlinks_html)):
    #print(matchedlinks_html[i])
    #print(matchedlinks[i].get('href'))
    second_url=matchedlinks[i].get('href')#this print href value
    #print(matchedlinks[i].text) #this print the text 
#second page selection
print(second_url)
r_second=requests.get(second_url)
tree_second=lxml.html.fromstring(r_second.text)
sel_second=CSSSelector('h4>a')
matchedlinks_second=sel_second(tree_second)
drive_link=matchedlinks_second[0].get('href')
print(drive_link)
#to do _____download css selctor and get get_reqest voice..
#div:nth-child(4) div[data-tooltip="Add a comment"]>div[class] this is selecter for download
#drive code

def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL=drive_link

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    


if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 3:
        print ("Usage: python google_drive.py drive_file_id destination_file_path")
    else:
        # TAKE ID FROM SHAREABLE LINK
        file_id = sys.argv[1]
        # DESTINATION FILE ON YOUR DISK
        destination = sys.argv[2]
        download_file_from_google_drive(file_id, destination)