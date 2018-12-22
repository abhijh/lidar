import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Query } from '../models/query.model';
import { Album } from '../models/album.model';

@Injectable({
  providedIn: 'root'
})
export class MusicApiService {
  
  private SEARCH = 'api/music/search/'
  private SEARCH_ALBUM_DETAILS = 'api/music/search-album-details/'
  private ALBUM = 'api/music/album/'

  constructor(private _http: HttpClient) { }

  search(searchPayload: Query) {
    return this._http.post(this.SEARCH, searchPayload);
  }

  searchAlbumDetails(albumURL: Query) {
    return this._http.post(this.SEARCH_ALBUM_DETAILS, albumURL);
  }

  addToLibrary(album: Album) {
    return this._http.post(this.ALBUM, album);
  }

  deleteFromLibrary(album: Album) {
    return this._http.delete(this.ALBUM + album.id + '/');
  }

  albums() {
    return this._http.get(this.ALBUM);
  }

  albumDetails(id: number) {
    return this._http.get(this.ALBUM + id);
  }

  
}
