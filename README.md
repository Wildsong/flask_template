# flask_template

Templates for Python flask apps.

simple_app/ -- uses blueprints

celery_app/ -- adds celery for async support

## Set up

```bash
conda create --name=flask --file=requirements.txt
conda activate flask
```
## Debug

Select which app you want to test in the debugger configurations and hit F5.

If the correct Flask app starts up, then
VSCode should open a browser that's pointing at it.

If you want to try running on HTTPS instead of HTTP then uncomment the
line "--cert=adhoc" in launch.json.

This version of launch.json attempts to do hot reload when you edit
source files. If you don't want that then change FLASK_DEBUG to 0 and
(optionally) add "--no-reload=true" under args.

I am using the "factory" pattern, so there is a "create_app" function
and it's called from start_simple_app.py. I don't need to use
the factory pattern here but it's needed in the celery app.



## To-do

* Make some generic forms
* Enable the login code.
* Perhaps add some notes on deployment.

