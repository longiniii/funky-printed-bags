from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "AIDIFAIDFIASDIF"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myDataBase.db"

db = SQLAlchemy(app)
