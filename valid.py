import logging
import bank_log
import re
import datetime

def check_money():
    logging.info(" ==== Entered Money Validation ==== ")
    while True:
        
        money = input("Enter the amount of Money : ₹")
        
        try:
            mon = int(money)
        except ValueError:
            logging.warning("User didnot entered digits")
            print("Invlaide Input. Please enter digits only.")
            continue
        
        if mon>0:
            logging.info("Money Validation confirmed")
            return mon
        else:
            print("Please Enter a positive value(₹)")
            logging.warning("User entered negative value.")


def phone():
    logging.info(" ==== Entered phone Number Verification ==== ")
    
    pattern = r"^[1-9][0-9]{9}$"
    
    while True:
        num = input("Enter your phone number : +91 ")
        if re.match(pattern,num):
            logging.info("Phone Number Verified.")
            return num
        else:
            logging.warning("Invalid Phone Number.")
            print("Incorrect Phone number format. Try Again.")
            
def date_of_birth():
    logging.info(" ==== Entered Date of Birth Verification ==== ")
    
    while True:
        dob = input("Enter your Date of Birth [dd/mm/yyyy] : ")
        try:
            # date = datetime.striptime(dob,"%d/%m/%Y")
            date = datetime.datetime.strptime(dob,"%d/%m/%Y")
            logging.info("Date of Birth Verified Successfully.")
            return str(date.date())
        except ValueError:
            logging.warning("Invalid Date format.")
            print("Invalid Date format. Please use [dd/mm/yyyy]")
            
def gender_verification():
    logging.info(" ==== Entered Gender Verification ==== ")

    while True:
        gen = input("Enter your Gender[M/F] : ")
        
        if gen == 'M'or gen == 'F' or gen == 'Male' or gen == 'Female':
            logging.info("Gender Verified.")
            return gen
        else:
            logging.info("Invalid Gender")
            print("Enter proper gender [M/F]")

def email_id():
    logging.info(" ==== Entered Email Id verification ==== ")
    
    pattern = r"^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]{2,}$"
    
    while True:
        mail = input("Enter your email address : ")
        
        if re.match(pattern,mail):
            logging.info("Email Address verified.")
            return mail
        else:
            logging.warning("Invalid email address")