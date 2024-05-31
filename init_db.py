from ext import app, db
from models import Product, ProductColor, ProductImage, ProductImagePattern

with app.app_context():
    db.drop_all()
    db.create_all()
    # image_patterns=['https://static.wixstatic.com/media/45d10e_35c84fb1d48540f1886b2ceb7a342c37~mv2_d_3500_1968_s_2.jpg/v1/fill/w_541,h_541,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/45d10e_35c84fb1d48540f1886b2ceb7a342c37~mv2_d_3500_1968_s_2.jpg']
    # product1 = Product(name="Camouflage",cost=27,how_much_discount=None)
    # color1 = ProductColor(color='Orange', product=product1)
    # color2 = ProductColor(color='Pink', product=product1)
    # image1 = ProductImage(image='https://static.wixstatic.com/media/45d10e_dd5d9543998c4c0f9ecf120fac20ffb0~mv2.jpg/v1/fill/w_625,h_625,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/45d10e_dd5d9543998c4c0f9ecf120fac20ffb0~mv2.jpg', product=product1)
    # image2 = ProductImage(image='https://static.wixstatic.com/media/45d10e_d6445cbc0df2428d9348c3a7639dbed8~mv2.jpg/v1/fill/w_625,h_625,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/45d10e_d6445cbc0df2428d9348c3a7639dbed8~mv2.jpg', product=product1)
    # image_pattern1 = ProductImagePattern(image_pattern='https://static.wixstatic.com/media/45d10e_35c84fb1d48540f1886b2ceb7a342c37~mv2_d_3500_1968_s_2.jpg/v1/fill/w_541,h_541,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/45d10e_35c84fb1d48540f1886b2ceb7a342c37~mv2_d_3500_1968_s_2.jpg', product=product1)
    # db.session.add_all(product1, color1, color2, image1, image2, image_pattern1)
    # db.session.commit()