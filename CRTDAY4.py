# * OPERATOR
# a=(1,2,3)*5
# print(a)

#BITWISE XOR
# a=int(input())
# b=int(input())
# c=a^b
# print(c)



#PACKAGES
# from packages import add_n_numbers
# print(add_n_numbers(10,20,30))





#OOPS CONCEPT
#PROGRAM 1
# class Student:
#     student_name="No name"
#     def __init__(self,name):
#         print('object created')
#         self.student_name=name
#         print(self.student_name)
# s1=Student("Nagendra")
# s2=Student("gopi")





#PROGRAM 2

# class Student:
#
#     student_name=""
#     student_age=""
#     stu_marks=0
#     def __init__(self,name,age):
#         self.student_name=name
#         self.student_age=age
#
#     def stu_marks(self,marks):
#         self.stu_marks=marks
#
#
# s1=Student('Nagendra',"19")
# s2=Student('Gopi',"20")
# s1.stu_marks(220)
# s2.stu_marks(200)
#
# print(s1.student_name,s1.student_age)
# print(f"marks ={s1.stu_marks}")
# print(s2.student_name,s2.student_age)
# print(f"marks = {s2.stu_marks}")





#PROGRAM 3

# class Bank:
#     u_name=""
#     ac_num=0
#     ac_balance=0.0
#     def __init__(self,name,number,balance):
#         self.u_name=name
#         self.ac_num=number
#         self.ac_balance=balance
#     def Customer_details(self):
#         print(f"Customer name is {self.u_name} with Account Number {self.ac_num} and having bank balance of {self.ac_balance}")
# c1 =Bank('nag',11221122,8936473.01)
# c2=Bank('gopi',11585466,7346734473465737463785.87568)
# c3=Bank('tarun',3632725,38446347566565847.57557)
# c1.Customer_details()
# c2.Customer_details()
# c3.Customer_details()




#PROGRAM 4

class User:
    full_name=""
    email=""
    __password=""
    mobile_number=""
    def __init__(self,name,email,password):
        self.full_name=name
        self.email=email
        self.__password=password
    def update_name(self,new_name):
        self.full_name=new_name
    def get_name(self):
        return self.full_name
    def update_password(self,new_password):
        self.__password=new_password
    def update_mobile_number(self,new_number):
        self.mobile_number=new_number
