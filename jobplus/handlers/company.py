from flask import Blueprint , render_template, request, current_app, \
    redirect, url_for, flash

from flask_login import login_required, current_user
from jobplus.forms import CompanyProfileForm, JobForm
from jobplus.models import User, Job, Delivery, db


company = Blueprint('company',__name__, url_prefix='/company')

@company.route('/')
def index():

    return render_template('cmp/cmp_front.html')
#    return "hollow"


@company.route('/profile/', methods=['GET', 'POST'])
@login_required
def profile():

    if not current_user.is_company:
        flash('Your are not comapany user', 'Warning')
        return redirect(url_for('front.index'))

    form = CompanyProfileForm(obj=current_user.comapny_detail)
    form.name.data = current_user.name
    form.name.data = current_user.email

    if form.validate_on_submit():
        form.updated_profile(current_user)
        flask('you have successful updated your info', 'success')

        return redirect(url_for('front.index'))
    return render_template('company/profile.html', form=form)


