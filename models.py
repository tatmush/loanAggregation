from app import app, db
from datetime import datetime

class User(db.Model):
	firstName=db.Column(db.String(50), primary_key=True)
	lastName=db.Column(db.String(50))
	address=db.Column(db.String(50))
	age=db.Column(db.Integer)
	occupation=db.Column(db.String(50))
	dateJoined=db.Column(db.String(10))
	netSalary=db.Column(db.Integer)
	loanType=db.Column(db.String(50))
	gender=db.Column(db.String(50))
	IDnumber=db.Column(db.String(50))
	phoneNumber=db.Column(db.String(50))


class loanProviders(db.Model):
	name=db.Column(db.String(50), primary_key=True)
	amountCapable=db.Column(db.String(50))
	loanType=db.Column(db.String(50))
	collateralType=db.Column(db.String(500))

	