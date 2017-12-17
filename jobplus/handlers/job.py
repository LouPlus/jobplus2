from flask import Blueprint, render_template, request, current_app, \
    redirect, url_for, flash

#from jobplus.decorators import admin_required
#from jobplus.models import
#from jobplus.forms import 


job = Blueprint('job',__name__, url_prefix='/job')

@job.route('/')
def index():

    return "job is doing fine "


