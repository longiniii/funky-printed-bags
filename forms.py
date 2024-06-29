from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, IntegerField, TextAreaField, RadioField
from wtforms.validators import data_required, length, equal_to, optional


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[data_required(message="Username is required")])
    email = StringField("Email", validators=[data_required(message="Email is required")])
    password = PasswordField("Password", validators=[data_required(message="Password is required"), length(min=8, max=64, message="the password's length must be between 8 and 64 characters")])
    repeat_password = PasswordField("Repeat Password", validators=[equal_to("password", message="the passwords should be the same")])
    submit = SubmitField("Sign up")


class LoginForm(FlaskForm):
    username_or_email= StringField("Username or Email", validators=[data_required(message="an Username or an Email is required")])
    password = PasswordField("Password",  validators=[data_required(message="Password is required")])


class PostingProduct(FlaskForm):
    name = StringField("products name   (name)", validators=[data_required(message="Products name is required")])
    cost = IntegerField("products price   (num)", validators=[data_required(message="Products price is required")])
    how_much_discount = IntegerField("products discount, in % percentages   (num)")
    colors = StringField("products colors   (color1, color2, color3...)", validators=[data_required(message="Products color is required")])
    images = StringField("products images   (url1, url2, url3...)", validators=[data_required(message="Products image is required")])
    images_patterns = StringField("products image patterns   (url1, url2, url3...)", validators=[data_required(message="Products image pattern is required")])
    submit = SubmitField("Submit")


class ContactForm(FlaskForm):
    first_name = StringField("first name*", validators=[data_required(message="first name is required")])
    last_name = StringField("last name*", validators=[data_required(message="last name required")])
    email = StringField("email*", validators=[data_required(message="email is required")])
    phone = IntegerField("phone", validators=[optional()])
    subject = StringField("subject*", validators=[data_required("subject is required")])
    message = TextAreaField("message*", validators=[data_required(message="message is required")])
    submit = SubmitField("Submit")


class RatingForm(FlaskForm):
    review = TextAreaField("leave a review")
    rating = RadioField(choices=[(1, ''), (2, ''), (3, ''), (4, ''), (5, '')], validators=[data_required()])
    submit = SubmitField("Rate")
