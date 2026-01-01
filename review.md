# Code Review - Uncommitted Changes

Date: 2026-01-01

## Bugs

### 1. frontend/app.py:136 - `media_type` capture timing bug

When the download completes (line 132-137), the code captures `media_type` into session state:

```python
st.session_state.download_file = {
    ...
    "media_type": media_type,  # Line 136
}
```

`media_type` is set at line 46 (`media_type = st.selectbox(...)`). If the user changes the media type dropdown while the download is running, the captured value will be the current dropdown value, not the value used to start the download. This causes the download button label (line 157) to display the wrong media type.

Fix: Capture the media type when starting the download (around line 84).

### 2. frontend/app.py:95-152 - No polling timeout

The progress polling loop has no timeout mechanism:

```python
while True:  # Line 95
    try:
        response = requests.get(...)
```

If the backend crashes, never sends "completed"/"error", or the network disconnects, this loop runs forever, hanging the UI. The only exit conditions are success or explicit error from the API.

Fix: Add a timeout (e.g., 5-10 minutes) and break with an error message if exceeded.

### 3. frontend/app.py:127-130 - Vulnerable content-disposition parsing

```python
if content_disposition:
    try:
        filename = content_disposition.split("filename=")[1].strip('"')
    except:
        pass
```

This parsing is fragile. If the header format differs (e.g., `filename*=utf-8''...`), it fails silently, falling back to "video.mp4". It also doesn't validate the extracted filename for path traversal attacks.

Fix: Use a proper header parsing library or more robust regex, and validate the filename.

## Structure & Design Issues

### 4. backend/main.py:38 - Memory leak in global task storage

```python
tasks: Dict[str, Dict[str, Any]] = {}
```

Completed tasks remain in this dictionary forever. With enough downloads, this grows unbounded. There's no cleanup mechanism for old tasks.

### 5. backend/main.py:155 - Race condition in task access

```python
async def get_progress(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]  # Line 158
```

The global `tasks` dict is accessed without any locking. While GIL provides some protection in CPython, this is not thread-safe across multiple workers in production.

### 6. frontend/app.py:19-31 - Missing error handling for video info display

The code stores video info in session state (line 27) and displays it (lines 34-44). If the API response is missing expected fields (title, thumbnail, etc.), accessing `info["thumbnail"]` etc. will raise KeyError and crash the UI.

## Minor Issues

### 7. frontend/app.py:40-41 - Missing null checks

```python
st.write(f"**Views:** {info['views']}")
st.write(f"**Duration:** {info['duration']} seconds")
```

If `view_count` or `duration` are null/None, these display as "None" which is acceptable but could be more user-friendly.

### 8. frontend/app.py:129 - Bare except clause

```python
except:
    pass
```

Catches all exceptions including SystemExit/KeyboardInterrupt. Should be `except Exception:` or more specific.
