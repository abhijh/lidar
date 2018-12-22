import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MaterialModule } from '../material.module';
import { MusicRoutingModule } from './music-routing.module';
import { SearchComponent } from './search/search.component';
import { AlbumListComponent } from './album-list/album-list.component';
import { SearchDetailsComponent } from './search-details/search-details.component';
import { AlbumDetailsComponent } from './album-details/album-details.component';
import { MusicComponent } from './music/music.component';
import { MusicDetailsComponent } from './music-details/music-details.component';

@NgModule({
  declarations: [
    SearchComponent,
    AlbumListComponent,
    SearchDetailsComponent,
    AlbumDetailsComponent,
    MusicComponent,
    MusicDetailsComponent,
  ],
  imports: [
    CommonModule,
    FormsModule,
    MaterialModule,
    MusicRoutingModule,
  ]
})
export class MusicModule { }
