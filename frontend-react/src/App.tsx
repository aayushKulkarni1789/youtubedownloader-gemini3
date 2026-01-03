import Header from './components/Header'
import UrlInput from './components/UrlInput'
import VideoPreview from './components/VideoPreview'
import DownloadConfig from './components/DownloadConfig'
import DownloadProgress from './components/DownloadProgress'
import SaveButton from './components/SaveButton'
import { useAppStore } from './store'
import { useVideoInfo, useDownload, useProgress } from './hooks'
import type { MediaType, VideoResolution, AudioQuality, VideoFormat } from './types'

function App() {
  const { url, setUrl, videoInfo, downloadConfig, setDownloadConfig } = useAppStore()

  const { fetch: fetchInfo, isLoading: isFetchingInfo } = useVideoInfo()
  const { start: startDownload, isLoading: isStartingDownload } = useDownload()
  const { progress, downloadUrl, filename } = useProgress()

  const handleFetch = () => {
    if (url.trim()) {
      fetchInfo()
    }
  }

  const handleDownload = () => {
    if (url.trim()) {
      startDownload()
    }
  }

  const isDownloading = progress?.status === 'downloading' || isStartingDownload

  return (
    <div className="min-h-screen bg-[#0F0F0F] font-['Lato']">
      <Header />
      <main className="max-w-4xl mx-auto px-4 py-8 space-y-6">
        <UrlInput
          url={url}
          onUrlChange={setUrl}
          onFetch={handleFetch}
          isLoading={isFetchingInfo}
        />

        {videoInfo && (
          <>
            <VideoPreview videoInfo={videoInfo} />
            <DownloadConfig
              mediaType={downloadConfig.mediaType}
              resolution={downloadConfig.resolution}
              audioQuality={downloadConfig.audioQuality}
              format={downloadConfig.format}
              onMediaTypeChange={(v: MediaType) => setDownloadConfig({ mediaType: v })}
              onResolutionChange={(v: VideoResolution) => setDownloadConfig({ resolution: v })}
              onAudioQualityChange={(v: AudioQuality) => setDownloadConfig({ audioQuality: v })}
              onFormatChange={(v: VideoFormat) => setDownloadConfig({ format: v })}
            />
            <DownloadProgress
              progress={progress}
              onDownload={handleDownload}
              isDownloading={isDownloading}
            />
            <SaveButton
              downloadUrl={downloadUrl}
              filename={filename}
            />
          </>
        )}
      </main>
    </div>
  )
}

export default App
