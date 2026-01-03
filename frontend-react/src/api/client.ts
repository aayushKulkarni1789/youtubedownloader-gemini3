import type {
  VideoInfo,
  DownloadProgress,
  StartDownloadResponse,
  MediaType,
  VideoResolution,
  VideoFormat,
  AudioQuality,
} from '../types';

const API_BASE = '/api';

export async function fetchVideoInfo(url: string): Promise<VideoInfo> {
  const response = await fetch(`${API_BASE}/info?url=${encodeURIComponent(url)}`);
  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Failed to fetch video info' }));
    throw new Error(error.detail || 'Failed to fetch video info');
  }
  return response.json();
}

export async function startDownload(params: {
  url: string;
  mediaType: MediaType;
  resolution: VideoResolution;
  format: VideoFormat;
  audioQuality: AudioQuality;
}): Promise<StartDownloadResponse> {
  const searchParams = new URLSearchParams({
    url: params.url,
    media_type: params.mediaType,
    resolution: params.resolution,
    video_format: params.format,
    audio_quality: params.audioQuality,
  });

  const response = await fetch(`${API_BASE}/download/start?${searchParams}`, {
    method: 'POST',
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Failed to start download' }));
    throw new Error(error.detail || 'Failed to start download');
  }
  return response.json();
}

export async function fetchDownloadProgress(taskId: string): Promise<DownloadProgress> {
  const response = await fetch(`${API_BASE}/download/progress/${taskId}`);
  if (!response.ok) {
    throw new Error('Failed to fetch download progress');
  }
  return response.json();
}

export function getDownloadFileUrl(taskId: string): string {
  return `${API_BASE}/download/file/${taskId}`;
}
