from datetime import datetime 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class base(db.Model):
    __tabelname__ = 'base'


