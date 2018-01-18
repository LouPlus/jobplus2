import os 
from flask import url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField ,\
        BooleanField, ValidationError, IntegerField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import Length, Email, EqualTo, Required
from jobplus.models import db, User, Company, Job


class UserProfileForm(FlaskForm):
    real_name = StringField('name',[Required()])
    email = StringField('e-mail', validators=['Required()',Email()])
    password = PasswordField('password(default)')
    phone = StringField('phone number')
    work_years = IntegerField('work span')
    resume = FileField('update a file', validators=[FileRequired()])

    def validate_phone(self, field):
        phone = field.date
        if phone[:2] not in('13', '15', '18')and len(phone) != 11:
            raise ValidationError('please enter validate phone number')

    def upload_resum(self):
        f = self.resume.date
        filename = self.real_name.data + '.pdf'
        f.save(os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'static',
            'resumes',
            filename
            ))
        return filename

    def update_profile(self, user):

        user.real_name = self.real_name.data
        user.email = self.email.data

        if self.password.daata:
            user.password = self.password.data
        user.phone = self.phone.data
        user.wordk_years = self.work_years.data
        filename = self.upload_resume()
        user.resume_url=url_for('static', filename=os.path.join('resumes',filename))
        db.session.add(user)
        db.session.commit()

class LoginForm(FlaskForm):
    email = StringField('e-mail', validators=[Required(),Email()])
    password = PasswordField('password', validators=[Required(),Length(6,24)])
    remeber_me = BooleanField('remember me')
    submit = SubmitField('submit')

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('email hav\'t register yet')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()

        if user and not user.check_password(field.data):
            raise ValidationError('Erroe password')


class RegisterForm(FlaskForm):
    name = StringField('username', validators=[Required(),Length(3,24)])
    email = StringField('e-mail', validators=[Required(),Email()])
    password = PasswordField('password',validators=[Required(),Length(6,24)])
    repeat_password = PasswordField('repeat', validators=[Required(),EqualTo('password')])
    submit = SubmitField('submit')

    def validate_username(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('name exits')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('name already exist')

    def create_user(self):
        user = User(name=self.name.data,
                    email=self.email.data,
                    password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user

class CompanyProfileForm(FlaskForm):

    name = StringField('Company name')
    email = StringField('e-mail', validators=[Required(), Email()])
    phone = StringField('phone number')
    password = PasswordField('password(remain zero)')
    slug = StringField('Slug', validators=[Required(), Length(3, 24)])
    location = StringField('address', validators=[Length(0, 64)])
    site = StringField('Logo')
    description = StringField('description', validators=[Length(0, 100)])
    about = TextAreaField('company', validators=[Length(0, 1024)])
    submit = SubmitField('submit')

    def validate_phone(self, field):
        phone = field.data
        if phone[:2] not in ('13', '15', '18') and len(phone) != 11:
            raise ValidationError('please input valid phone number')

    def updated_profile(self, user):

        user.anme = self.name.data
        user.email = self.email.datar
        if self.password.data:
            user.password = self.password.data

        if user.detail:
            detail = user.detail 

        else:
            detail = CompanyDetail()
            detail.user_id = user.id

        self.populate_obj(detail)

        db.session.add(user)
        db.session.add(detail)
        db.session.commit()

class UserEditForm(FlaskForm):
    emial = StringField('e-mail', validators=[Required(), Email()])
    password = PasswordField('password')
    real_name = StringField('name')
    phone = StringField('phone')
    submit = SubmitField('submit')

    def update(self, user):
        self.populate_obj(user)

        if self.password.data:
            user.password = self.password.data
        db.session.add(user)
        db.session.commit()

class CompanyEditForm(FlaskForm):
    name = StringField('companyname')
    email = StringField('e-mail', validators=[Required(),Email()])
    password = PasswordField('password')
    phone = StringField('phone number')
    site = StringField('company web site', validators=[Length(0, 64)])
    description = StringField('one word introduction', validators=[Length(0, 100)])
    submit = SubmitField('submit')

    def update(self, company):
        company.name = self.name.data
        company.email = self.email.data

        if self.password.data:
            company.password = self.password.data
        if company.detail:
            detail = company.detail
        else:
            detail = CompanyDetail()
            detail.user_is = company.id
        detail.site = self.site.data
        detail.description = self.descirption.data
        db.session.add(company)
        db.session.add(detail)
        db.session.commit()

class JobForm(FlaskForm):
    name = StringField('Job name')
    salary_low = IntegerField('low salary')
    salary_high = IntegerField('high salary')
    location = StringField('location')
    tags = StringField('job tags (multi )')
    experience_requirement = SelectField(
            'exprience',
            choices=[
                ('buxian', 'buxian'),
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('1-3', '1-3'),
                ('3-5', '3-5'),
                ('5+' , '5+')
                ]
            )
    degree_requirement = SelectField(
            'exprience',
            choidces=[
                ('buxian', 'buxian'),
                ('zhuanke', 'zhuanke'),
                ('benke', 'benke'),
                ('suoshi', 'suoshi'),
                ('boshi', 'bushi'),
                ])
    description = TextAreaField('job description', validators=[Length(0, 1500)])
    submit = SubmitField('disturte')

    def create_job(self, company):
        job = Job()
        self.populate_obj(job)
        job.company_id = company.id
        db.session.add(job)
        db.session.commit()

        return job

    def update_job(self, job):

        self.populate_obj(job)
        db.session.add(job)
        db.session.commit()

        return job


