import { useQuery } from '@tanstack/react-query';
import { fetchDownloadProgress, getDownloadFileUrl } from '../api/client';
import { useAppStore } from '../store';

export function useProgress() {
  const taskId = useAppStore((state) => state.taskId);

  const query = useQuery({
    queryKey: ['progress', taskId],
    queryFn: () => fetchDownloadProgress(taskId!),
    enabled: !!taskId,
    refetchInterval: (query) => {
      const status = query.state.data?.status;
      if (status === 'completed' || status === 'error') {
        return false;
      }
      return 1000;
    },
  });

  const downloadUrl = query.data?.status === 'completed' && taskId 
    ? getDownloadFileUrl(taskId) 
    : null;

  return {
    progress: query.data ?? null,
    isLoading: query.isLoading,
    error: query.error,
    downloadUrl,
    filename: query.data?.filename ?? 'download',
  };
}
