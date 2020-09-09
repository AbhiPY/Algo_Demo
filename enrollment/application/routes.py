from application import app, db
from flask import render_template, request, Response, json, flash, redirect, session,url_for
from application.models import User
from application.forms import Loginform, Registration, DeleteUser

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template('index.html', index=True)

@app.route("/login", methods=['GET','POST'])
def login():
    if session.get("username"):
        return redirect('/index')
    
    form = Loginform()
    if form.validate_on_submit():
        email     = form.email.data
        password  = form.password.data

        user = User.objects(email=email).first() 
        if user and user.get_password(password):
            flash(f"{user.first_name}, You are successfully logged in!!","success")
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            return redirect("/user")
        else:
            flash("Something..went wrong!!","danger")
    return render_template('login.html',title='Login', form=form, login=True)

@app.route("/logout")
def logout():
    session['user_id'] = False
    session.pop("username",None)
    return redirect(url_for('index'))

@app.route("/register", methods=['POST','GET'])
def register():
    if session.get("username"):
        return redirect('/index')
    
    form = Registration()
    if form.validate_on_submit():
        user_id   = User.objects.count()
        user_id   += 1

        email       = form.email.data
        password    = form.password.data
        first_name  = form.first_name.data
        last_name   = form.last_name.data

        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash("You are successfully added","success")
        return redirect("/index")
    return render_template('register.html',title="Register", form=form)

@app.route('/user')
def user():
    user_delete = DeleteUser()
    users = User.objects.all()
    return render_template("user.html", users=users, title="User Details", delete=user_delete)

@app.route("/deleted_user", methods=['POST','GET'])
def deleted_user():
    val = request.form.get('option')
    user = User.objects.get(email=val)
    User.objects(email=val).delete()
    session.pop("username",None)
    return render_template("deleted_user.html", user=user, title="Deleted User Details")
   