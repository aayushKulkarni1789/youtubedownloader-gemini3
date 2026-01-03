import React from 'react';

interface UrlInputProps {
  url: string;
  onUrlChange: (url: string) => void;
  onFetch: () => void;
  isLoading: boolean;
}

const UrlInput: React.FC<UrlInputProps> = ({ url, onUrlChange, onFetch, isLoading }) => {
  return (
    <div className="flex flex-col md:flex-row gap-4 mb-8">
      <input
        type="text"
        value={url}
        onChange={(e) => onUrlChange(e.target.value)}
        placeholder="Paste YouTube URL here..."
        className="flex-1 bg-[#272727] border border-[#3d3d3d] rounded px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-red-500 font-['Lato'] transition-colors"
        disabled={isLoading}
      />
      <button
        onClick={onFetch}
        disabled={isLoading || !url.trim()}
        className={`px-8 py-3 rounded font-['Oswald'] font-bold tracking-wider text-white transition-all
          ${isLoading || !url.trim() 
            ? 'bg-gray-700 cursor-not-allowed opacity-50' 
            : 'bg-gradient-to-r from-red-600 to-red-700 hover:from-red-700 hover:to-red-800 shadow-lg transform hover:-translate-y-0.5'
          }`}
      >
        {isLoading ? 'LOADING...' : 'FETCH INFO'}
      </button>
    </div>
  );
};

export default UrlInput;
