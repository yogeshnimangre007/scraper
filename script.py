# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:53:29 2018

@author: OptimusPrime
"""
#import statements
import lxml.html
import requests
from lxml.cssselect import CSSSelector
#website to download paper
url="http://jobwik.com/page/free-epaper-the-hindu/"
#request
r = requests.get(url)
#changing a html text into dom tree 
tree=lxml.html.fromstring(r.text)
#cssselctor and aplying it to tree
sel=CSSSelector('article>div:first-child a[class^=\'color-\']')
matchedlinks=sel(tree)
#converting tree back to html format
matchedlinks_html=[lxml.html.tostring(item) for item in matchedlinks]
second_url=matchedlinks[0].get('href')
#url of page to which we will be redirected when our date is choosed
print(second_url)
#same stuff
r_second=requests.get(second_url)
tree_second=lxml.html.fromstring(r_second.text)
sel_second=CSSSelector('h4>a')
matchedlinks_second=sel_second(tree_second)
drive_link=matchedlinks_second[0].get('href')
#link of google drive 
print(drive_link)
#extractting id
file_id = drive_link[(drive_link.index("=")+1):]
#funtion to download file 
def download_file_from_google_drive(id):

    GDRIVE_DOWNLOAD_LINK = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(GDRIVE_DOWNLOAD_LINK, params={
                           'id': id}, stream=True)
    token = get_confirm_token(response)
    print("Hey Google Drive could you please take the File ID and give me file!! ...")
    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(GDRIVE_DOWNLOAD_LINK,
                               params=params, stream=True)

    save_response_content(response)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def save_response_content(response):
    import platform
    if platform.system() == 'Windows':
        DESTINATION_FILE_NAME = 'C:\\Users\\OptimusPrime\\Desktop\\papers\\paper_hindu-'
    else:
        DESTINATION_FILE_NAME = 'paper_'

    DESTINATION_FILE_NAME = DESTINATION_FILE_NAME + \
        str(datetime.datetime.today().strftime('%d-%m-%Y')) + '.pdf'
    CHUNK_SIZE = 32768

    with open(DESTINATION_FILE_NAME, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    print("Thanks Google Drive for the File.")
    print("Hey got the file ^_^ and I saved as",
          DESTINATION_FILE_NAME, "\n")
    


if __name__ == "__main__":
    import datetime
    print("Usage: Just run it with 'PYTHON' you will get pdf in 'Linux:current directory' and in 'Windows:C Drive'\nas 'paper_dd-mm-yy.pdf'\n")

    URL_TO_SCRAPE = "http://jobwik.com/page/free-epaper-the-hindu/"

    # DESTINATION_FILE_NAME is subjected to change according to user needs!
    download_file_from_google_drive(file_id)
#thank you :-)