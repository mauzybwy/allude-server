# screen -m gunicorn --bind :6969 --timeout 0 --workers 1 --threads 8 server:app
gunicorn --bind :6969 --timeout 0 --workers 1 --threads 8 server:app
# gunicorn --bind :6969 --timeout 0 --workers 1 --threads 8 blueprint:reddit_blueprint
