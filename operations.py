from bank import Account
import data as d

def account_creation():
    name = input("Enter your Full name : ")
    dob = input("Enter your Date of Birth [dd/mm/yyyy] : ")
    gender = input("Enter your Gender [Male/Female] : ")
    email = input("Enter your email address : ")
    phone_no = input("Enter your Phone Number : ")
    
    info = Account(name,gender,dob,email,phone_no)
    user_data = info.bank_app()
    
    conn = d.get_connection()
    cursor = conn.cursor()
    
    query = '''
        INSERT INTO account (name,gender,DOB,email,phone_no)
        VALUES (:name, :gender, :DOB, :email, :phone_no)
    '''
    
    cursor.execute(query,user_data)
    conn.commit()
    