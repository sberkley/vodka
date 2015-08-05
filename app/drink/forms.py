# Import Form and RecaptchaField (optional)
from flask.ext.wtf import Form # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, BooleanField, DateField, IntegerField

# Import Form validators
from wtforms.validators import Required


# Define the login form (WTForms)

class DrinkForm(Form):
    name = TextField('Drink Name', [
            Required(message='Drinks must have a name.')])
    abv = IntegerField('ABV')
    with_ice = BooleanField('Prepared with ice?')
    first_tried_on = DateField('Date first tried')
