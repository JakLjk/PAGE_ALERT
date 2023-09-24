from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import Integer, String, DateTime, Text


class User(db.Model, UserMixin):
    id = db.Column(Integer, primary_key=True)
    # login credentials
    email = db.Column(String(150), unique=True)
    password = db.Column(String(150),)
    # One user can have many alert processes [One-To-Many]
    user_process = db.relationship('UserProcess',
                                back_populates='user')

    
class UserProcess(db.Model):
    id = db.Column(Integer, primary_key=True)
    # One user can have many alert processes
    user_id = db.Column(Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', 
                           back_populates='user_process')
    # Columns with informations about alert
    alert_name = \
        db.Column(String)
    alert_status = \
        db.Column(String)
    element_comparison_identifier = \
        db.Column(String, )
    element_comparison_type = \
        db.Column(String)
    refresh_interval_period_type = \
        db.Column(String)
    refresh_interval_value = \
        db.Column(Integer)
    last_refresh_time = \
        db.Column(DateTime)
    webpage_link = \
        db.Column(String)
    initial_raw_data = \
        db.Column(Text)