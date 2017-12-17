from flask import Blueprint , render_template, request, current_app, \
    redirect, url_for, flash

#from jobplus.decorators import admin_required
#from jobplus.models import 
#from jobplus.form import ..

company = Blueprint('company',__name__, url_prefix='/company')

@company.route('/')
def index():

    return " company html is doing ok"


