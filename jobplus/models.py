from datetime import datetime 
from flask_sqlalchemy import SQLAlchemy
#from flask_login import UserMixin
#from werkzeug.security import generate_password_hash,
#check_password_hash



db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = 'True'

    created_at = db.Column(db.DateTime, default=datetime.utcnow)    
    updated_at = db.Column(db.DateTime, 
                            default=datetime.utcnow, 
                            onupdate=datetime.utcnow)

class User(Base):
    __tablename__ = 'user'

    #ROLE_USER = 10
    #ROLE_CMP = 20
    #ROLE_ADMIN = 30

    u_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True,\
                nullable=False)
    email = db.Column(db.String(32), unique=True, index=True,\
            nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)


#    @property
#    def url(self):
#        pass
    
#    @password.setter
#    def password(self, raw_passowrd):
        
        #self._password = generate_password_hash(orig_password)
#        pass

#    def check_password(self, password):
#        """判断用户输入的密码和存储哈希密码是否相等
#        """
        #return check_passowrd_hash(self._password, password)

#    def is_admin(self):
    
        # return self.role == self.ROLE_ADMIN
#       pass

#    def is_company(self):

        #return self.role == self.ROLE_COMPANY
#        pass

#    def __repr__(self):

#        return '<User:{}>'.format(self.name) 

class Company(Base):
    __tablename__ = "company"

    cmp_id = db.Column(db.Integer,primary_key=True)
    cmp_name = db.Column(db.String(256),nullable=False, index=True)
    cmp_logo = db.Column(db.String(256), index=True)
    cmp_website = db.Column(db.String(256), nullable=False,index=True)
    cmp_slogan = db.Column(db.String(64))
    cmp_address = db.Column(db.String(256))
    cmp_decription = db.Column(db.String(256))


class Job(Base):
    __tablename__ = "job"

    j_id = db.Column(db.Integer, primary_key=True)
    cmp_id = db.Column(db.Integer, db.ForeignKey('company.cmp_id'))
    j_title = db.Column(db.String(256), index=True)
    j_status = db.Column(db.Boolean, index=True)
    salary_range = db.Column(db.String(256), index=True)
    address = db.Column(db.String(256), index=True)
    j_description = db.Column(db.String(256), index=True)
    j_requirements = db.Column(db.String(256), index=True)

class Apply(Base):
    __tablename__ = "apply"

    a_id = db.Column(db.Integer, primary_key=True)
    j_id = db.Column(db.Integer, nullable=False)
    result = db.Column(db.Boolean) 


