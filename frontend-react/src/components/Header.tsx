import React from 'react';

const Header: React.FC = () => {
  return (
    <header className="bg-gradient-to-r from-red-600 to-red-700 py-6 px-4 shadow-lg mb-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl md:text-4xl font-['Oswald'] font-bold text-white tracking-wide uppercase">
          YouTube Downloader
        </h1>
      </div>
    </header>
  );
};

export default Header;
