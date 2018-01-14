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


@job.route('/<int:job_id>')
def detail(job_id):
    job =job.query.get_or_404(job_id)

    return render_template('job/detail.html', job=job, active='')

@job.route('/<int:job_id>/apply')
@login_required
def apply(job_id)

    job = Job.query.get_or_404(job_id)

    if current_user.resume_user is None:
        flash('please upload your file', 'warnning')
    elif job.current_user_is_applied:
        flash('you hav t applied this job', 'warnning')
    else:
        d = Delivery(
                job_id=job.id, 
                user_id=current_user.id, 
                company_id = job.company.id
                )
        db.session.add(d)
        db.session.commit()
        flash('input successful', 'success')
    return redirect(url_for('job.detail', job_id=job.id))

@job.route('/<int:job_id>/disable')
@login_required
def disable(job_id):
    job = Job.query.get_or_404(job_id)

    if not current_user.is_admin and current_user.id != job.company.id:
        abort(404) 
    if job.is_disable:
        flash('job is offline', 'waringing')

    else:
        job.is_disable = True
        db.session.add(job)
        db.session.commit()
        flash('job is offline ', 'success')

    if current_user.is_admin:

        return redirect(url_for('admin.jobs'))
    else:
        return redirect(url_for('company.admin_index', 
            company_id=job.company.id))

@job.route('/<int:job_id>/enable')
@login_required
def enable(job_id):
    job = Job.query.get_or_404(job_id)

    if not current_user.is_admin and current_user.id != job.company.id:
        abort(404)

    if not job.is_disable:
        flash('job is already online', 'warnning')

    else:
        job.is_disable = False
        db.session.add(job)
        db.session.commit()
        flash('job is online ', 'success')

    if current_user.is_admin:
        return redirect(url_for('admin.jobs'))
    else:
        return redirect(url_for('company.admin_index', 
                company_id = job.company.id))

