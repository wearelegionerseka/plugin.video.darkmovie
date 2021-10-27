#!/usr/bin/python

from requests import get
from bs4 import BeautifulSoup
from scrapers.utils import get_piece, headers
from hosts.exceptions.exceptions import VideoNotAvalaible

import logging
def logga(mess):
    #if debug == 'on':
    logging.warning('vup.py: '+mess)

class Metadata:
    def __init__(self):
        self.logo = "https://cdn.vup.to/apple-touch-icon.png"
        self.icon = "https://cdn.vup.to/favicon-16x16.png"

    
        
def get_video(url, referer):
    headers['Referer'] = referer
    body = get(url, headers = headers).text
    logga(f'URL-->{url} \n referer-->{referer}')
    logga(f' body--->{body}')
    video_url=""
    '''
    try:
        video_url1 = body.split("sources: [{")[1]   
        logga(f'1 split-->{video_url1}')
        video_url2=video_url1.split("\"")[1]
        logga(f'2 split-->{video_url2}')
        video_url=video_url2.split("\"")[1]
        logga(f'3 split   video_url-->{video_url}')
    except IndexError:
            logga('Sono in def get_video, esco con errore sul primo split')
            raise VideoNotAvalaible(url)
    return video_url

    '''
    
    pieces = BeautifulSoup(body, "html.parser").find_all("script")

    try:
        piece = get_piece(pieces)
    except UnboundLocalError:
        raise VideoNotAvalaible(url)

    splitted = [""]
    splitted += piece.split("|")[1:]

    indexs = (
        piece
        .split("//")[2]
        .split("\"")[0]
    )

    s_indexs = indexs.split("/")
    video_url = "https://"

    for a in range(
        len(s_indexs)
    ):
        if a == 0:
            for b in s_indexs[a].split("."):
                index = int(b, 36)
                video_url += "%s." % splitted[index]

            video_url = video_url[:-1]

        elif a == 1:
            index = int(s_indexs[a], 36)
            video_url += splitted[index]

        elif a == 2:
            things = s_indexs[a].split(",")

            for b in things:
                if b == "":
                    video_url += ","
                    continue

                elif b[0] == ".":
                    video_url += "."
                    b = b[1:]

                index = int(b, 36)
                video_url += splitted[index]

                if b != things[-1][1:]:
                    video_url += ","

        elif a == 3:
            things = s_indexs[a].split(".")

            for b in things:
                index = int(b, 36)
                video_url += splitted[index]

                if b != things[-1]:
                    video_url += "."

        video_url += "/"

    return video_url[:-1]
  