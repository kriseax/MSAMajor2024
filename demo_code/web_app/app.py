#import modules
from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#make a Flask app
app = Flask(__name__)
app.config["DEBUG"] = True

#set a secret key to use when validating form data
app.config["SECRET_KEY"] = "your secret key"

#Function to request student data from the api
#Input: url
#Output: JSON student data
def get_student_data(url):
    #make a request
    response = requests.get(url)

    #convert format to json
    response_json = response.json()

    return response_json

#create a route for the site index page that will display all student data
@app.route("/", methods=['GET'])
def index():
    #get the student data
    #make a request to the student data api url
    url = "http://127.0.0.1:5000/api/students/all"

    student_data = get_student_data(url)

    #send the student data to the index.html page
    return render_template('index.html', student_data=student_data)

@app.route('/majors', methods=['GET'])
def majors():
    return render_template('majors.html')


app.run(port=5005)
