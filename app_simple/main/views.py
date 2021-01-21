from flask import Blueprint, render_template, redirect, flash
from . import main
from .forms import AdditionForm

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

            z = x+y

        except Exception as e:
            print("Can't get values", e)
            error = e
            return redirect("/fail")      
        
    return render_template('addition.html', form=form, result=z)

# That's all!
