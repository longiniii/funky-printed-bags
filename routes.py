from flask import render_template, request, redirect
from forms import RegistrationForm, LoginForm, PostingProduct, ContactForm, RatingForm
from ext import app, db, login_manager
from models import Contact, Product, ProductColor, ProductImage, ProductImagePattern, User, CartProduct, Review, FoundReviewHelpful
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy import or_
from datetime import datetime


@app.context_processor
def global_variable():
    cart = []
    if current_user.is_authenticated:
        for product in current_user.cart_products:
            cart.append([Product.query.get(product.product_id), product.quantity, product.id])

    top_rated_products = Product.query.all()
    n = len(top_rated_products)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if get_products_average_rating(top_rated_products[j]) < get_products_average_rating(top_rated_products[j + 1]):
                top_rated_products[j], top_rated_products[j + 1] = top_rated_products[j + 1], top_rated_products[j]
    top_rated_products = list(filter(lambda n: float(get_products_average_rating(n)) > 0, top_rated_products))
    return dict(top_rated_products=top_rated_products[:10], the_average_rating=get_products_average_rating, cart=cart)


@app.route("/")
def index():
    searchterm = request.args.get('search')
    page = request.args.get("page")
    if page == None:
        page = 1
    else:
        page = int(page)
    products_length = 0
    if searchterm != None:
        products = Product.query.filter(Product.name.contains(searchterm.lower()))
        products_length = len(list(products))
    else:
        products = Product.query.all()
        products_length = len(products)
    return render_template("index.html", products=products[(page - 1) * 12 : page * 12], products_length = products_length)


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
        discountedCost = None
        if product_posting_form.how_much_discount.data > 0:
            hasDiscount = True
            howMuchDiscount = product_posting_form.how_much_discount.data
            discountedCost = product_posting_form.cost.data - (product_posting_form.cost.data * (product_posting_form.how_much_discount.data / 100))
        new_product = Product(
            name = product_posting_form.name.data, 
            cost = product_posting_form.cost.data, 
            how_much_discount = howMuchDiscount, 
            discounted_cost = discountedCost,
            added_by = current_user.id, 
            edited_by = current_user.id
            )
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
        average_rating += int(review.rating)
        length += 1
    if length != 0:
        average_rating = average_rating / length
    return str(average_rating)[:3]


@app.route("/product/<product_id>", methods=["GET", "POST"])
@login_required
def product_details(product_id):
    products = Product.query.all()
    product = Product.query.get(product_id)
    rating_form = RatingForm()
    if rating_form.validate_on_submit():
        product = Product.query.get(product_id)
        user = User.query.get(current_user.id)
        review = None
        for userRev in user.reviews:
            for prodRev in product.reviews:
                if prodRev.id == userRev.id:
                    review = Review.query.get(prodRev.id)
                    break
            if (review != None):
                break
        theReview = None
        if rating_form.review.data.strip() != '':
            theReview = rating_form.review.data
        if review == None:
            new_review = Review(review = theReview,
                            rating = rating_form.rating.data,
                            date = datetime.now(),
                            product = product,
                            user = user)
            db.session.add(new_review)
            db.session.commit()
        else:
            review.review = theReview
            review.rating = rating_form.rating.data
            review.date = datetime.now()
            review.product = product
            review.user = user
            db.session.commit()


    return render_template("product.html", products=products, product=product, rating_form=rating_form)


@app.route("/delete-product/<product_id>")
@login_required
def delete_product(product_id):
    if current_user.role != 'admin':
        return redirect("/")
    
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    for cart_product in CartProduct.query.all():
        if cart_product.product_id == product.id:
            db.session.delete(CartProduct.query.get(cart_product.id))
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
        discountedCost = None
        if product_posting_form.how_much_discount.data > 0:
            hasDiscount = True
            howMuchDiscount = product_posting_form.how_much_discount.data
            discountedCost = product_posting_form.cost.data - (product_posting_form.cost.data * (product_posting_form.how_much_discount.data / 100))
        product.name = product_posting_form.name.data
        product.cost = product_posting_form.cost.data
        product.how_much_discount = howMuchDiscount
        product.discounted_cost = discountedCost
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
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect("/")
    return render_template("sign-up.html", registration_form=registration_form)


@app.route("/log-in" , methods=["GET", "POST"])
def log_in():
    log_in_form = LoginForm()
    if log_in_form.validate_on_submit():
        user = User.query.filter(or_(log_in_form.username_or_email.data == User.username, log_in_form.username_or_email.data == User.email)).first()
        if (user != None) and (User.check_password(user, log_in_form.password.data)):
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
    user = User.query.get(current_user.id)
    new_cart_product = CartProduct(product_id=post_data['productId'], quantity=post_data['productQuantity'], user=user)
    db.session.add(new_cart_product)
    db.session.commit()
    return 'the product has been added, slay!'


@app.route("/api/delete-review/<user_id>/<review_id>", methods=["DELETE"])
@login_required
def delete_review(user_id, review_id):
    if current_user.id == int(user_id) or current_user.role == "admin":
        theReviewToBeDeleted = Review.query.get(review_id)
        db.session.delete(theReviewToBeDeleted)
        db.session.commit()
        return "the review has been deleted"
    return "current user can't delete the review"


@app.route("/api/delete-cart-product/<cart_product_id>", methods=["DELETE"])
@login_required
def delete_cart_product(cart_product_id):
    cart_product = CartProduct.query.get(cart_product_id)
    if cart_product_id == "-1":
        print('aee')
        for product_of_cart in current_user.cart_products:
            print('ooo')
            db.session.delete(product_of_cart)
            db.session.commit()
        return "checkouted"
    db.session.delete(cart_product)
    db.session.commit()
    return "deleted cart product succesfully"


@app.route("/api/was-review-helpful", methods=["POST"])
@login_required
def wasTheReviewHelpful():
    post_data = request.get_json()
    the_review = Review.query.get(post_data['reviewId'])
    is_helpful = post_data['isHelpful']
    new_found_review_helpful = FoundReviewHelpful(found_helpful = is_helpful, review=the_review, user=current_user)
    db.session.add(new_found_review_helpful)
    db.session.commit()
    return "done"