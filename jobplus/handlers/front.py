from flask import Blueprint, render_template, redirect, url_for, flash, \
        request, current_app

# from job.models import 
# from job.forms import 
# from flask_login import 

front = Blueprint('front', __name__)

@front.route('/')
def index():

    return render_template('front.html')


