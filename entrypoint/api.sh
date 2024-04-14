PORT=${PORT:-8080}
HOST=${HOST:-127.0.0.1}
APP_ENV=${APP_ENV:-dev}
WORKERS=${WORKERS:-1}
cmd="gunicorn -b $HOST:$PORT aero_copilot.api.main:app --workers $WORKERS -k uvicorn.workers.UvicornWorker"q
if [ "$APP_ENV" = "dev" ]; then
    echo "Running in development mode"    
    exec $cmd --reload
else
    exec $cmd
fi