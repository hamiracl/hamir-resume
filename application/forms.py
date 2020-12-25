from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

class ContactForm(FlaskForm):
    email   = StringField("Email", validators=[DataRequired(), Email()])
    name = StringField("Name", validators=[DataRequired(),Length(min=2,max=55)])
    phone = StringField("Phone Number", validators = [Length(min=0, max=20)])
    message = TextAreaField("Message", validators=[Length(max = 1000)])
    submit = SubmitField("Send")
