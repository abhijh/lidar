import { Component, Input, OnInit, OnChanges } from '@angular/core';
import { fromEvent } from 'rxjs';
import { Album } from '../models/album.model';
import { MusicApiService } from '../services/music-api.service';
import { Router } from '@angular/router';
import { DownloaderService } from '../../shared/services/downloader.service';
import { DownloadPayload } from '../../shared/models/download-payload.model';

@Component({
  selector: 'album-details',
  templateUrl: './album-details.component.html',
  styleUrls: ['./album-details.component.scss']
})
export class AlbumDetailsComponent implements OnInit {
  displayedTrackColumns: string[] = ['title', 'url'];
  player;
  playing;
  interval;

  constructor(private _musicApiService: MusicApiService,
    private _router: Router,
    private _downloaderService: DownloaderService) { }

  @Input() album: Album;

  ngOnInit() {
    this.player = <HTMLAudioElement>document.querySelector("#audio-player");
    fromEvent(this.player, 'ended').subscribe(this.stop);    
  }

  ngOnChanges() {
    if(this.album['pid']) {
      if (this.interval) {
        clearInterval(this.interval);
      }
      this.interval = setInterval(() => { this.fetchDownloadStatus() }, 1000);
    }
  }

  fetchDownloadStatus() {
    console.log("Calling");
    let downloadPayload = new DownloadPayload();
    downloadPayload.pid = this.album.pid;
    this._downloaderService.getProgress(downloadPayload)
      .subscribe(response => console.log, error => console.error);
  }

  onAddToLibrary() {
    delete this.album.image;
    this._musicApiService.addToLibrary(this.album).subscribe((album:Album) => {
      this._router.navigate(['/music/details', album.id]);      
    }, error => console.error);
  }

  onDeleteFromLibrary() {
    this._musicApiService.deleteFromLibrary(this.album).subscribe(album => {
      localStorage.removeItem('album');
      this._router.navigate(['/music']);
    }, error => console.error);
  }

  onDownloadSelectedTracks() {
    this._downloaderService.download(new DownloadPayload(this.album.title, this.album.tracks.filter(el => el.download)))
      .subscribe(response => console.log, error => console.error);
  }

  play(track) {
    if(this.playing !== track) {
      this.playing = track;
      this.player.src = track.url;
    }
    this.player.play();
  }

  pause() {
    this.player.pause();
  }

  stop() {
    this.player.pause();
    this.player.currentTime = 0;
    this.playing = undefined;
  }

  isPlaying(track) {
    return track == this.playing && !this.player.ended;
  }
}
