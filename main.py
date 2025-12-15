import operations as ops
import data
import display as dis
import login
import logging
import bank_log

def main():
    logging.info("Started Bank Application")
    logging.info("Loading Database")
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
        try:
            if choice == '1':
                ops.account_creation()
                
            elif choice == '2':
                try:
                    logging.info("Starting login attempt")
                    user_email = input("Enter your email address : ")
                    if login.login_validation(user_email) == True:
                        
                        print("\nWelcome\n")
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
                                    logging.info("User Entering Account Details")
                                    user_data = ops.account_detail(user_email)
                                    if user_data:
                                        dis.account_display(user_data)
                                    # else:
                                    #     raise Exception("Account not found")
                                    
                                case '2':
                                    logging.info("User Depositing Money")
                                    ops.money_deposit(user_email)
                                    
                                case '3':
                                    logging.info("User withdrawing Money")
                                    ops.money_withdraw(user_email)
                                    
                                case '4':
                                    logging.info("User deleting Account")
                                    ops.delete_account(user_email)
                                    break
                                
                                case '5':
                                    print("Exiting ...")
                                    break
                    else:
                        logging.error("User Typed incorrect Password. Login Attempt failed.")
                        raise Exception("Invlaid Loging Credential")
                        break
                    
                except Exception as e:
                    print(str(e))
                                
            elif choice == '3':
                print("Exiting the APP")
                break
            
        except ValueError as e:
            print(str(e))
            
        except TypeError as e:
            print(str(e))
            
        except Exception as e:
            print(str(e))
            
            
if __name__ == "__main__":
    main()