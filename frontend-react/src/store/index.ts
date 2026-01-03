import { create } from 'zustand';
import type { VideoInfo, DownloadConfig } from '../types';

interface AppState {
  url: string;
  videoInfo: VideoInfo | null;
  taskId: string | null;
  downloadConfig: DownloadConfig;

  setUrl: (url: string) => void;
  setVideoInfo: (info: VideoInfo | null) => void;
  setTaskId: (taskId: string | null) => void;
  setDownloadConfig: (config: Partial<DownloadConfig>) => void;
  reset: () => void;
}

const defaultConfig: DownloadConfig = {
  mediaType: 'video',
  resolution: 'Best',
  format: 'mp4',
  audioQuality: 'Best',
};

export const useAppStore = create<AppState>((set) => ({
  url: '',
  videoInfo: null,
  taskId: null,
  downloadConfig: defaultConfig,

  setUrl: (url) => set({ url }),
  setVideoInfo: (videoInfo) => set({ videoInfo }),
  setTaskId: (taskId) => set({ taskId }),
  setDownloadConfig: (config) =>
    set((state) => ({
      downloadConfig: { ...state.downloadConfig, ...config },
    })),
  reset: () =>
    set({
      url: '',
      videoInfo: null,
      taskId: null,
      downloadConfig: defaultConfig,
    }),
}));
