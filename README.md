# flask_template

This is a simple template for a Python flask app.

I was inspired by "Advanced Application Structure"
from "Mastering Flask Web Development", but I backed off
when the complexity started to go asymptotic on me.

This is the simple template, maybe I will add an
advanced one when I actually need it.

## Set up

```bash
conda create --name=flask --file=requirements.txt
conda activate flask
```
## Debug

If the setup went well, you should now be able to open VSCode and hit F5
to launch the app in a debugger.  If the Flask app starts up, then
VSCode should open a browser that's pointing at it.

If you want to try running on HTTPS instead of HTTP then uncomment the
line "--cert=adhoc" in launch.json.

This version of launch.json attempts to do hot reload when you edit
source files. If you don't want that then change FLASK_DEBUG to 0 and
(optionally) add "--no-reload=true" under args.

## To-do

* Make some generic forms
* Enable the login code.
* Perhaps add some notes on deployment.

