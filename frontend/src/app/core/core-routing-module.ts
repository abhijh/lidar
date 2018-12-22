import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  { path: 'dashboard', loadChildren: '../dashboard/dashboard.module#DashboardModule'},
  { path: 'music', loadChildren: '../music/music.module#MusicModule' },
  { path: '**', redirectTo: '/music/search', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CoreRoutingModule { }
