from flask import Blueprint, render_template, redirect, flash
from celery_app.main.forms import AdditionForm
from .tasks import Add

from flask import current_app
from celery.result import AsyncResult

main_blueprint = Blueprint(
    'main', 
    __name__,
    template_folder='../templates/main'
)

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

@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    z = None
    form = AdditionForm()
    if form.validate_on_submit():
        # We've received input.

        try:
            x = s2i(form.x.data)
            y = s2i(form.y.data)

            print("Here is where you need to queue the request.",x,y)
            task = Add.delay(x,y)
            
            async_result = AsyncResult(id=task.task_id, app=current_app.celery)
            # On the first pass, (after you submit data)
            # this will return z=None
            # Then wen some result comes back we'll execute this code again
            # with z = the results from the Celery worker.
            z = async_result.get()

        except Exception as e:
            print("Can't get values", e)
            error = e
            return redirect("/fail")      
        
    return render_template('addition.html', form=form, result=z)

# That's all!
