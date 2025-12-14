class Account:
    def __init__(self,name,gender,dob,email,phone_no):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.email = email
        self.phone_no = phone_no
        
    def bank_app(self):
        
        form = {
            "name" : self.name,
            "gender" : self.gender,
            "DOB" : self.dob,
            "email" : self.email,
            "phone_no" : self.phone_no
        }
        
        return form
        