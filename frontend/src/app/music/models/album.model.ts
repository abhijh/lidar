import { Track } from './track.model';

export class Album {

    constructor(
      public id: number,
      public title: string,
      public url: string,
      public image: string,
      public tracks?: Track[],
      public pid?: number,
    ) {  }
  
  }