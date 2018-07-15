from app import app, db
from flask import redirect, url_for, request, render_template
from forms import RegistrationForm, loanCalculator
from models import Userman, loanProviders
from sqlalchemy import desc
from random import randint


@app.route('/')
def applicantInfo():
	return render_template('applicantInfo.html')

@app.route('/userData', methods=['POST'])
def userData():
	firstName=request.form['firstname']
	lastName=request.form['lastname']
	address=request.form['physicaladdress']
	age=request.form['age']
	occupation=request.form.get('occupation')
	dateJoined=request.form['time']
	netSalary=request.form['netsalary']
	loanType=request.form.get('loanType')
	gender=request.form['gender']
	IDnumber=request.form['IDnumber']
	phoneNumber=request.form['phoneNumber']
	

	#newUser=Userman(firstName=firstName, lastName=lastName, address=address, age=age, occupation=occupation, dateJoined=dateJoined, netSalary=netSalary, loanType=loanType, gender=gender, IDnumber=IDnumber, phoneNumber=phoneNumber)
	#db.session.add(newUser)
	#db.session.commit()

	netSalary=int(netSalary)
	age=int(age)


	if occupation=='permanent':
		occupationType=1
	elif occupation=='contract':
		occupationType=0.75
	elif occupation=='self':
		occupationType=0.5
	else:
		occupationType=0

	percentage=(netSalary/10000) * 100
	if percentage>20:
		ratio=4
	elif percentage<20 and percentage>10:
		ratio=3
	elif percentage<=10 and percentage>5:
		ratio=2
	else:
		ratio=1

	if age<18:
		ageRate=0
	elif age>18 and age<35:
		ageRate=2
	elif age>36 and age<50:
		ageRate=1.5
	elif age>51 and age>65:
		ageRate=1
	else:
		ageRate=0

	#transactionHist=randint(0,4)
	transactionHist=1.5
	outcome=occupationType+ratio+ageRate+transactionHist%10

	return render_template('rating.html', outcome=outcome)


@app.route('/financers')
def financers():
	return render_template('Financers.html')


@app.route('/loanCal')
def loanCal():
	return render_template('loanCal.html')