from flask import Blueprint , render_template, request, current_app, \
    redirect, url_for, flash

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
    comapny = User.query.get_or_404(company_id)
    if not company.is_comapny:
        abort(404)
    return render_template('company/detail.html', company=company,active='',panel='about')

@company.route('/<int:company_id>/jobs')
def company_jobs(company_id):
    company = User.query.get_or_404(company_id)
    if not company.is_company:
        abort(404)
    return render_template('company/detail.html', company=company,active='',panel='job')

