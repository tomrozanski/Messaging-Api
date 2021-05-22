from flask import Flask, request
from dotenv import dotenv_values

app = Flask(__name__)
config = dotenv_values(".env") 
app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
app.config['SECRET_KEY'] = config['SECRET_KEY']
