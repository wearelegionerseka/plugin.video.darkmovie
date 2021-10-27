#!/usr/bin/python

from requests import get
from bs4 import BeautifulSoup
from scrapers.utils import get_piece, headers
from hosts.exceptions.exceptions import VideoNotAvalaible

import re
import logging
def logga(mess):
    
    logging.warning('mixdrop.py: '+mess)


class Metadata:
    def __init__(self):
        self.logo = "https://mixdrop.co/imgs/mixdrop-logo2.png"
        self.icon = "https://mixdrop.co/favicon.ico"

def get_emb(url):
    url = url.replace("/f/", "/e/")
    url = url.replace("mixdrops", "mixdrop")
    url = url.replace(".icu", ".co")

    if url[-1] == "/":
        url = url[:-1]

    return url

def right_path(body):
    if body[:8] == "<script>":
        path = (
            body
            .split("= \"")[1]
            .split("\"")[0]
        )

        url = "https://mixdrop.co%s" % path
        body = get(url, headers = headers).text

    return body

def get_video(url, referer):
    try:
        url = get_emb(url)
        logga(f'sono in get_video  url che arriva-->{url}')
        headers['Referer'] = ""
        body = get(url, headers = headers).text
        logga(f'body 1-->{body}')
        if "This embed is domain protected." in body:
            headers['Referer'] = referer
            body = get(url, headers = headers).text
            logga(f'body 2-->{body}')
        body = right_path(body)
        logga(f'body ultimo-->{body}')
        pieces = BeautifulSoup(body, "html.parser").find_all("script")
        logga(f'sono in get_video pieces-->{pieces}')
        piece = get_piece(pieces)
        logga(f'sono in get_video piece-->{piece}')
        splitted = [""]
        splitted += piece.split("|")[3:]
        excapes = ["a", "e", "s"]

        indexs = (
            piece
            .split("//")[2]
            .split("\";")[0]
        )

        video_url = "https://"

        for a in indexs:
            if (
                a.isalpha() or a.isdigit()
            ) and (
                not a in excapes
            ):
                index = int(a, 36)
                video_url += splitted[index]
            else:
                video_url += a
        logga(f'video_url-->{video_url}')
        return video_url
    except (IndexError, UnboundLocalError) as a:
        raise VideoNotAvalaible(url)