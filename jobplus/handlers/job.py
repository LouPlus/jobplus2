from flask import Blueprint, render_template, request, current_app, \
    redirect, url_for, flash

#from jobplus.decorators import admin_required
from jobplus.models import Job
#from jobplus.forms import 


job = Blueprint('job',__name__, url_prefix='/job')

@job.route('/')
def index():

    return render_template('job/job.html')


@job.route('/joblist')
def job_list():

    page = request.args.get('page', default=1, type=int)
    jobs = Job.query.paginate(page, per_page=\
            current_app.config['INDEX_PER_PAGE'],
            error_out=False)

    return render_template('job/job_list.html',\
            pagination=jobs, active='job')



