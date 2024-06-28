from flask import render_template, request, redirect
from forms import RegistrationForm, LoginForm, PostingProduct, ContactForm, RatingForm
from ext import app, db, login_manager
from models import Contact, Product, ProductColor, ProductImage, ProductImagePattern, User, Cart, CartProduct, Review
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy import or_
from datetime import datetime


@app.context_processor
def global_variable():
    top_rated_products = Product.query.all()
    n = len(top_rated_products)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if get_products_average_rating(top_rated_products[j]) < get_products_average_rating(top_rated_products[j + 1]):
                top_rated_products[j], top_rated_products[j + 1] = top_rated_products[j + 1], top_rated_products[j]

    carts = Cart.query.all()
    return dict(top_rated_products=top_rated_products[:10],cart=carts)


@app.route("/")
def index():
    products = Product.query.all()
    return render_template("index.html", products=products)


@app.route("/post-a-product", methods=["GET", "POST"])
@login_required
def post_a_product():
    if current_user.role != 'admin':
        return redirect("/")
    product_posting_form = PostingProduct()
    if product_posting_form.validate_on_submit():
        colors = product_posting_form.colors.data.split(' ')
        images =  product_posting_form.images.data.split(' ')
        images_patterns = product_posting_form.images_patterns.data.split(' ')
        hasDiscount = False
        howMuchDiscount = None
        if product_posting_form.how_much_discount.data > 0:
            hasDiscount = True
            howMuchDiscount = product_posting_form.how_much_discount.data
        new_product = Product(
            name = product_posting_form.name.data, 
            cost = product_posting_form.cost.data, 
            how_much_discount = howMuchDiscount, 
            added_by = current_user.id, 
            edited_by = current_user.id)
        db.session.add(new_product)
        db.session.commit()
        for color in colors:
            new_color = ProductColor(color = color, product = new_product)
            db.session.add(new_color)
            db.session.commit()
        for image in images:
            new_image = ProductImage(image = image, product = new_product)
            db.session.add(new_image)
            db.session.commit()
        for image_pattern in images_patterns:
            new_image_pattern = ProductImagePattern(image_pattern = image_pattern, product = new_product)
            db.session.add(new_image_pattern)
            db.session.commit()
    return render_template("post-a-product.html", product_posting_form=product_posting_form)


def get_products_average_rating(product):
    average_rating = 0
    length = 0
    for review in product.reviews:
        average_rating += review.rating
        length += 1
    if length != 0:
        average_rating = average_rating / length
    return average_rating


@app.route("/product/<product_id>", methods=["GET", "POST"])
@login_required
def product_details(product_id):
    products = Product.query.all()
    product = Product.query.get(product_id)
    rating_form = RatingForm()
    average_rating = get_products_average_rating(product)
    if rating_form.validate_on_submit():
        product = Product.query.get(product_id)
        user = User.query.get(current_user.id)
        print(user)
        theReview = None
        if rating_form.review.data.strip() != '':
            theReview = rating_form.review.data
        new_review = Review(review = theReview,
                            rating = rating_form.rating.data,
                            date = datetime.now(),
                            product = product,
                            user = user,)
        db.session.add(new_review)
        db.session.commit()
    return render_template("product.html", products=products, product=product, average_rating=str(average_rating)[:3], rating_form=rating_form)


@app.route("/delete-product/<product_id>")
@login_required
def delete_product(product_id):
    if current_user.role != 'admin':
        return redirect("/")
    
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect("/")


@app.route("/edit-product/<product_id>", methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    if current_user.role != 'admin':
        return redirect("/")
    
    product = Product().query.get(product_id)
    colors = []
    images = []
    image_patterns = []
    for color in product.colors:
        colors.append(color.color)
    for image in product.images:
        images.append(image.image)
    for image_pattern in product.image_patterns:
        image_patterns.append(image_pattern.image_pattern)
    
    product_posting_form = PostingProduct(name = product.name, cost=product.cost, how_much_discount=product.how_much_discount, colors = " ".join(colors), images = " ".join(images), images_patterns = " ".join(image_patterns))
    if product_posting_form.validate_on_submit():
        colors = product_posting_form.colors.data.split(' ')
        images =  product_posting_form.images.data.split(' ')
        images_patterns = product_posting_form.images_patterns.data.split(' ')
        hasDiscount = False
        howMuchDiscount = None
        if product_posting_form.how_much_discount.data > 0:
            hasDiscount = True
            howMuchDiscount = product_posting_form.how_much_discount.data
        product.name = product_posting_form.name.data
        product.cost = product_posting_form.cost.data
        product.how_much_discount = howMuchDiscount
        product.added_by = product.id
        product.edited_by = current_user.id
        # delete
        for color in product.colors:
            db.session.delete(color)
        for image in product.images:
            db.session.delete(image)
        for image_pattern in product.image_patterns:
            db.session.delete(image_pattern)
        
        # add
        for color in colors:
            product.colors.append(ProductColor(color = color, product = product))
        for image in images:
            product.images.append(ProductImage(image = image, product = product)) 
        for image_pattern in images_patterns:
            product.image_patterns.append(ProductImagePattern(image_pattern = image_pattern, product = product))
        db.session.commit()
    return render_template('edit-product.html', product_posting_form=product_posting_form)

@app.route("/gift-card")
def gift_card():
    return render_template("gift-card.html")


@app.route("/gift-card-checkout")
def gift_card_checkout():
    return render_template("gift-card-checkout.html")


@app.route("/contact", methods=["GET", "POST"])
@login_required
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        new_contact = Contact(
            user = current_user.id,
            first_name=contact_form.first_name.data, 
            last_name=contact_form.last_name.data, 
            email=contact_form.email.data,
            phone=contact_form.phone.data,
            subject=contact_form.subject.data,
            message=contact_form.message.data)
        db.session.add(new_contact)
        db.session.commit()
    return render_template("contact.html", contact_form=contact_form)


@app.route("/view-contacts")
@login_required
def view_contacts():
    if current_user.role != 'admin':
        return redirect("/")
    
    contacts = Contact.query.all()
    return render_template("view-contacts.html", contacts=contacts)


@app.route("/delete-contact/<contact_id>")
def delete_contact(contact_id):
    if current_user.role != 'admin':
        return redirect("/")
    
    contact = Contact.query.get(contact_id)
    db.session.delete(contact)
    db.session.commit()
    return redirect("/view-contacts")


@app.route("/sign-up", methods=["GET","POST"])
def sign_up():
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        if (User.query.filter(registration_form.username.data == User.username).first() == None):
            new_user = User(username=registration_form.username.data, email=registration_form.email.data, password=registration_form.password.data)
            #new_cart = Cart(user_id=new_user.id)
            db.session.add(new_user)
            #db.session.add(new_cart) mere daaaaaaaaaaaaaaaaaaaamateeeeeeeeeeeee
            db.session.commit()
            return redirect("/")
    return render_template("sign-up.html", registration_form=registration_form)


@app.route("/log-in" , methods=["GET", "POST"])
def log_in():
    log_in_form = LoginForm()
    if log_in_form.validate_on_submit():
        user = User.query.filter(or_(log_in_form.username_or_email.data == User.username, log_in_form.username_or_email.data == User.email)).first()
        if (user != None) & User.check_password(user, log_in_form.password.data):
            login_user(user)
            return redirect("/")
    return render_template("log-in.html", log_in_form=log_in_form)


@app.route("/log-out")
@login_required
def log_out():
    logout_user()
    return redirect("/")

@app.route("/api/add-to-cart", methods=['POST'])
@login_required
def add_to_cart():
    post_data = request.get_json()
    print(post_data['productQuantity'])
    new_cart_product = CartProduct(product_id=post_data['productId'], quantity=post_data['productQuantity'], cart_id=current_user.id)
    db.session.add(new_cart_product)
    db.session.commit()
    return 'the product has been added, slay!'

@app.route("/api/delete-review/<user_id>/<review_id>", methods=["DELETE"])
@login_required
def delete_review(user_id, review_id):
    if current_user.id == user_id or current_user.role == "admin":
        print(review_id)
        theReviewToBeDeleted = Review.query.get(review_id)
        db.session.delete(theReviewToBeDeleted)
        db.session.commit()
        return "the review has been deleted"
    return "current user can't delete the review"
