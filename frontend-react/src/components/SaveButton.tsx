import React from 'react';

interface SaveButtonProps {
  downloadUrl: string | null;
  filename: string;
}

const SaveButton: React.FC<SaveButtonProps> = ({ downloadUrl, filename }) => {
  if (!downloadUrl) return null;

  return (
    <div className="text-center animate-fade-in">
      <a
        href={downloadUrl}
        download={filename}
        className="inline-block bg-[#272727] hover:bg-[#333] border border-green-600 text-green-500 hover:text-green-400 font-['Oswald'] font-bold text-lg py-3 px-8 rounded shadow-lg transition-all transform hover:-translate-y-0.5 tracking-wide"
      >
        SAVE FILE
      </a>
      <p className="mt-3 text-gray-500 text-sm font-['Lato']">
        Click to save {filename} to your device
      </p>
    </div>
  );
};

export default SaveButton;
