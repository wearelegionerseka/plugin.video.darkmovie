#!/usr/bin/python

from requests import get, head
#from bs4 import BeautifulSoup
from scrapers.utils import headers
from hosts.exceptions.exceptions import VideoNotAvalaible
import sys
PY3 = sys.version_info[0] == 3

import logging
def logga(mess):
    
    logging.warning('streamtape.py: '+mess)

    
class Metadata:
    def __init__(self):
        self.logo = "https://streamtape.com/images/Logo@2x.png"
        self.icon = "https://streamtape.com/favicon.ico"

def get_mp4(url):
    headerss = head(url)
    mp4 = headerss.headers['Location']
    return mp4

def get_video(url, referer):
    referer = ""
    headers['Referer'] = referer
    body = get(url, headers = headers).text
    
   
    #logga(f'URL-->{url} \n referer-->{referer}')
    #logga(f' body--->{body}')
    
    video_url=""   
    
  
    try:
        link1=body.split("innerHTML = ")[1]
        link2=link1.split("('")[1]
        link3=link2.split("')")[0]
        link4=link3.split("=")
        link5=link4[1]+"="+link4[2]+"="+link4[3]+"="+link4[4]
        '''
        logga('Sono dentro TRY')
        logga(f'\n link 1° innerHTML split-->{link1}') 
        logga(f'\n link 2° split-->{link2}')
        logga(f'\n link 3°-->{link3}')
        logga(f'\n link 4°-->{link4}')
        logga(f'\n link 5°-->{link5}') 
        '''
        video_link="//streamta.pe/get_video?id="+link5
        
        logga(f' video_link-->https:{video_link}')
    except IndexError:
            logga('Sono in def get_video, esco con errore sul primo spilt innerHTML')
            raise VideoNotAvalaible(url)
    
    video_url = get_mp4("https:%s" % video_link)
    logga(f'Video URL-->{video_url}')
    return video_url

