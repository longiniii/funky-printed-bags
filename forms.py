from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, EmailField, SubmitField, IntegerField, BooleanField
from wtforms.validators import data_required, length, email, equal_to


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[data_required(message="Username is required")])
    email = EmailField("Email", validators=[data_required(message="Email is required")])
    password = PasswordField("Password", validators=[data_required(message="Password is required"), length(min=8, max=64, message="the password's length must be between 8 and 64 characters")])
    repeat_password = PasswordField("Repeat Password", validators=[equal_to("password", message="the passwords should be the same")])
    submit = SubmitField("Sign up")


class PostingProduct(FlaskForm):
    name = StringField("products name", validators=[data_required(message="Products name is required")])
    cost = IntegerField("products price", validators=[data_required(message="Products price is required")])
    how_much_discount = IntegerField("products discount, in % percentages")
    colors = StringField("products colors  (separate each with a space)", validators=[data_required(message="Products color is required")])
    images = StringField("products images  (separate each with a space)", validators=[data_required(message="Products image is required")])
    images_patterns = StringField("products image patterns (separate each with a space)", validators=[data_required(message="Products image pattern is required")])
    submit = SubmitField("Submit")
