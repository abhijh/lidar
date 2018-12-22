import { TestBed } from '@angular/core/testing';

import { MusicApiService } from './music-api.service';

describe('MediaApiService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: MusicApiService = TestBed.get(MusicApiService);
    expect(service).toBeTruthy();
  });
});
