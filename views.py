from app import app, db
from flask import redirect, url_for, request, render_template
from forms import RegistrationForm, loanCalculator
from models import User, loanProviders
from sqlalchemy import desc

@app.route('/')
def home():
	return'<h1>Hello</h1>'

@app.route('/applicantInfo')
def applicantInfo():
	return render_template('applicantInfo.html')

@app.route('/userData', methods=['POST'])
def userData():
	firstName=request.form['firstname']
	lastName=request.form['lastname']
	address=request.form['physicaladdress']
	age=request.form['age']
	occupation=request.form['occupation']
	dateJoined=request.form['time']
	netSalary=request.form['netsalary']
	loanType=request.form.get('loanType')
	gender=request.form['gender']
	IDnumber=request.form['IDnumber']
	phoneNumber=request.form['phoneNumber']
	
	newUser=User(firstName=firstName, lastName=lastName, address=address, age=age, occupation=occupation, dateJoined=dateJoined, netSalary=netSalary, loanType=loanType, gender=gender, IDnumber=IDnumber, phoneNumber=phoneNumber)
	db.session.add(newUser)
	db.session.commit()

	if occupation==

	return'ratng.html'