from flask import render_template, redirect, request, url_for, session
from ronggoAdmin.admin import blueprint
from ronggoAdmin.models import models
from ronggoAdmin import db

@blueprint.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')



    return render_template('login.html')

@blueprint.route('/register',methods=['GET','POST'])
def register():
    if request.method == "GET":
         return render_template('register.html')
    else:

        nama = request.form.get('nama')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')   
        
        data = models.Admin(
            nama = nama,
            username = username,
            password = password,
            email = email

        )
        db.session.add(data)
        db.session.commit()

        return redirect(url_for('base_bluprint.login'))
   
    