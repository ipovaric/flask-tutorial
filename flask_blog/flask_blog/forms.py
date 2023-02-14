from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_blog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
        validators=[DataRequired(message='Username Data Invalid'),Length(min=2,max=20)])
    email = StringField('Email',
        validators=[DataRequired(message='Email Data Invalid'),Email(message='Email Invalid')])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
        validators=[DataRequired(message='PW Data Invalid'),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is taken. Please choose a different one')
    
    

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
