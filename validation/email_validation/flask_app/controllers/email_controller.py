from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users/process', methods=["POST"])
def process():
    if not User.validate(request.form):
        return redirect('/')

    User.save(request.form)
    return redirect('/email/result')

@app.route('/email/result')
def result():
    data = User.read()
    return render_template('result.html', emails = data)
