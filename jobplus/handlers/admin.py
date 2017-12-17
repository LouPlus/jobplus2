from flask import Blueprint, render_template, request, current_app,\
    redirect, url_for, flash

#from jobplus.decorators import
#from jobplus.models import 
#from simpledu.forms import

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def index():

    return 'hello world'


