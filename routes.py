from flask import render_template, request, redirect
from forms import RegistrationForm, PostingProduct, ContactForm
from ext import app, db
from models import Contact, Product, ProductColor, ProductImage, ProductImagePattern


@app.context_processor
def global_variable():
    products = Product.query.all()
    return dict(products=products)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/post-a-product", methods=["GET", "POST"])
def post_a_product():
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
            added_by = 1, 
            edited_by = 1)
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


@app.route("/product/<product_id>")
def product_details(product_id):
    product = Product.query.get(product_id)
    return render_template("product.html", product=product)


@app.route("/delete-product/<product_id>")
def delete_product(product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect("/")


@app.route("/edit-product/<product_id>", methods=['GET', 'POST'])
def edit_product(product_id):
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
        product.added_by = 1
        product.edited_by = 1
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
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        new_contact = Contact(
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
def view_contacts():
    contacts = Contact.query.all()
    return render_template("view-contacts.html", contacts=contacts)


@app.route("/delete-contact/<contact_id>")
def delete_contact(contact_id):
    contact = Contact.query.get(contact_id)
    db.session.delete(contact)
    db.session.commit()
    return redirect("/view-contacts")


@app.route("/log-in")
def log_in():
    return render_template("log-in.html")


@app.route("/sign-up", methods=["GET","POST"])
def sign_in():
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        print(registration_form.username.data)
    return render_template("sign-up.html", registration_form=registration_form)


@app.route("/api/add-to-cart", methods=['POST'])
def add_to_cart():
    post_data = request.get_json()
    return 'successfully added to cart'
