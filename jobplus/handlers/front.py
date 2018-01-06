from flask import Blueprint, render_template, redirect, url_for, flash, \
        request, current_app
from jobplus.models import User, db, Job, Company
from jobplus.forms import RegisterForm ,LoginForm
from flask_login import login_user, logout_user, login_required

# from job.models import 
# from job.forms import 
# from flask_login import 

front = Blueprint('front', __name__)

@front.route('/')
def index():

    newest_jobs = Job.query.filter(Job.is_disable.is_(False))\
            .order_by(Job.created_at.desc()).limit(9)

    newest_companies = User.query.filter(
            User.role == User.ROLE_COMPANY
            ).order_by(User.created_at.desc()).limit(8)
    
    return render_template(
            'index.html',
            active = 'index',
            newest_jobs = newest_jobs,
            newest_companies=newest_companies
            )

#    return render_template('index.html')
#    return 'hollo world'



@front.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.is_disable:
            flask('user is disabel')
            return redirect(url_for('front.login'))
        else:
            login_user(user, form.remeber_me.data)
            next = 'user.profile'

            if user.is_admin:
                next = 'admin.index'
            elif user.is_company:
                next = 'company.profile'
    return render_template('login.html', form=form)

@front.route('/userregister',methods=['GET', 'POST'])
def user_register():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('regiser successful, please login', 'success')

        return redirect(url_for('.login'))
    return render_template('user_register.html', form=form)

@front.route('/companyregister', methods=['GET','POST'])
def company_register():
    form = RegisterForm()
    form.name.label = u'company name'

    if form.validate_on_submit():

        company_user = form.create_user()
        company_user.role = User.ROLE_COMPANY

        db.session.add(company_user)
        db.session.commit()

        flash('regiser , ok', 'success')
        return redirectr(url_for('.loing'))
    return render_template('company_register.html', form=form)

