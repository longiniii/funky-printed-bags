from ext import db


class Contact(db.Model):
    __tablename__ = "contacts"

    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.String(), nullable=False, default=1)
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
    added_by = db.Column(db.Integer(), nullable=False)
    edited_by = db.Column(db.Integer(), nullable=False)
    colors = db.relationship("ProductColor", backref="product", lazy=True)
    images = db.relationship("ProductImage", backref="product", lazy=True)
    image_patterns = db.relationship("ProductImagePattern", backref="product", lazy=True)

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