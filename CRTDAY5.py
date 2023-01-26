#INHERITANCE
#TYPES OF INHERITANCE:

# 1.Single inheritance
# 2.Multi level inheritance
# 3.Hierarchical inheritance
# 4.Multiple inheritance
# 5.Hybrid inheritance

#Single inheritance
# class A:
#     name="mukesh"
#     age=36
# class B(A):
#     age=10
# obj=B()
# print(obj.age)
# print(obj.name)

#Multi level inheritance

# class Country:
#     Country_Name="India"
#
# class State(Country):
#     State_Name="Andhra Pradesh"
# class District(State):
#
#     District_Name="East Godavari"
# obj=District()
# print(f"District name is {obj.District_Name},and State name is {obj.State_Name}, and Country Name is {obj.Country_Name}")


#Hierarchical Inheritance

class Person:
    Name=""
    age=0
class Country(Person):
    Country_Name="India"
    Prime_Minister="Narendra Modi"
class State(Person):
    State_Name="Andhra Pradesh"
    Chief_Minister="Jagan"
class District(Person):
    District_Name="East Godavari"
obj1=District()
obj2=State()
obj3=Country()
print(f"Country name is {obj3.Country_Name} and PM is {obj3.Prime_Minister}")
print(f"State name is {obj2.State_Name} and CM is {obj2.Chief_Minister}")



#MULTIPLE INHERITANCE
# class P1:
#     def m1(self):
#         print("In parent class 1")
# class P2:
#     def m1(self):
#         print("In parent class 2")
# class P3(P2,P1):
#     pass
# obj=P3()
# print(obj.m1())

