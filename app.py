from ext import app

if __name__ == "__main__":
    from routes import global_variable, index, product_details, gift_card, gift_card_checkout, contact, log_in, sign_in, post_a_product, add_to_cart, view_contacts, delete_contact, delete_contact, edit_product
    app.run(debug=True)