import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SearchComponent } from './search/search.component';
import { SearchDetailsComponent } from './search-details/search-details.component';
import { MusicComponent } from './music/music.component';
import { MusicDetailsComponent } from './music-details/music-details.component';

const routes: Routes = [
  { path: 'search', component: SearchComponent },
  { path: 'search/details/:url', component: SearchDetailsComponent },
  { path: 'details/:id', component: MusicDetailsComponent },
  { path: '', component: MusicComponent },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MusicRoutingModule { }
