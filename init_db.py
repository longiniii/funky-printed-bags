from ext import app, db
from models import *
from productsData import data

with app.app_context():
    db.drop_all()
    db.create_all()




    new_user = User(username='admin', email='admin@gmail.com', password='admin', role='admin')
    db.session.add(new_user)
    db.session.commit()
    new_user = User(username='guest', email='guest@gmail.com', password='guest', role='guest')
    db.session.add(new_user)
    db.session.commit()

    for product in data:
        new_product = Product(name=product['name'],cost=product['cost'], how_much_discount=product['howMuchDiscount'], added_by=1,edited_by=1)
        db.session.add(new_product)
        db.session.commit()
        for color in product['colors']:
            new_color = ProductColor(color=color, product=new_product)
            db.session.add(new_color)
            db.session.commit()
        for image in product['images']:
            new_image = ProductImage(image=image, product=new_product)
            db.session.add(new_image)
            db.session.commit()
        for image_pattern in product['images_patterns']:
            new_image_pattern = ProductImagePattern(image_pattern=image_pattern, product=new_product)
            db.session.add(new_image_pattern)
            db.session.commit()