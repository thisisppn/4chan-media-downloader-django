from urllib.parse import urlparse


class FourchanParser(object):
    @staticmethod
    def parse_fourchan_thread_url(url):
        url_obj = urlparse(url)
        if url_obj:
            if url_obj[0] in ['http', 'https']:
                base_url = url_obj[1]
                path = url_obj[2]
                path = path.split('/')

                board = path[1]
                type = path[2]
                thread_id = path[3]

                if type != 'thread':
                    raise Exception('Invalid thread url.')
                __response = {
                    'board': board,
                    'thread': thread_id,
                    'url': url
                }
                return __response
            else:
                raise Exception("Invalid url, enter full valid url including http.")
        else:
            return False