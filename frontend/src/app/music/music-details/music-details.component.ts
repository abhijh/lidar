import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Album } from '../models/album.model';
import { MusicApiService } from '../services/music-api.service';

@Component({
  selector: 'app-music-details',
  templateUrl: './music-details.component.html',
  styleUrls: ['./music-details.component.scss']
})
export class MusicDetailsComponent implements OnInit {

  album: Album;

  constructor(private _route: ActivatedRoute,
    private _router: Router,
    private _musicApiService: MusicApiService) { }

  ngOnInit() {
    this._route.params.subscribe(params => {
      let id = params['id'];
      if(id) {
        this._musicApiService.albumDetails(id)
        .subscribe((album: Album) => this.album = album, error => this._router.navigate(['/music']));
      } else {
        this._router.navigate(['/music']);
      }
    });
  }

}
