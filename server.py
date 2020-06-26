from flask import Flask, render_template, send_from_directory
import os
from flask import request,redirect
import csv

app = Flask(__name__)

@app.route('/')
def myHome():
    return render_template('index.html')

@app.route('/<string:page_name>')
def website(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method=='POST':
        data=request.form.to_dict()
        write_to_csv(data)
        return redirect('ThankYou.html')
    else:
        print('Something went wrong !')

def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as database2:
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer=csv.writer(database2,delimiter="")
        csv_writer.writerows([email,subject,message])



# @app.route('/index.html')
# def home():
#     return render_template('index.html')
#
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# set FLASK_APP=server.py
# set FLASK_ENV=development