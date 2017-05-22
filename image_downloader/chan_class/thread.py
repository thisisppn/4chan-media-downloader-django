import urllib.request
from pathlib import Path

import requests

from image_downloader.chan_class.parser import FourchanParser


class FourchanThread(object):
    url = ''
    board = ''
    thread = ''
    thread_name = ''
    json_url = ''

    def __init__(self, thread_url):
        parser_response = FourchanParser.parse_fourchan_thread_url(thread_url)
        if parser_response:
            self.url = parser_response['url']
            self.board = parser_response['board']
            self.thread = parser_response['thread']
            self.json_url = self.url + ".json"

    def download_images(self):
        r = requests.get(self.json_url)
        response_json = r.json()
        posts = response_json['posts']
        for post in posts:
            if 'tim' in post:
                print('Processing ')
                print(post)
                post_obj = Post(post, self.board, self.thread)
                post_obj.download()


class Post(object):
    filename = ''
    ext = ''
    tim = ''
    cdn_url = ''
    board = ''
    thread = ''

    def __init__(self, post_json, board, thread):
        self.tim = post_json['tim']
        self.filename = post_json['filename']+post_json['ext']
        self.ext = post_json['ext']
        self.board = board
        self.thread = thread
        self.cdn_url = 'http://i.4cdn.org/' + self.board + '/' + str(self.tim) + self.ext

    def download(self):
        print('Downloading image ', self.filename)
        directory = "F:\\4chan-image-downloader\downloads\\"+self.board+"\\"+self.thread
        path = Path(directory)
        try:
            path.mkdir(parents=True, exist_ok=True)
            has_folder = True
        except Exception as e:
            print("Exception while creating folder %s", str(e))
            has_folder = False

        print(directory+"\\"+self.filename)

        if has_folder:
            try:
                urllib.request.urlretrieve(self.cdn_url, directory+"\\"+self.filename)
            except Exception as e:
                print('Unexpected exception %s', str(e))