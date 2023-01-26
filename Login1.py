from User1 import UserClass

class Login:
    __db = []
    def __init__(self):
        self.print_menu()
    def print_menu(self):
        print("Welcome User")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
    def create_user(self, name, email, password):
        new_user = UserClass(name, email, password)
        self.__db.append(new_user)
        print(self.__db)
        return True
    def validate_user(self, email, password):
        temp=self.__db.copy()
        for user_obj in temp:
            if email==user_obj.email:
                if password == user_obj.get_user_password():
                    return "Login succefull"
                else:
                    return "password incorrect:Login Failed"
            else:
                return "Login failed: password incorrect"
    def validate_email(self,email):
        if(email[0].isalpha() and '@' in email and email[-4]==".com"):
            return False
        else:
            return True

obj = Login()
while True:
    option = input("Enter your choice: ")
    if option == '1':
        while True:
            if obj.validate_email():
                print("invalid email")
                email=input("enter valid email")
            else:
                break

    elif option == '2':
        email=input('enter your email')
        password=input('enter your password')
        print(obj.validate_user(email,password))
    elif option == '3':
        break
    else:
        print("Invalid Input")




