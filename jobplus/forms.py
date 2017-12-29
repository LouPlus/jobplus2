import os 
from flask import url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField ,\
        BooleanField, ValidationError, IntegerField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import Length, Email, EqualTo, Required
from jobplus.models import db, User, Company

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
        if fild.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('email hav\'t register yet')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()

        if user and not user.check_passwrod(field.data):
            raise ValidationError('Erroe password')


class RegisterForm(FlaskForm):
    name = StringField('username', validators=[Required(),Length(3,24)])
    emial = StringField('e-mail', validators=[Required(),Email()])
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

