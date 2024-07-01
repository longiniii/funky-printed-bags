from flask_login import UserMixin
from ext import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash


class Contact(db.Model):
    __tablename__ = "contacts"

    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.String(), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    phone = db.Column(db.Integer(), nullable=True)
    subject = db.Column(db.String(), nullable=False)
    message = db.Column(db.String(), nullable=False)


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    cost = db.Column(db.Integer(), nullable=False)
    how_much_discount = db.Column(db.Integer())
    discounted_cost = db.Column(db.Integer())
    added_by = db.Column(db.Integer(), nullable=False)
    edited_by = db.Column(db.Integer(), nullable=False)
    colors = db.relationship("ProductColor", backref="product", lazy=True)
    images = db.relationship("ProductImage", backref="product", lazy=True)
    image_patterns = db.relationship("ProductImagePattern", backref="product", lazy=True)
    reviews = db.relationship("Review", backref="product", lazy=True)

class ProductColor(db.Model):
    __tablename__ = "product_colors"

    id = db.Column(db.Integer(), primary_key=True)
    color = db.Column(db.String())
    product_id = db.Column(db.Integer(), db.ForeignKey("products.id"))

class ProductImage(db.Model):
    __tablename__ = "product_images"

    id = db.Column(db.Integer(), primary_key=True)
    image = db.Column(db.String(), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))

class ProductImagePattern(db.Model):
    __tablename__ = "product_image_patterns"

    id = db.Column(db.Integer(), primary_key=True)
    image_pattern = db.Column(db.String(), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    role = db.Column(db.String(), nullable=True)
    cart_products = db.relationship("CartProduct", backref="user", lazy=True)
    reviews = db.relationship("Review", backref="user", lazy=True)
    found_helpfuls = db.relationship("FoundReviewHelpful", backref="user", lazy=True)

    def __init__(self, username, email, password, role='guest'):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role
    def check_password(self, password):
        return check_password_hash(self.password,password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class CartProduct(db.Model):
    __tablename__ = "cart_products"

    id = db.Column(db.Integer(), primary_key=True)
    product_id = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"))
    quantity = db.Column(db.Integer(), nullable=False)


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer(), primary_key=True)
    review = db.Column(db.String(), nullable=True)
    rating = db.Column(db.Integer(), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    product_id = db.Column(db.Integer(), db.ForeignKey("products.id"))
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"))
    found_helpfuls = db.relationship("FoundReviewHelpful", backref="review", lazy=True)


class FoundReviewHelpful(db.Model):
    __tablename__ = "foundReviewHelpfuls"

    id = db.Column(db.Integer(), primary_key=True)
    found_helpful = db.Column(db.Boolean(), nullable=False)
    review_id = db.Column(db.Integer(), db.ForeignKey("reviews.id"))
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"))