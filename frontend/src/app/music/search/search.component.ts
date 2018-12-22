import { Component, OnInit } from '@angular/core';
import { Query } from '../models/query.model';
import { MusicApiService } from '../services/music-api.service';
import { Album } from '../models/album.model';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {
  
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
  albums: Album[];
  
  searchPayload = new Query(this.SEARCH_TYPES[0].value);

  constructor(private _musicApiService: MusicApiService) { }

  ngOnInit() {
  }

  onSearch() {
    this._musicApiService.search(this.searchPayload)
      .subscribe((albums: Album[]) => this.albums = albums);
  }
}
