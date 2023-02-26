from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

#? =====Home Page route========
@app.route('/')
def index():
    return redirect('/dojos')

#? =====Render Dojo list page====
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos = dojos)

#? =====Add a new dojo========
@app.route('/newdojo/process', methods=['POST'])
def process():
    data = {
        "name": request.form["name"]
    }
    dojo_new = Dojo.save(data)
    print(dojo_new)
    return redirect('/dojos')

#? =======Add a new ninja======
@app.route('/newninja')
def add_ninja():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', dojos=dojos)

#? ======Grab information from new_ninja.html and add to table=======
@app.route('/ninja/received', methods=['POST'])
def register_ninja():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["location"]
    }
    Ninja.save(data)
    return redirect('/dojos/'+ data["dojo_id"])

#? =====Route to show list of ninjas of a dojo=======
@app.route('/dojos/<int:id>')
def show_list(id):
    data = {
        'id' : id
    }
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template('ninja_list.html', dojo = dojo)