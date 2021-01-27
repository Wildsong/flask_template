from flask import Blueprint, render_template, redirect, flash
from . import main
from  .forms import AdditionForm

from flask import current_app
from .tasks import add, info, log
from celery.result import AsyncResult

def s2i(s):
    """ Convert a string to an integer even if it has + and , in it. """
    if s == None or s == '':
        return None
    if type(s) == type(0):
        # This is already an integer
        return s
    if s:
        return int(float(s.replace(',', '')))
    return None

@main.route('/', methods=['GET', 'POST'])
def index():
    z = None
    form = AdditionForm()
    if form.validate_on_submit():
        # We've received input.

        try:
            x = s2i(form.x.data)
            y = s2i(form.y.data)

            print("Queue request:",x,y)
            task = add.delay(x,y)
            
            async_result = AsyncResult(id=task.task_id, app=current_app.celery)
            # On the first pass, (after you submit data)
            # this will return z=None
            # Then wen some result comes back we'll execute this code again
            # with z = the results from the Celery worker.
            z = async_result.get()
            print("result =", z)

        except Exception as e:
            print("Can't get values", e)
            error = e
            return redirect("/fail")      
        
    return render_template('addition.html', form=form, result=z)

@main.route('/info')
def info():
    try:
        print("Queue request:")
        task = info.delay()
        
        async_result = AsyncResult(id=task.task_id, app=current_app.celery)
        info = async_result.get()
        print("info =", info)

    except Exception as e:
        print("Can't get info", e)
        error = e
        return redirect("/fail")      
        
    return render_template('info.html', result=info)

# That's all!
