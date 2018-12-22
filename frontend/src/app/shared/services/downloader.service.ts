import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { DownloadPayload } from '../models/download-payload.model';

@Injectable({
  providedIn: 'root'
})
export class DownloaderService {
  DOWNLOAD_URL = '/api/download/'
  PROGRESS_URL = '/api/download/progress/'
  constructor(private _http: HttpClient) { }

  download(downloadPayload: DownloadPayload) {
    return this._http.post(this.DOWNLOAD_URL, downloadPayload);
  }

  getProgress(downloadPayload: DownloadPayload) {
    return this._http.get(this.PROGRESS_URL + '/' + downloadPayload.pid + '/');
  }
  
}
