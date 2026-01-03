#!/bin/bash

cleanup() {
    echo "Stopping services..."
    kill $(jobs -p) 2>/dev/null
    exit
}

trap cleanup SIGINT SIGTERM

if ! command -v uv &> /dev/null; then
    echo "Error: 'uv' is not installed. Please install it first (e.g., curl -LsSf https://astral.sh/uv/install.sh | sh)"
    exit 1
fi

if ! command -v npm &> /dev/null; then
    echo "Error: 'npm' is not installed. Please install Node.js first."
    exit 1
fi

echo "Creating virtual environment..."
uv venv

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing Python dependencies with uv..."
uv pip install -r requirements.txt

echo "Installing frontend dependencies..."
cd frontend-react && npm install && cd ..

echo "Starting Backend..."
uv run uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

echo "Starting Frontend..."
cd frontend-react && npm run dev &
FRONTEND_PID=$!
cd ..

echo "Application is running!"
echo "Backend: http://localhost:8000/docs"
echo "Frontend: http://localhost:5173"

wait $BACKEND_PID $FRONTEND_PID
