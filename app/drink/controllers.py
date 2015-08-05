# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
import pdb

# Import the database object from the main app module
from app import db

# Import module forms
from app.drink.forms import DrinkForm

# Import module models (i.e. User)
from app.drink.models import Drink

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_drink = Blueprint('drink', __name__, url_prefix='/drink')

@mod_drink.route('/', methods=['GET'])
def list():
    somenum=47
    drinks = Drink.query.all()
    #pdb.set_trace()
    return render_template("drink/list.html", drinks=drinks, somenum=somenum)

@mod_drink.route('/show/<id>', methods=['GET'])
def show(id):
    drink = Drink.query.get(id)
    return render_template("drink/show.html")

# Set the route and accepted methods
@mod_drink.route('/new', methods=['GET', 'POST'])
def new():

    form = DrinkForm(request.form)
    #pdb.set_trace()
    if form.validate_on_submit():
        drink = Drink(form.name.data, form.abv.data, form.with_ice.data, form.first_tried_on.data)
        #pdb.set_trace()
        db.session.add(drink)
        db.session.commit()
        return redirect(url_for('.list'))
    else:
        flash('Error when adding drink', 'error-message')
            #pdb.set_trace()
        return render_template("drink/new.html", form=form)
