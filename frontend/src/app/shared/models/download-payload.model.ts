import { Track } from '../../music/models/track.model';

export class DownloadPayload {
    constructor(
        public name?: string,
        public tracks?: Track[],
        public pid?: number,
    ) {  }
  
}