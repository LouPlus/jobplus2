from flask import Blueprint, render_template, request, current_app, \
    redirect, url_for, flash
from flask_login import login_required, current_user
from jobplus.forms import UserProfileForm


user = Blueprint('user', __name__, url_prefix='/user')



@user.route('/', methods=['GET','POST'])
@login_required
def profile():

    form = UserProfileForm(obj=current_user)

    if form.validate_on_submit():
        form.update_profile(current_user)

        flash('you have successfully updated your personal inf','success')
        return redirect(url_for('front.index'))
    return render_template('user/profile.html', form=form)

    return 'profile routing is doing ok '

