
import data as d
def login_validation(email):

    password = input("Enter your password : ")
    
    conn = d.get_connection()
    cursor = conn.cursor()
    
    query = '''
        SELECT password
        FROM credential
        WHERE user_email = :user_email
    '''
    
    cursor.execute(query,{'user_email' : email})
    record = cursor.fetchone()
    conn.close()
    
    check_record = record['password']
    
    if check_record == password:
        return True
    else:
        print("Incorrect Password")
        return False