from flask import Flask, session

app = Flask(__name__)

app.secret_key = "don't tell anyone!"

DATABASE = 'email_db'