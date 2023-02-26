from flask_app import app
from flask import render_template, redirect, session, flash
from flask_app.models.user_model import User

@app.route('/new/sighting')
def report_new():
    if not 'uid' in session:
        flash("ACCESS DENIED","login")
        return redirect('/')
    logged_in_user = User.get_user_id(session['uid'])

    return render_template('report.html', user = logged_in_user)