import requests
import json
from music.models import Album

class PyLoad(object):
    def __init__(self, host, port, username, password):
        self.BASE_URL = "%s:%s/api" % (host, port)
        data = {
            'username': username,
            'password': password
        }
        self.session = requests.post(self.BASE_URL + '/login', data=data).content[1:-1]
    
    def download(self, name, tracks):
        response = dict()
        dl_response = requests.post(self.BASE_URL + '/addPackage', data = {
            'session': self.session,
            'name': json.dumps(name),
            'dest': 1,
            'links': json.dumps([track['url'] for track in tracks])
        })
        if dl_response.status_code == 200:
            album = Album.objects.get(title=name)
            album.pid = dl_response.content
            album.save()
            response['message'] = "Download Queued Successfully."
        else:
            response['message'] = response.content
        return response

    def get_download_status(self, pid):
        data = {
            'session': self.session,
            'pid': pid
        }
        return requests.post(self.BASE_URL + '/getPackageData', data=data)
