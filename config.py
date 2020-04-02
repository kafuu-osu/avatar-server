import multiprocessing
import os

log_dir = 'log'

current_path = os.getcwd()
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


bind = "0.0.0.0:5000"
workers = multiprocessing.cpu_count() * 2
threads = 4
worker_class = 'gevent'
daemon = False

loglevel = 'info'
pidfile = f"{current_path}/{log_dir}/gunicorn.pid"
accesslog = f"{current_path}/{log_dir}/access.log"
errorlog = f"{current_path}/{log_dir}/debug.log"

