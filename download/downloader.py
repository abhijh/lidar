import re
import requests
import os
import time
# from pySmartDL import SmartDL

class Downloader(object):
    def __init__(self, BASE_DOWNLOAD_DIR):
        self.BASE_DOWNLOAD_DIR = BASE_DOWNLOAD_DIR

    def download_album(self, album_name, track_list):
        # for track in track_list:
            # self.download_single_track(track.track_name, album_name, self.)
        pass

    def download_single_track(self, track_name, album_name, url, task=None):
        for i in range(20):
            task.update_state(state='PROGRESS',
                meta={'process_percent':i*5})
            time.sleep(1)
        # base_name = self.BASE_DOWNLOAD_DIR + '/' + album_name + '/'
        # file_name_from_cd = self.get_file_name_from_cd(url)
        # if file_name_from_cd:
        #     file_name = base_name + file_name_from_cd
        # else:
        #     file_name = base_name + track_name + '.mp3'
        
        # self.download(url, file_name)

    def download(self, url, file_name, task):
        self.create_dirs(file_name)
        with open(file_name, "wb") as f:
            print("Downloading %s" % file_name)
            response = requests.get(url, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None: # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)

    # def downloads(self, url, file_name, task):
    #     smartDL = SmartDL(url, file_name)
    #     smartDL.start()
    #     while(!smartDL.isFinished()):


    def create_dirs(self, file_name):
        if not os.path.exists(os.path.dirname(file_name)):
            try:
                os.makedirs(os.path.dirname(file_name))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise    

    def get_file_name_from_cd(self, url):
        """
        Get filename from content-disposition
        """
        headers = requests.head(url, allow_redirects=True).headers
        cd = headers.get('content-disposition')
        if not cd:
            return None
        fname = re.findall('filename=(.+)', cd)
        if len(fname) == 0:
            return None
        return fname[0]