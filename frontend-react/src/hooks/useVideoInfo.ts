import { useMutation } from '@tanstack/react-query';
import { fetchVideoInfo } from '../api/client';
import { useAppStore } from '../store';

export function useVideoInfo() {
  const { url, setVideoInfo, setTaskId } = useAppStore();

  const mutation = useMutation({
    mutationFn: () => fetchVideoInfo(url),
    onSuccess: (data) => {
      setVideoInfo(data);
      setTaskId(null);
    },
  });

  return {
    fetch: mutation.mutate,
    isLoading: mutation.isPending,
    error: mutation.error,
  };
}
