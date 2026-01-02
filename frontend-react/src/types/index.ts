export interface VideoInfo {
  title: string;
  uploader: string;
  views: number;
  duration: number;
  thumbnail: string;
}

export interface DownloadProgress {
  status: 'pending' | 'downloading' | 'processing' | 'completed' | 'error';
  progress: number;
  filename: string | null;
  error: string | null;
}

export type MediaType = 'video' | 'audio';

export type VideoResolution = 'Best' | '1080p' | '720p' | '480p' | '360p';

export type VideoFormat = 'mp4' | 'mkv' | 'webm';

export type AudioQuality = 'Best' | '320kbps' | '256kbps' | '192kbps' | '128kbps';

export interface DownloadConfig {
  mediaType: MediaType;
  resolution: VideoResolution;
  format: VideoFormat;
  audioQuality: AudioQuality;
}

export interface StartDownloadResponse {
  task_id: string;
}
