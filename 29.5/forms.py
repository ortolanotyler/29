from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    """Login Form"""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=20)],
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6, max=55)],
    )

class RegisterForm(FlaskForm):
    """User Registration Form"""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=20)],
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6, max=55)],
    )
    email = StringField(
        "Email Address",
        validators=[InputRequired(), Email(), Length(max=50)],
    )
    first_name = StringField(
        "First Name",
        validators=[InputRequired(), Length(max=30)],
    )
    last_name = StringField(
        "Last Name",
        validators=[InputRequired(), Length(max=30)],
    )

class FeedbackForm(FlaskForm):
    """Feedback Form"""

    title = StringField(
        "Feedback Title",
        validators=[InputRequired(), Length(max=100)],
    )
    content = StringField(
        "Feedback Content",
        validators=[InputRequired()],
    )

class DeleteForm(FlaskForm):
    """Deletion Confirmation Form"""
    pass