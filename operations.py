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

def money_deposit(email):
    conn = d.get_connection()
    cursor = conn.cursor()
    
    deposit = int(input("Enter How much money you want to deposit : ₹"))
    
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
    conn.commit()
    conn.close()
    
def money_withdraw(email):
    conn = d.get_connection()
    cursor = conn.cursor()
    
    withdraw_money = int(input("Enter how much money you want to withdraw : ₹"))
    
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
    conn.close()
    
    
def delete_account(email):
    conn = d.get_connection()
    cursor = conn.cursor()
    
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
    # cursor.execute(query1,data)
    conn.commit()
    conn.close()