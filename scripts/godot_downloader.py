#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from zipfile import ZipFile
import os
import shutil
import sys


def find_latest_godot_url(os, version, mono_version):

    result = requests.get("https://godotengine.org/download/"+os)

    if result.status_code == 200:

        src = result.content
        soup = BeautifulSoup(src, 'html.parser')

        divs = soup.find_all("div", class_="btn split download")

        for div in divs:
            for anchor in div.find_all('a'):
                if anchor.has_attr('href'):
                    
                    link = str(anchor['href'])

                    if link.find(version) != -1:
                        if mono_version :
                            if link.find("mono") != -1 :
                                return link 
                        elif link.find("mono") == -1 :
                            return link
        
        print("link not found")

    else :
        print("Request not received")

    return ""

#this has been copy and pasted + modified from https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests
def download(url, filename):
    request = requests.get(url, stream=True)
    total_size = int(request.headers.get('content-length', 0))
    block_size = 1024 #1 Kibibyte
    t=tqdm(total=total_size, unit='iB', unit_scale=True)
    with open(filename, 'wb') as f:
        for data in request.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()
    if total_size != 0 and t.n != total_size:
        print("ERROR, something went wrong")


def extractZip(filename):
    with ZipFile(filename, 'r') as zipObj:
        # Extract all the contents of zip file in current directory
        zipObj.extractall()

def str2bool(v):
   return str(v).lower() in ("yes", "true", "t", "1", "vrai", "v", "y")


def main():

    os = str(sys.argv[1])
    version = str(sys.argv[2])
    mono_version = str2bool(str(sys.argv[3]))
    downloaded_filename = str(sys.argv[4])

    #Finds the link
    link = str(find_latest_godot_url(os, version, mono_version))
    print("Downloading Godot from " + link)
    #Downloads the zip from the url with the corresponding filename
    download(link, downloaded_filename)

    #Extracts the zip
    extractZip(downloaded_filename)


if(__name__ == "__main__"):
    main()