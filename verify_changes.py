import requests
import time
import sys

BASE_URL = "http://localhost:8000"
VIDEO_URL = "https://www.youtube.com/watch?v=jNQXAC9IVRw"  # Me at the zoo


def verify():
    print("Starting download...")
    try:
        resp = requests.post(f"{BASE_URL}/api/download/start", params={"url": VIDEO_URL})
        resp.raise_for_status()
        task_id = resp.json()["task_id"]
        print(f"Task ID: {task_id}")
    except Exception as e:
        print(f"Failed to start download: {e}")
        sys.exit(1)

    while True:
        try:
            resp = requests.get(f"{BASE_URL}/api/download/progress/{task_id}")
            resp.raise_for_status()
            data = resp.json()
            status = data["status"]
            progress = data.get("progress", 0)
            print(f"Status: {status}, Progress: {progress}%")

            if status == "completed":
                print("Download completed!")
                break
            elif status == "error":
                print(f"Download failed: {data.get('error')}")
                sys.exit(1)

            time.sleep(2)
        except Exception as e:
            print(f"Error polling: {e}")
            sys.exit(1)

    print("Retrieving file...")
    try:
        resp = requests.get(f"{BASE_URL}/api/download/file/{task_id}")
        resp.raise_for_status()
        if len(resp.content) > 0:
            print(f"File retrieved successfully, size: {len(resp.content)} bytes")
        else:
            print("File is empty")
            sys.exit(1)
    except Exception as e:
        print(f"Failed to retrieve file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    print("Waiting for server...")
    # Wait for server to start
    for _ in range(20):
        try:
            requests.get(f"{BASE_URL}/health")
            print("Server is up!")
            break
        except:
            time.sleep(1)
    else:
        print("Server failed to start")
        sys.exit(1)

    verify()
