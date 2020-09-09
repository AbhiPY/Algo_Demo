from flask_wtf import FlaskForm
from wtforms import BooleanField,SubmitField,PasswordField,StringField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from application.models import User

class Loginform(FlaskForm):
    email       = StringField('Email', validators=[DataRequired(), Email()])
    password    = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=15)])
    remember_me = BooleanField('Keep Login')
    submit      = SubmitField("Login")

class Registration(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=15)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(),Length(min=6,max=15),EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(),Length(min=2,max=100)])
    last_name = StringField("Last Name", validators=[DataRequired(),Length(min=2,max=100)])
    submit    = SubmitField("Register Now")

    def validate_email(self,email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use.Pick another one!!")

class DeleteUser(FlaskForm):
    submit    = SubmitField("Delete User")


