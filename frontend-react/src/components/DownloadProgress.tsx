import React from 'react';
import type { DownloadProgress as DownloadProgressType } from '../types';

interface DownloadProgressProps {
  progress: DownloadProgressType | null;
  onDownload: () => void;
  isDownloading: boolean;
}

const DownloadProgress: React.FC<DownloadProgressProps> = ({ progress, onDownload, isDownloading }) => {
  const isComplete = progress?.status === 'completed';
  const percent = progress?.progress || 0;

  return (
    <div className="mb-8">
      {!isDownloading && !isComplete ? (
        <button
          onClick={onDownload}
          className="w-full bg-gradient-to-r from-red-600 to-red-700 hover:from-red-700 hover:to-red-800 text-white font-['Oswald'] font-bold text-xl py-4 rounded shadow-lg transform hover:-translate-y-0.5 transition-all tracking-wider"
        >
          START DOWNLOAD
        </button>
      ) : (
        <div className="bg-[#1a1a1a] rounded-lg p-6 border border-[#272727]">
          <div className="flex justify-between items-end mb-2">
            <span className="text-white font-['Oswald'] text-lg">
              {progress?.status === 'processing' ? 'PROCESSING...' : 
               progress?.status === 'completed' ? 'COMPLETE!' : 'DOWNLOADING...'}
            </span>
            <span className="text-red-500 font-bold font-['Lato']">
              {isComplete ? '100%' : `${Math.round(percent)}%`}
            </span>
          </div>
          <div className="w-full bg-[#272727] rounded-full h-4 overflow-hidden">
            <div 
              className="bg-gradient-to-r from-red-600 to-red-700 h-full transition-all duration-300 ease-out"
              style={{ width: `${isComplete ? 100 : percent}%` }}
            />
          </div>
          {progress?.error && (
            <div className="mt-4 text-red-500 font-['Lato'] text-sm bg-red-900/20 p-3 rounded border border-red-900/50">
              Error: {progress.error}
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default DownloadProgress;
