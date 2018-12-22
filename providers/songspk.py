from utils.parser import Parser

class SongsPK(object):
    def __init__(self):
        self.BASE_URL = "https://songspk.shop"
        self.SEARCH_ALBUM_URL = self.BASE_URL + "/search?type=albums&q="
        self.parser = Parser()

    def search_for_albums(self, q):
        return self.parser.parse_data(self.SEARCH_ALBUM_URL + q, {
            'items': [
                {
                    'name': 'albums',
                    'has_children': True,
                    'child_selector': {
                        'type': 'tag',
                        'value': 'figure'
                    },
                    'type': 'selector',
                    'value': 'body > section > main > content > div.archive-body > div.col-body'
                }
            ],
            'keys': {
                'albums': {
                    'image': {
                        'selector': 'div.thumb-image > a > img',
                        'attr': 'src',
                        'prefix': self.BASE_URL,
                        'type': 'selector'
                    },
                    'title': {
                        'selector': 'figcaption > h3 > a',
                        'attr': 'text',
                        'type': 'selector'
                    },
                    'url': {
                        'selector': 'figcaption > h3 > a',
                        'attr': 'href',
                        'prefix': self.BASE_URL,
                        'type': 'selector'
                    },
                }
            }
        })

    def fetch_album_details(self, url):
        return self.parser.parse_data(url, {
            'items': [
                {
                    'name': 'tracks',
                    'has_children': True,
                    'child_selector': {
                        'type': 'tag',
                        'value': 'li'
                    },
                    'type': 'selector',
                    'value': '.page-tracklist-body > ul'
                },
                {
                    'name': 'title',
                    'has_children': False,
                    'type': 'selector',
                    'selector': 'body > section > main > content > div.page-meta-wrapper > div > div.col-md-9.page-meta > ul > li:nth-of-type(1) > div.col-md-9.col-xs-6.text-left',
                    'attr': 'text'
                },
                {
                    'name': 'url',
                    'has_children': False,
                    'type': 'finder',
                    'selector': {
                        'tag': 'link',
                        'extra': {
                            'rel': 'canonical'
                        }
                    },
                    'attr': 'href',
                },
                {
                    'name': 'image',
                    'has_children': False,
                    'type': 'selector',
                    'selector': 'body > section > main > content > div.page-meta-wrapper > div > div.col-md-3.page-cover > img',
                    'attr': 'src',
                    'prefix': self.BASE_URL
                }
            ],
            'keys': {
                'tracks': {
                    'title': {
                        'selector': 'div.col-md-7.col-xs-10.col-text > h3 > a',
                        'attr': 'text',
                        'type': 'selector'
                    },
                    'url': {
                        'selector': 'div.col-md-4.col-xs-5.col-download > a',
                        'attr': 'href',
                        'type': 'selector'
                    }
                }
            }
        })
