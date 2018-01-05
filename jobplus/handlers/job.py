from flask import Blueprint, render_template, request, current_app, \
    redirect, url_for, flash

#from jobplus.decorators import admin_required
#from jobplus.models import
#from jobplus.forms import 


job = Blueprint('job',__name__, url_prefix='/job')

@job.route('/')
def index():

    return render_template('job/job.html')


@job.route('/joblist')
def job_list():

    return render_template('job/job_list.html')
