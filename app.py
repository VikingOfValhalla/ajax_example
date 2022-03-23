# importing of the flask module as well as render_template module
# render_template module allows to return an html document
# jsonify template to send request to AJAX server
# import NumPy to use an array (this is more compact than python lists)
from flask import Flask, render_template
from flask import jsonify
import numpy as np

# naming the Flask application to assign location within script
application = Flask(__name__)

# assigning NumPy to create a global vairable for an array of random numbers
random_decimal = np.random.rand()

# @application.route('') defines the location of the webpages
@application.route("/update_decimal", methods=['POST'])

# function to define the process of updating the decimal
def update_decimal():
    # linking the random_decimal variable to the function
    random_decimal = np.random.rand()
    # forcing a jsonify typing style for the templates
    return jsonify('', render_template('random_decimal_model.html', x=random_decimal))

# function defining home page of the app
@application.route("/")
# functionality of the home page
def hello_world():
    # defining first returned template on the home page
    return render_template('home.html', x=random_decimal)
