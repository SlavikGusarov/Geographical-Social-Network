from flask_sqlalchemy import SQLAlchemy
import datetime
#To set database up
#from flask import Flask
#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:aist2371@localhost/gsn'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
#db = SQLAlchemy(app)
db = SQLAlchemy()


# Here should be defined all models
class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20))
    email = db.Column(db.String(50))
    password = db.Column(db.String(160))
    activation_link = db.Column(db.String(20))

class UsersInfo(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(30))
    sex = db.Column(db.String(6))
    country = db.Column(db.String(30))
    city= db.Column(db.String(30))
    date = db.Column(db.Date)
    telephone = db.Column(db.String(15))
    about = db.Column(db.String(200))
    ava_ref = db.Column(db.String(100))

    user = db.relationship('Users', backref=db.backref('UsersInfo', lazy=True))

class Posts(db.Model):
	post_id = db.Column(db.Integer, primary_key=True)
	author_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
	title = db.Column(db.String(150))
	lat = db.Column(db.Float)
	lng = db.Column(db.Float)
	privacy = db.Column(db.Integer)
	description = db.Column(db.Text)

	author = db.relationship('Users', backref=db.backref('Posts', lazy=True))

class Chat(db.Model):
    chat_id = db.Column(db.Integer, primary_key=True)
    member = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    chat_name = db.Column(db.String(150))
    memb = db.relationship('Users', backref=db.backref('Chat', lazy=True))


class Massages(db.Model):
    massage_id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))    
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.chat_id'))
    text = db.Column(db.Text) 
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    author = db.relationship('Users', backref=db.backref('Massages', lazy=True))

# To Create databese like this run this:
# db.create_all()
# Таня, возможно чтобы поднять на heroku такую бд нужно раскоментить строчку и запустить проект. Вдруг сработает