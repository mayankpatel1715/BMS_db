from bank import Account
import data as d
import display as dis


def account_creation():
    name = input("Enter your Full name : ")
    dob = input("Enter your Date of Birth [dd/mm/yyyy] : ")
    gender = input("Enter your Gender [Male/Female] : ")
    email = input("Enter your email address : ")
    phone_no = input("Enter your Phone Number : ")
    
    password = input("Choose and enter a password : ")
    
    info = Account(name,gender,dob,email,phone_no)
    user_data = info.bank_app()
    
    conn = d.get_connection()
    cursor = conn.cursor()
    
    query = '''
        INSERT INTO account (name,gender,DOB,email,phone_no)
        VALUES (:name, :gender, :DOB, :email, :phone_no)
    '''
    
    cursor.execute(query,user_data)
    cursor.execute("INSERT INTO credential (password, user_email) VALUES(?,?)",(password,email))
    conn.commit()
    conn.close()
    
def account_detail(user_email):
        
    conn = d.get_connection()
    cursor = conn.cursor()
    
    query = '''
        SELECT * 
        FROM account
        WHERE email = :email
    '''
    
    cursor.execute(query,{"email" : user_email})
    result = cursor.fetchone()
    
    conn.close()
        
    if result:
        return dict(result)
    else:
        return

        