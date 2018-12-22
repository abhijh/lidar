import { Component, OnInit } from '@angular/core';
import { Album } from '../models/album.model';
import { ActivatedRoute, Router } from '@angular/router';
import { MusicApiService } from '../services/music-api.service';
import { Query } from '../models/query.model';

@Component({
  selector: 'app-search-details',
  templateUrl: './search-details.component.html',
  styleUrls: ['./search-details.component.scss']
})
export class SearchDetailsComponent implements OnInit {
  
  album: Album;
  
  constructor(private _route: ActivatedRoute,
    private _router: Router,
    private _musicApiService: MusicApiService) { }

  ngOnInit() {
    this._route.params.subscribe(params => {
      let url = params['url'];
      if(url) {
      let query = new Query();
        query.url = url;
        this._musicApiService.searchAlbumDetails(query).subscribe((album: Album) => this.album = album);
      } else {
        this._router.navigate(['/music/search']);
      }
    });
  }

}
