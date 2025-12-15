import operations as ops
import data
import display as dis
import login

def main():
    
    data.db()
    
    print("\n")
    print("Welcome to Banking System")
    
    while True:
        print("\n")
        print("1. Create New Account")
        print("2. Login")
        print("3. Exit the App")
        print("\n")
        
        choice = input("Select your Choice : ")
        
        if choice == '1':
            ops.account_creation()
            
        elif choice == '2':
            user_email = input("Enter your email address : ")
            if login.login_validation(user_email) == True:
                while True:
                    print("\n")
                    print("1. Account Details")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. Delete Account")
                    print("5. Exit")
                
                    option = input("Choose an option : ")
                
                    match option:
                        case '1':
                            user_data = ops.account_detail(user_email)
                            if user_data:
                                dis.account_display(user_data)
                            else:
                                print("No Account found")
                        case '2':
                            pass
                        case '3':
                            pass
                        case '4':
                            pass
                        case '5':
                            print("Exiting ...")
                            break
            else:
                print("Invalid Login Credential")
                break           
        elif choice == '3':
            print("Exiting the APP")
            break
        
if __name__ == "__main__":
    main()