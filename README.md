# Avatar-server
Kafuu avatar server

## python3.6

`flask`
`gevent`
`gunicorn`


## step.1 requirements

```
pip3 install -r requirements.txt
```

## step.2 start

Choose one

- Start the service directly

```
python3 server.py
```

- Start service with gunicorn **(recommend, better performance)**

```
gunicorn -c config.py server:app
```
