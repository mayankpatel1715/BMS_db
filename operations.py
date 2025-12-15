from bank import Account
import data as d
import display as dis
import valid
import logging
import bank_log
import login

def account_creation():
    name = input("Enter your Full name : ")
    dob = valid.date_of_birth()
    gender = valid.gender_verification()
    email = valid.email_id()
    phone_no = valid.phone()
    
    hash_pass = login.password()
    
    info = Account(name,gender,dob,email,phone_no)
    user_data = info.bank_app()
    
    conn = d.get_connection()
    cursor = conn.cursor()
    
    query = '''
        INSERT INTO account (name,gender,DOB,email,phone_no)
        VALUES (:name, :gender, :DOB, :email, :phone_no)
    '''
    
    cursor.execute(query,user_data)
    cursor.execute("INSERT INTO credential (password, user_email) VALUES(?,?)",(hash_pass,email))
    conn.commit()
    conn.close()
    
def account_detail(user_email):
    
    logging.info(" ==== Entered Account Details ==== ")
    
    conn = d.get_connection()
    cursor = conn.cursor()
    
    try:
        query = '''
            SELECT * 
            FROM account
            WHERE email = :email
        '''
    
        cursor.execute(query,{"email" : user_email})
        result = cursor.fetchone()
        
    except Exception as e:
        logging.warning("Soemthing went wrong with Database")
        raise e
    
    finally:
        conn.close()
        logging.info("Connection with database is closed")
        
        if result:
            logging.info("Account fetched Sccussfully")
            return dict(result)
        # else:
        #     return

def money_deposit(email):
    
    logging.info(" ==== Entered Deposit Money ==== ")
    conn = d.get_connection()
    cursor = conn.cursor()
    
    deposit = valid.check_money()
        
    try:
        logging.info("Quering to database")
        query = '''
            UPDATE account
            SET Balance = Balance + :deposit
            WHERE email = :email
        '''
        
        data={
            "deposit" : deposit,
            "email" : email
        }
    
        cursor.execute(query,data)
        logging.info("Operation Performed")
        conn.commit()
        
    except Exception as e:
        logging.warning("Something went wrong.")
        raise e
    
    finally:
        conn.close()
        logging.info("Connection with database is closed")
        logging.info(f"User Desposited : ₹{deposit}")
    
    
def money_withdraw(email):
    
    logging.info(" ==== Entered Withdraw Money ==== ")
    conn = d.get_connection()
    cursor = conn.cursor()
    
    withdraw_money = valid.check_money()
    
    try:
        logging.info("Quering to database")
        cursor.execute("SELECT Balance FROM account WHERE email = :email",{"email" : email})
        
        result = cursor.fetchone()
        curr_bal = int(result['Balance'])

        if curr_bal > withdraw_money:

            query = '''
                UPDATE account
                SET Balance = Balance - :withdraw_money
                WHERE email = :email
            '''

            data ={
                "withdraw_money" : withdraw_money,
                "email" : email
            }
            
            cursor.execute(query,data)
            conn.commit()
        else:
            logging.warning("User is trying to withdraw negative balance.")
            print("User can't withdraw negative balance.")
            raise Exception("User cannot withdraw negative balance.")
        
    except Exception as e:
        logging.warning("Something went wrong with database.")
        raise e
    
    finally:
        conn.close()
        logging.info("Connection with database is closed")
        logging.info(f"User Withdrawn : ₹{withdraw_money}")

    
    
def delete_account(email):
    
    logging.info(" ==== Entered Account Deletion Mode ==== ")
    conn = d.get_connection()
    cursor = conn.cursor()
    
    try:
        
        logging.info("Quering to database")
        query = '''
            DELETE FROM account
            WHERE email  = :email
        '''
        query1 = '''
            DELETE FROM credential
            WHERE user_email = :email
        '''
    
        data = {"email" : email}
    
        cursor.execute(query1,data)
        cursor.execute(query,data)
        conn.commit()
        
    except Exception as e:
        logging.warning("Something went wrong with database.")
        raise e
    
    finally:
        conn.close()
        logging.info("Connection with database is closed")
        logging.info(f"User Account : {email} deleted sccussfully")