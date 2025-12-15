import logging
import bank_log
import data as d
import bcrypt

def password():
    password = input("Enter your password : ")
    pass_bytes = password.encode('utf-8')
    hash_pass = bcrypt.hashpw(pass_bytes,bcrypt.gensalt())
    return hash_pass.decode("utf-8")
    
def login_validation(email):
    
    logging.info("Entered login Validation")
    
    try:
        conn = d.get_connection()
        cursor = conn.cursor()
        logging.info("Connection with database is Open")
    
        query = '''
            SELECT password
            FROM credential
            WHERE user_email = :user_email
        '''
    
        cursor.execute(query,{'user_email' : email})
        record = cursor.fetchone()
    
    except Exception as e:
        logging.warning("Something went wrong with database.")
        raise e
    
    finally:    
        conn.close()
        logging.info("Connection with database is closed")

    
    plain_password = input("Enter your password : ")
    plain = plain_password.encode('utf-8')
    
    if record:
        logging.info(f"USer : {email} logged in sccussfully")
        check_record = record['password'].encode('utf-8')
        
        if bcrypt.checkpw(plain,check_record):
            logging.info("Login Sccussfull")
            print("Login Sccussfull")
            return True
        else:
            return False
    else:
        logging.error("Account Not Found")
        raise TypeError("Account Not Found")