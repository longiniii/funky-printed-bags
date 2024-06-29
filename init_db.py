from ext import app, db
from models import Product, ProductColor, ProductImage, ProductImagePattern, User, CartProduct

with app.app_context():
    db.drop_all()
    db.create_all()




    new_user = User(username='admin', email='admin@gmail.com', password='admin', role='admin')
    db.session.add(new_user)
    db.session.commit()
    new_user = User(username='guest', email='guest@gmail.com', password='guest', role='guest')
    db.session.add(new_user)
    db.session.commit()