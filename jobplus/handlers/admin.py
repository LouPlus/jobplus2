from flask import Blueprint, render_template, request, current_app,\
    redirect, url_for, flash
from jobplus.decorators import admin_required
from jobplus.models import User, db, Job
from jobplus.forms import RegisterForm, UserEditForm, CompanyEditForm

#from jobplus.decorators import
#from jobplus.models import 
#from simpledu.forms import

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def index():

#    return 'hello world'
    return render_template('admin/index.html')

@admin.route('/users')
#@admin_required
def users():
#    page = request.args.get('page', default=1, type=int)
#    pagination = User.query.paginate(
#            page=page, 
#            per_page=current_app.config['ADMIN_PER_PAGE'],
#            error_out=False
#            )
#    return render_template('admin/user.html', pagination=pagination)
    return "ok"

@admin.route('/user/create_user', methods=['GET', 'POST'])
@admin_required
def create_user():
    form = RegisterForm()
    if form.is_submitted():
        form.create_user()
        flash('success the job is created ', 'success')
        return redirect(url_for('admin.user'))
    return render_template('admin/create_user.html', form=form)

@admin.route('/user/create_company', methods=['GET', 'POST'])
@admin_required
def create_company():
    form = RegisterForm()
    form.name.label = u'company name'
    if form.validate_on_submit():
        form.create_user()
        flash('company created successfully', 'success')
        return redirect(url_for('admin.users'))
    return render_template('admin/create_company.html', form=form)

@admin.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_user(user_id):

    user = User.query.get_or_404(user_id)

    if user.is_company:
        form = CompanyEditForm(obj=user)

    else:
        form = UserEditForm(obj=user)

    if form.validate_on_submit():
        form.update(user)
        flash('update successful', 'success')
        
        return redirect(url_for('admin.users'))
    if user.is_company:
        form.site.data = user.detail.site
        form.description.data = user.detail.description 
    return render_template('admin/edit_user.html', form=form,user=user)

@admin.route('/users/<int:user_id>/disable', methods=['GET', 'POST'])
@admin_required
def disable_user(user_id):
    user = User.query.get_or_404(user_id)

    if user.is_disable:
        user.is_disable = False
        flash('alread shutdown current user', 'success')
    else:
        user.is_disable = False
        flash('alread activate user', 'success')
    db.session.add(user)
    db.seesion.commit()

    return redirect(url_for('admin.users'))

@admin.route('/jobs')
@admin_required
def jobs():
#    page = request.args.get('page', default=1, type=int)
#    pagination = Job.query.paginate(
#            page=page,
#            per_page=current_app.config['ADMIN_PER_PAGE'],
#            error_out=False
#            )
#    return render_template('admin/jobs.html', pagination=pagination)
    return "Ok"

