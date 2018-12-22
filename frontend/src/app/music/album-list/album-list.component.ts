import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Album } from '../models/album.model';

@Component({
  selector: 'album-list',
  templateUrl: './album-list.component.html',
  styleUrls: ['./album-list.component.scss']
})
export class AlbumListComponent implements OnInit {
  @Input() public albums: Album[];
  
  constructor(private _router: Router) { }

  ngOnInit() { }

  navigate(album: Album) {
    localStorage.setItem('album', JSON.stringify(album));
    if(album.id) {
      this._router.navigate(['/music/details/', album.id]);
    } else {
      this._router.navigate(['/music/search/details/', album.url]);
    }
    
  }
}
