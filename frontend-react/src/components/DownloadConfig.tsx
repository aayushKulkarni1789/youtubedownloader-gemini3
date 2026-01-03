import React from 'react';
import type { MediaType, VideoResolution, VideoFormat, AudioQuality } from '../types';

interface DownloadConfigProps {
  mediaType: MediaType;
  resolution: VideoResolution;
  audioQuality: AudioQuality;
  format: VideoFormat;
  onMediaTypeChange: (type: MediaType) => void;
  onResolutionChange: (res: VideoResolution) => void;
  onAudioQualityChange: (quality: AudioQuality) => void;
  onFormatChange: (fmt: VideoFormat) => void;
}

const DownloadConfig: React.FC<DownloadConfigProps> = ({
  mediaType,
  resolution,
  audioQuality,
  format,
  onMediaTypeChange,
  onResolutionChange,
  onAudioQualityChange,
  onFormatChange
}) => {
  return (
    <div className="bg-[#1a1a1a] rounded-lg p-6 shadow-xl mb-8 border border-[#272727]">
      <h3 className="text-xl font-['Oswald'] font-bold text-white mb-6 border-b border-[#272727] pb-2">
        DOWNLOAD OPTIONS
      </h3>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="col-span-1 md:col-span-2 flex gap-4 mb-2">
          <button
            onClick={() => onMediaTypeChange('video')}
            className={`flex-1 py-3 rounded font-['Oswald'] font-bold tracking-wide transition-all ${
              mediaType === 'video'
                ? 'bg-red-600 text-white shadow-lg'
                : 'bg-[#272727] text-gray-400 hover:bg-[#333]'
            }`}
          >
            VIDEO
          </button>
          <button
            onClick={() => onMediaTypeChange('audio')}
            className={`flex-1 py-3 rounded font-['Oswald'] font-bold tracking-wide transition-all ${
              mediaType === 'audio'
                ? 'bg-red-600 text-white shadow-lg'
                : 'bg-[#272727] text-gray-400 hover:bg-[#333]'
            }`}
          >
            AUDIO ONLY
          </button>
        </div>

        {mediaType === 'video' ? (
          <>
            <div className="flex flex-col gap-2">
              <label className="text-gray-400 font-['Lato'] text-sm font-bold">RESOLUTION</label>
              <select
                value={resolution}
                onChange={(e) => onResolutionChange(e.target.value as VideoResolution)}
                className="bg-[#272727] border border-[#3d3d3d] rounded px-4 py-3 text-white focus:outline-none focus:border-red-500 font-['Lato']"
              >
                <option value="Best">Best Available</option>
                <option value="1080p">1080p</option>
                <option value="720p">720p</option>
                <option value="480p">480p</option>
                <option value="360p">360p</option>
              </select>
            </div>
            <div className="flex flex-col gap-2">
              <label className="text-gray-400 font-['Lato'] text-sm font-bold">FORMAT</label>
              <select
                value={format}
                onChange={(e) => onFormatChange(e.target.value as VideoFormat)}
                className="bg-[#272727] border border-[#3d3d3d] rounded px-4 py-3 text-white focus:outline-none focus:border-red-500 font-['Lato']"
              >
                <option value="mp4">MP4</option>
                <option value="mkv">MKV</option>
                <option value="webm">WebM</option>
              </select>
            </div>
          </>
        ) : (
          <div className="col-span-1 md:col-span-2 flex flex-col gap-2">
            <label className="text-gray-400 font-['Lato'] text-sm font-bold">AUDIO QUALITY</label>
            <select
              value={audioQuality}
              onChange={(e) => onAudioQualityChange(e.target.value as AudioQuality)}
              className="bg-[#272727] border border-[#3d3d3d] rounded px-4 py-3 text-white focus:outline-none focus:border-red-500 font-['Lato']"
            >
              <option value="Best">Best Available</option>
              <option value="320kbps">320kbps (High)</option>
              <option value="256kbps">256kbps</option>
              <option value="192kbps">192kbps</option>
              <option value="128kbps">128kbps</option>
            </select>
          </div>
        )}
      </div>
    </div>
  );
};

export default DownloadConfig;
