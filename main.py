import smtplib

class email:
    def __init__(self):
        self.port=465
        self.username="snowwing14@gmail.com"
        self.password="***************"
        self.address="snowwing140@gmail.com"
        self.message="Hello"

    def connectGmail(self):
        self.server=smtplib.SMTP_SSL("smtp.gmail.com",self.port)
    
    def login(self):
        self.username=input("Username: ")
        self.password=input("Password: ")
        try:
            self.server.login(self.username,self.password)
        except:
            print("Error login! Check you mail")
    
    def sent(self):
        self.address=input("send to: ")
        self.message=input("Message: ")
        self.server.sendmail(self.username,self.address,self.message)
        self.server.quit()
    
if __name__ == "__main__":
    obj_1=email()
    obj_1.connectGmail()
    obj_1.login()
    obj_1.sent()
    
