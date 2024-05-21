from flask import Flask, render_template

app = Flask(__name__)

data = [
    {
        "id": 1,
        "name": "Camouflage",
        "cost": 27,
        "discount": False,
        "howMuchDiscount": None,
        "topSeller": False,
        "colors": [
            "Orange",
            "Pink"
        ],
        "images": [
            "https://static.wixstatic.com/media/45d10e_dd5d9543998c4c0f9ecf120fac20ffb0~mv2.jpg/v1/fill/w_625,h_625,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/45d10e_dd5d9543998c4c0f9ecf120fac20ffb0~mv2.jpg",
            "https://static.wixstatic.com/media/45d10e_d6445cbc0df2428d9348c3a7639dbed8~mv2.jpg/v1/fill/w_625,h_625,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/45d10e_d6445cbc0df2428d9348c3a7639dbed8~mv2.jpg"
        ],
        "images_patterns": [
            "https://static.wixstatic.com/media/45d10e_35c84fb1d48540f1886b2ceb7a342c37~mv2_d_3500_1968_s_2.jpg/v1/fill/w_541,h_541,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/45d10e_35c84fb1d48540f1886b2ceb7a342c37~mv2_d_3500_1968_s_2.jpg"
        ]
    },
    {
        "id": 2,
        "name": "Lemon",
        "cost": 15,
        "discount": True,
        "howMuchDiscount": 27,
        "topSeller": False,
        "colors": [
            "Light purple",
            "Mint"
        ],
        "images": [
            "https://static.wixstatic.com/media/45d10e_15641be40e0c43d89f5426f8949b51bd~mv2.jpg/v1/fill/w_625,h_625,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/45d10e_15641be40e0c43d89f5426f8949b51bd~mv2.jpg",
            "https://static.wixstatic.com/media/45d10e_3f6b16a5b6f245adb42be86ef69705b9~mv2.jpg/v1/fill/w_625,h_625,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/45d10e_3f6b16a5b6f245adb42be86ef69705b9~mv2.jpg"
        ],
        "images_patterns": [
            "https://static.wixstatic.com/media/45d10e_0a7831138003425684827b5eedb8813a~mv2_d_3500_1968_s_2.jpg/v1/fill/w_541,h_541,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/45d10e_0a7831138003425684827b5eedb8813a~mv2_d_3500_1968_s_2.jpg"
        ]
    },
    {
        "id": 3,
        "name": "Hand",
        "cost": 24,
        "discount": False,
        "howMuchDiscount": None,
        "topSeller": True,
        "colors": [
            "Green"
        ],
        "images": [
            "https://static.wixstatic.com/media/45d10e_9e18a8d563fc4774a0b917d7f5e07ff6~mv2.jpg/v1/fill/w_625,h_625,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/45d10e_9e18a8d563fc4774a0b917d7f5e07ff6~mv2.jpg"
        ],
        "images_patterns": [
            "https://static.wixstatic.com/media/45d10e_4f8f19f78fe64963b0861ad87b8984fa~mv2_d_3500_1968_s_2.jpg/v1/fill/w_541,h_541,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/45d10e_4f8f19f78fe64963b0861ad87b8984fa~mv2_d_3500_1968_s_2.jpg"
        ]
    },
    {
        "id": 4,
        "name": "Abstract",
        "cost": 19,
        "discount": True,
        "howMuchDiscount": 35,
        "topSeller": False,
        "colors": [
            "Blue"
        ],
        "images": [
            "https://static.wixstatic.com/media/45d10e_1d14719f23fa4277bddd33220562c678~mv2.jpg/v1/fill/w_625,h_625,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/45d10e_1d14719f23fa4277bddd33220562c678~mv2.jpg"
        ],
        "images_patterns": [
            "https://static.wixstatic.com/media/45d10e_634904991ab140089d95a832cac3ec03~mv2_d_3500_1968_s_2.jpg/v1/fill/w_541,h_541,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/45d10e_634904991ab140089d95a832cac3ec03~mv2_d_3500_1968_s_2.jpg"
        ]
    },
    {
        "id": 5,
        "name": "Dalmatian",
        "cost": 30,
        "discount": False,
        "howMuchDiscount": None,
        "topSeller": False,
        "colors": [
            "Black"
        ],
        "images": [
            "https://static.wixstatic.com/media/45d10e_b35e4713f3524a1d818de736bb4765b2~mv2.jpg/v1/fill/w_625,h_625,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/45d10e_b35e4713f3524a1d818de736bb4765b2~mv2.jpg"
        ],
        "images_patterns": [
            "https://static.wixstatic.com/media/45d10e_fcf0fc02da714ac993c176af2ae771fb~mv2_d_3500_1968_s_2.jpg/v1/fill/w_541,h_541,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/45d10e_fcf0fc02da714ac993c176af2ae771fb~mv2_d_3500_1968_s_2.jpg"
        ]
    },
    {
        "id": 6,
        "name": "Cactus",
        "cost": 16,
        "discount": False,
        "howMuchDiscount": None,
        "topSeller": False,
        "colors": [
            "Black"
        ],
        "images": [
            "https://static.wixstatic.com/media/45d10e_3c8908475cb04049a7341efbc73f6a73~mv2.jpg/v1/fill/w_625,h_625,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/45d10e_3c8908475cb04049a7341efbc73f6a73~mv2.jpg"
        ],
        "images_patterns": [
            "https://static.wixstatic.com/media/45d10e_fba225710b3b49dfa8c8617610cd9358~mv2_d_3500_1968_s_2.jpg/v1/fill/w_541,h_541,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/45d10e_fba225710b3b49dfa8c8617610cd9358~mv2_d_3500_1968_s_2.jpg"
        ]
    },
    {
        "id": 7,
        "name": "Unique",
        "cost": 22,
        "discount": False,
        "howMuchDiscount": None,
        "topSeller": True,
        "colors": [
            "Multicolor"
        ],
        "images": [
            "https://static.wixstatic.com/media/45d10e_45e21af15e5a4e2fa81bc324b0c51cbf~mv2.jpg/v1/fill/w_625,h_625,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/45d10e_45e21af15e5a4e2fa81bc324b0c51cbf~mv2.jpg"
        ],
        "images_patterns": [
            "https://static.wixstatic.com/media/45d10e_291e40a5e013492795a1e7b2543fd84f~mv2_d_3500_1968_s_2.jpg/v1/fill/w_541,h_541,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/45d10e_291e40a5e013492795a1e7b2543fd84f~mv2_d_3500_1968_s_2.jpg"
        ]
    },
    {
        "id": 8,
        "name": "Banana",
        "cost": 28,
        "discount": False,
        "howMuchDiscount": None,
        "topSeller": False,
        "colors": [
            "Orange"
        ],
        "images": [
            "https://static.wixstatic.com/media/45d10e_184c51e0dfc64e70a5bc0fa7e2fe981e~mv2.jpg/v1/fill/w_625,h_625,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/45d10e_184c51e0dfc64e70a5bc0fa7e2fe981e~mv2.jpg"
        ],
        "images_patterns": [
            "https://static.wixstatic.com/media/45d10e_b20e57309af44269b6655ce248bca487~mv2_d_3500_1968_s_2.jpg/v1/fill/w_541,h_541,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/45d10e_b20e57309af44269b6655ce248bca487~mv2_d_3500_1968_s_2.jpg"
        ]
    },
    {
        "id": 9,
        "name": "Tiger and a girl",
        "cost": 17,
        "discount": True,
        "howMuchDiscount": 23,
        "topSeller": False,
        "colors": [
            "Purple"
        ],
        "images": [
            "https://static.wixstatic.com/media/45d10e_871191908b1c4045995538d0a943a5a3~mv2.jpg/v1/fill/w_625,h_625,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/45d10e_871191908b1c4045995538d0a943a5a3~mv2.jpg"
        ],
        "images_patterns": [
            "https://static.wixstatic.com/media/45d10e_20a938f8eca444a1ab34b1b2d361b71f~mv2_d_3500_1968_s_2.jpg/v1/fill/w_541,h_541,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/45d10e_20a938f8eca444a1ab34b1b2d361b71f~mv2_d_3500_1968_s_2.jpg"
        ]
    },
    {
        "id": 10,
        "name": "Swimmer",
        "cost": 23,
        "discount": False,
        "howMuchDiscount": None,
        "topSeller": False,
        "colors": [
            "Purple"
        ],
        "images": [
            "https://static.wixstatic.com/media/45d10e_0e8c51e5fcbe457397c2823e833cfa62~mv2.jpg/v1/fill/w_625,h_625,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/45d10e_0e8c51e5fcbe457397c2823e833cfa62~mv2.jpg"
        ],
        "images_patterns": [
            "https://static.wixstatic.com/media/45d10e_7534171f1db24b66af322f721a90d7c7~mv2_d_3500_1968_s_2.jpg/v1/fill/w_541,h_541,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/45d10e_7534171f1db24b66af322f721a90d7c7~mv2_d_3500_1968_s_2.jpg"
        ]
    },
    {
        "id": 11,
        "name": "Cheetah",
        "cost": 14,
        "discount": False,
        "howMuchDiscount": None,
        "topSeller": True,
        "colors": [
            "Pink"
        ],
        "images": [
            "https://static.wixstatic.com/media/45d10e_e72efca453234bfda3baa6dde357e4d8~mv2.jpg/v1/fill/w_625,h_625,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/45d10e_e72efca453234bfda3baa6dde357e4d8~mv2.jpg"
        ],
        "images_patterns": [
            "https://static.wixstatic.com/media/45d10e_bebe0265a9644b8697b873a11de242f6~mv2_d_3500_1968_s_2.jpg/v1/fill/w_541,h_541,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/45d10e_bebe0265a9644b8697b873a11de242f6~mv2_d_3500_1968_s_2.jpg"
        ]
    },
    {
        "id": 12,
        "name": "Pine cone",
        "cost": 29,
        "discount": False,
        "howMuchDiscount": None,
        "topSeller": False,
        "colors": [
            "Yellow"
        ],
        "images": [
            "https://static.wixstatic.com/media/45d10e_f2827033127e4856b9b030067d81bba2~mv2.jpg/v1/fill/w_625,h_625,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/45d10e_f2827033127e4856b9b030067d81bba2~mv2.jpg"
        ],
        "images_patterns": [
            "https://static.wixstatic.com/media/45d10e_85b84e09e8964627bcb095a52463344e~mv2_d_3500_1968_s_2.jpg/v1/fill/w_541,h_541,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/45d10e_85b84e09e8964627bcb095a52463344e~mv2_d_3500_1968_s_2.jpg"
        ]
    }
]


@app.context_processor
def global_variable():
    return dict(products=data)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/product/<product_id>")
def product_details(product_id):
    return render_template("product.html", product=data[int(product_id) - 1])


@app.route("/gift-card")
def gift_card():
    return render_template("gift-card.html")


@app.route("/gift-card-checkout")
def gift_card_checkout():
    return render_template("gift-card-checkout.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/log-in")
def log_in():
    return render_template("log-in.html")


@app.route("/sign-up")
def sign_in():
    return render_template("sign-up.html")


app.run(debug=True)
