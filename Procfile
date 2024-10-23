web: gunicorn -w 2 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080 --worker-tmp-dir /dev/shm app:app
# web: uvicorn app:app --host 0.0.0.0 --port 8080 --workers 2