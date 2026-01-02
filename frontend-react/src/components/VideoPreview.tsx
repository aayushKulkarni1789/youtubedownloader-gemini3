import React from 'react';
import type { VideoInfo } from '../types';

interface VideoPreviewProps {
  videoInfo: VideoInfo | null;
}

const VideoPreview: React.FC<VideoPreviewProps> = ({ videoInfo }) => {
  if (!videoInfo) return null;

  return (
    <div className="bg-[#1a1a1a] rounded-lg overflow-hidden shadow-xl mb-8 animate-fade-in border border-[#272727]">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-0">
        <div className="md:col-span-1 relative aspect-video md:aspect-auto">
          <img 
            src={videoInfo.thumbnail} 
            alt={videoInfo.title} 
            className="w-full h-full object-cover"
          />
          <div className="absolute bottom-2 right-2 bg-black/80 px-2 py-1 text-xs text-white rounded font-['Lato']">
            {new Date(videoInfo.duration * 1000).toISOString().substr(11, 8).replace(/^00:/, '')}
          </div>
        </div>
        <div className="md:col-span-2 p-6 flex flex-col justify-center">
          <h2 className="text-xl md:text-2xl font-['Oswald'] font-bold text-white mb-2 line-clamp-2">
            {videoInfo.title}
          </h2>
          <div className="flex flex-wrap gap-4 text-gray-400 font-['Lato'] text-sm">
            <span className="flex items-center gap-1">
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
              {videoInfo.uploader}
            </span>
            <span className="flex items-center gap-1">
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
              {videoInfo.views.toLocaleString()} views
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default VideoPreview;
