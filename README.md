# flask_template

Templates for Python flask apps.

simple_app/ -- uses blueprints

celery_app/ -- adds celery for async support

## Read this book

If you read it, then a lot of the code here will be familiar.
https://learning.oreilly.com/library/view/flask-web-development

## Set up

Create a conda environment with the requirements. This does not
pin down versions, so it's not suitable for production. This is only
a template. (Or rather "templates".)

```bash
conda create --name=flask --file=requirements.txt
conda activate flask
```


### Testing

TODO: I have only just started adding unit tests so this is not working yet.

The templates have unit testing templates too.
See also https://docs.python.org/3.6/library/unittest.html

#### Monitor and test Celery

Browse to port 5555. In a terminal, start a bunch of tasks so there is something to monitor.

```bash
docker run -it -e FLASK_APP=start_celery_app --net=flask_template_flask_net -v `pwd`:/srv wildsong/flask flask shell
from app_celery.main.tasks import *
from celery import chord, group
sig = chord(group(add.s(1, 1) for i in range(1000)), log.s())
sig.delay()
```

## Running in debugger

Select which app you want to test in the debugger configurations and hit F5.

If the correct Flask app starts up, then (happy days),
VSCode should offer to open a browser that's pointing at it.
(This even works with remote access because VSCode forwards ports.)

If you want to try running on HTTPS instead of HTTP then uncomment the
line "--cert=adhoc" in launch.json.

This version of launch.json attempts to do hot reload when you edit
source files. If you don't want that then change FLASK_DEBUG to 0 and
(optionally) add "--no-reload=true" under args.

### Celery app

The Celery app uses three components so in addition to the web app you also
have to launch the celery worker and redis.

To start Redis, (it runs in background):
```bash
docker run -d -p 6379:6379 redis:latest
```

You can run both the app and the worker at the same time using F5
if you select the "compound" entry called Celery App/Worker in launch.json 

## Running in Docker

This is a template but includes sample Docker files to run the Celery app.

```bash
docker-compose build
docker-compose up -d
```

## Kernel optimization

These messages are disturbing me
```bash
redis_1    | 1:C 26 Jan 2021 22:30:26.220 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
redis_1    | 1:M 26 Jan 2021 22:30:26.251 * Running mode=standalone, port=6379.
redis_1    | 1:M 26 Jan 2021 22:30:26.251 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
redis_1    | 1:M 26 Jan 2021 22:30:26.251 # Server initialized
redis_1    | 1:M 26 Jan 2021 22:30:26.251 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
redis_1    | 1:M 26 Jan 2021 22:30:26.252 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo madvise > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled (set to 'madvise' or 'never').
```

## To-do

* Make some generic forms
* Enable the login code.
* Perhaps add some notes on deployment, after I figure out how.

