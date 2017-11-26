import os
import smtplib
import random
import string
from flask_mail import Mail, Message
from flask import Flask, render_template, request, g, redirect, session, url_for,json,jsonify, Blueprint
from flask_mysqldb import MySQL
from werkzeug import check_password_hash, generate_password_hash
import random
import string
from MySQLdb.cursors import DictCursor
from flask_uploads import UploadSet, configure_uploads, IMAGES
# Database
from GSN import database

mod = Blueprint('profile', __name__, template_folder='templates')
UPLOADED_PHOTOS_DEST = 'static/img/user'

@mod.route("/myprofile", methods = ['POST'])
def myprofpost():
    if g.user is None:
        return redirect(url_for('login.login'))

    user = database.Users.query.filter_by(user_id=g.user.user_id).first()
    user_info = database.UsersInfo.query.filter_by(user_id=g.user.user_id).first()

    user.name = request.form.get("name")
    user_info.surname = request.form.get("surname")
    user.email = request.form.get("email")
    user_info.sex = request.form.get("sex")
    user_info.country = request.form.get("country")
    user_info.city = request.form.get("city")
    user_info.date = request.form.get("date")
    user_info.telephone = request.form.get("telephone")
    user_info.about = request.form.get("about")
    
    #print('Surname:', user_info.surname)
    database.db.session.commit()
    return redirect(url_for('profile.myprofget'))

    

@mod.route("/myprofile", methods = ['GET'])
def myprofget():
    if g.user is None:
        return redirect(url_for('login.login'))
    user = database.Users.query.filter_by(user_id=g.user.user_id).first()
    user_info = database.UsersInfo.query.filter_by(user_id=g.user.user_id).first()
    if user_info.ava_ref is not None:
        ref_ava = UPLOADED_PHOTOS_DEST + '/' + user_info.ava_ref
    else:
        ref_ava = 'static/img/avatar.png'
    return render_template('MyProfileSettings.html', ava=ref_ava, name=user.name, surname=user_info.surname, email=user.email, country=user_info.country, city=user_info.city,date=user_info.date,sex=user_info.sex,telephone=user_info.telephone, about=user_info.about)

        
@mod.route('/upload', methods=['POST'])
def upload():
    if 'photo' in request.files:
        user_info = database.UsersInfo.query.filter_by(user_id=g.user.user_id).first()
        if user_info.ava_ref is not None:
            os.remove(UPLOADED_PHOTOS_DEST + '/' + g.user.user_info)

        fname = g.photo.save(request.files['photo'])

        #appending random prefix to name of the file to prevent name collision
        rand_prefix = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(15))
        os.rename(UPLOADED_PHOTOS_DEST + '/' + fname, UPLOADED_PHOTOS_DEST + '/' + rand_prefix + fname) 
        user_info.ava_ref = rand_prefix + fname
        database.db.session.commit()
        return redirect(url_for('profile.myprofile'))


# @mod.route('/upload', methods=['POST'])
# def upload():
#    if 'photo' in request.files:
#        cur_id = g.user['user_id']
#        cur = mysql.connection.cursor()
       
#        #if user already has an avatar - delete
#        if (g.user['ava_ref'] is not None):
#            os.remove(mod.config['UPLOADED_PHOTOS_DEST'] + '/' + g.user['ava_ref'])

#        fname = photos.save(request.files['photo'])
#        #appending random prefix to name of the file to prevent name collision
#        rand_prefix = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
#        os.rename(mod.config['UPLOADED_PHOTOS_DEST'] + '/' + fname, 
#                  mod.config['UPLOADED_PHOTOS_DEST'] + '/' + rand_prefix + fname)
       
#        cur.execute('''UPDATE users SET ava_ref = %s WHERE user_id = %s''', (rand_prefix + fname, cur_id))
#        mysql.connection.commit()
#    return redirect(url_for('myprofget'))

