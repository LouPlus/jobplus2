from flask import Blueprint , render_template, request, current_app, \
    redirect, url_for, flash , abort 

from flask_login import login_required, current_user
from jobplus.forms import CompanyProfileForm
## JobFrom hav't import yet 
from jobplus.models import User, Job, Delivery, db


company = Blueprint('company',__name__, url_prefix='/company')

@company.route('/')
def index():
    
    page = request.args.get('page', 1, type=int)
    pagination = User.query.filter(
            User.role==User.ROLE_COMPANY
            ).order_by(User.created_at.desc()).paginate(
                    page=page,
                    per_page=12,
                    error_out=False
                    )
    return render_template('company/front.html',
            pagination=pagination, active='company')

#    return render_template('company/front.html')
#    return "hollow"

@company.route('/profile/',methods=['GET', 'POST'])
def profile():

    return "profile is ok"


#@company.route('/profile/', methods=['GET', 'POST'])
#@login_required
#def profile():
#
#    if not current_user.is_company:
#        flash('Your are not comapany user', 'Warning')
#        return redirect(url_for('front.index'))
#
#    form = CompanyProfileForm(obj=current_user.company)
#    form.name.data = current_user.name
#    form.name.data = current_user.email
#
#    if form.validate_on_submit():
#        form.updated_profile(current_user)
#        flask('you have successful updated your info', 'success')
#
#        return redirect(url_for('front.index'))
#    return render_template('company/profile.html', form=form)

@company.route('/<int:company_id>')
def detail(company_id):
    company = User.query.get_or_404(company_id)
    if not company.is_company:
        abort(404)
    return render_template('company/detail.html', company=company,active='',panel='about')

@company.route('/<int:company_id>/jobs')
def company_jobs(company_id):
    company = User.query.get_or_404(company_id)
    if not company.is_company:
        abort(404)
    return render_template('company/detail.html', company=company,active='',panel='job')

@company.route('/<int:company_id>/admin')
@login_required
def admin_index(company_id):
    if not current_user.is_admin and not current_user.id == company_id:
        abort(404)

    page = request.args.get('page', default=1, type=int)
    pagination = Job.query.filter_by(company_id=company_id).paginate(
            page=page,
            per_page=current_app.config['ADMIN_PER_PAGE'],
            error_out=False
            )
    return render_template('company/admin_index.html',
            company_id=company_id, pagination=pagination) 

@company.route('/<int:company_id>/admin/apply')
@login_required
def admin_apply(company_id):

    if not current_user.is_admin and not current_user.id == company_id:
        abort(404)

    status = request.args.get('status', 'all')
    page = request.args.get('page', default=1, type=int)
    q = Delivery.query.filter_by(company_id=company_id)

    if stauts == 'waiting':
        q = q.filter(Delivery.status == Delivery.STATUS_WAITING)
    elif status == 'reject':
        q = q.filter(Delivery.status==Delivery.STATUS_REJECT)

    pagination = q.order_by(Delivery.created_at.desc()).pagintate(
            page=page,
            per_page=current_app.config['ADMIN_PER_PAGE'],
            error_out=False
            )
    return render_template('company/admin_apply.html',pagination=pagination,company_id=company_id)


@company.route('/<int:company_id>/admin/apply/<int:delivery_id>/reject/')
@login_required
def admin_apply_reject(company_id, delivery_id):
    d = Delivery.query.get_or_404(delivery_id)
    if current_user.id != company_id:
        abort(404)
    d.status = Delivery.STATUS_REJECT
    db.session.add(d)
    db.session.commit()

    return redirect(url_for('company.admin_apply',company_id=company_id))
@company.route('/<int:company_id>/admin/apply/<int:delivery_id>/accept/')
@login_required
def admin_apply_accept(company_id, delivery_id):
    d = Delivery.query.get_or_404(delivery_id)
    if current_user.id != company_id:
        abort(404)
    job = Job.query.get_or_404(job_id)
    if job.company_id != current_user.id:
        abort(404)

    db.session.delete(job)
    de.session.commit()
    flash('opening upgrade success', 'success')
    return redirect(url_for('company.admin_index', company_id=current_user.id))

