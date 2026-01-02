import { useMutation } from '@tanstack/react-query';
import { startDownload } from '../api/client';
import { useAppStore } from '../store';

export function useDownload() {
  const { url, downloadConfig, setTaskId } = useAppStore();

  const mutation = useMutation({
    mutationFn: () =>
      startDownload({
        url,
        mediaType: downloadConfig.mediaType,
        resolution: downloadConfig.resolution,
        format: downloadConfig.format,
        audioQuality: downloadConfig.audioQuality,
      }),
    onSuccess: (data) => {
      setTaskId(data.task_id);
    },
  });

  return {
    start: mutation.mutate,
    isLoading: mutation.isPending,
    error: mutation.error,
  };
}
