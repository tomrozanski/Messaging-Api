from flask import Flask, request
from dotenv import dotenv_values

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '\x1e\xda\t\x91\xdeu\xf2\xee\x9c\xaeR\xd3Uo\xbe\xf6\xf5\x189\xff?\xb5\xd7\xfb'
