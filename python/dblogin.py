'''
dailyDose demo system
Author: David Christy

A quick little write up to test the user login, and soon to be message system.


TODO:

'''

import re
import hashlib
import os
import mysql.connector
from mysql.connector import errorcode
import string
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

cnx = 0
cursor = 0
current_user = 0

def connectToDatabase():
	# Connecting to the server
	try:
		global cnx
		cnx = mysql.connector.connect(user='testUser', password='testPass',
									host='127.0.0.1',
									database='dailyDose')
		global cursor 
		cursor = cnx.cursor()
	except mysql.connector.Error as err:
	  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
	    print("Something is wrong with your user name or password")
	    exit()
	  elif err.errno == errorcode.ER_BAD_DB_ERROR:
	    print("Database does not exist")
	    exit()
	  else:
	    print(err)
	    exit()

def logIn():
	os.system("clear")
	email = raw_input("Enter in your email: \n")
	password = hashlib.sha256(raw_input("Enter in your password: \n")).hexdigest()

	query = ("SELECT email, password_hash, password_salt FROM user "
    	     "WHERE email = '" + email + "'")

	cursor.execute(query)

	for (email, password_hash, password_salt) in cursor:
		if password_hash == hashlib.sha256(password + password_salt).hexdigest():
			print bcolors.OKGREEN + "You have been logged in!\nCurrent user: " + email + bcolors.ENDC
			global current_user
			current_user = email
			return True
		else:
			print bcolors.FAIL + "You have enter password wrong" + bcolors.ENDC
			return False
	# the username is not found
	print bcolors.FAIL + "You have enter username wrong" + bcolors.ENDC
	return False


def checkInput(email, phone):

	# Super basic error checking for email
	if not re.search('^.*@.*\..*$',email):
		print "email not correct, please try again"
		return False

	# Super basic checking for phone
	if not phone.isdigit() or len(phone) != 10:
		print "phone number is in wrong format, please try again"
		return False

	# is username already in database?
	query = ("SELECT email, password_hash, password_salt FROM user "
	    	     "WHERE email = '" + email + "'")
	cursor.execute(query)

	if len(cursor.fetchall()):
		print "'" + email + "' Already exist, please pick another"
		return False

	return True



def createAcount():
	email = raw_input("Enter in your email: \n")
	password = hashlib.sha256(raw_input("Enter in your password: \n")).hexdigest()
	phone = raw_input("Enter in your phone number: \n")

	if not checkInput(email, phone):
		return

	# adding data to the table
	add_user = ("INSERT INTO user "
	               "(phone_number, password_hash, password_salt, email) "
	               "VALUES (%s, %s, %s, %s)")
	salt = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16))
	data_user = (phone, hashlib.sha256(password+salt).hexdigest(), salt, email)
	cursor.execute(add_user, data_user)
	cnx.commit()	


def submitSMS():
	smsText = raw_input("What is the message you would like to submit?\n")

	query = ("SELECT email, user_ID FROM user "
	    	     "WHERE email = '" + current_user + "'")
	cursor.execute(query)
	for (email, user_ID) in cursor:
		userID = user_ID

	# Do some checkingo on this
	add_sms = ("INSERT INTO message "
	               "(user_ID, text) "
	               "VALUES (%s, %s)")
	data_sms = (userID, smsText)

	cursor.execute(add_sms, data_sms)
	cnx.commit()


def recieveSMS():
	os.system("clear")
	query = ("SELECT text FROM message "
			"ORDER BY RAND()"
			"LIMIT 1")
	cursor.execute(query)
	
	print cursor.fetchall()[0][0]

def main():

	os.system("clear")
	connectToDatabase()
	while True:
		if not current_user:
			print "Do you want to log in or create an account"
			print "1) Log in"
			print "2) Create Account"
			tempinput = raw_input()
			if tempinput == "1" or tempinput[0].lower() == "l":
				if not logIn():
					break
			elif tempinput == "2" or tempinput[0].lower() == "c":
				createAcount()
				break
			else:
				print bcolors.WARNING + "try again" + bcolors.ENDC
		else:
			print "Welcome " + current_user
			print "Do you want to submit a sms or recieve on?"
			print "1) submit sms"
			print "2) recieve sms"
			tempinput = raw_input()
			if tempinput == "1" or tempinput[0].lower() == "s":
				submitSMS()
				break
			elif tempinput == "2" or tempinput[0].lower() == "r":
				recieveSMS()
				break
			else:
				print bcolors.WARNING + "try again" + bcolors.ENDC
	
if __name__ == '__main__':
	main()

