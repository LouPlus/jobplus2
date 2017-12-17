from flask import Blueprint, render_template, request, current_app, \
    redirect, url_for, flash
#from jobplus.decorators import admin_required
#from jobplus.models import 
#from jobplus.forms import 


user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/')
def index():

    return "user html is doing ok"


