import { Component, OnInit } from '@angular/core';
import { MusicApiService } from '../services/music-api.service';
import { Album } from '../models/album.model';
import { Query } from '../models/query.model';

@Component({
  selector: 'app-music',
  templateUrl: './music.component.html',
  styleUrls: ['./music.component.scss']
})
export class MusicComponent implements OnInit {
  albums: Album[];
  SEARCH_TYPES = [
    {
      'value': 'album',
      'viewValue': 'Albums'
    },
    {
      'value': 'singles',
      'viewValue': 'Singles'
    }
  ]
  searchPayload: Query = new Query(this.SEARCH_TYPES[0].value);
  
  constructor(private _musicApiService: MusicApiService) { }

  ngOnInit() {
    this._musicApiService.albums()
      .subscribe((albums: Album[]) => this.albums = albums);
  }

}
