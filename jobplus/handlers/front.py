from flask import Blueprint, render_template, redirect, url_for, flash, \
        request, current_app
from jobplus.models import User, db
from jobplus.forms import RegisterForm ,LoginForm
from flask_login import login_user, logout_user, login_required

# from job.models import 
# from job.forms import 
# from flask_login import 

front = Blueprint('front', __name__)

@front.route('/')
def index():

    return render_template('index.html')
#    return 'hollo world'



@front.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
#    if form.validate_on_submit():
#        user = User.query.filter_by(email=form.email.data).first()
#        if user.is_disable:
#            flask('user is disabel')
#            return redirect(url_for('front.login'))
#        else:
#            login_user(user, form.remeber_me.data)
#            next = 'user.profile'
#
#            if user.is_admin:
#                next = 'admin.index'
#            elif user.is_company:
#                next = 'company.profile'
    return render_template('login.html', form=form)

