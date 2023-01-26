#DICTIONARIES
# lst=[]
# d = {}
# for i in range(0,5):
#     a=int(input())
#     b=int(input())
#     d.update({'key1':a})
#     d.update({'key2':b})
#     lst.append(d)
# print(lst)


#METHOD 2
# l=[]
# for i in range(5):
#     d={
#         'key1':input('Enter 1st value'),
#         'key2':input('Enter 2nd value')
#     }
#     l.append(d)
# print(l)


#USERNAME AND PASSWORD

# db=[{'123':'abc'},
#     {'xyz@example.com':'123'},
#     {'a123@example.com':'qwertyuiop'},
#     {'zxcv@example.com':'1234567890'}
# ]
# un=input('Enter a User Name:')
# ps=input('Enter a Password')
# db1={
#     un:ps
# }
# if db1 in db:
#     print('found')
# else:
#     print('not found')


#SIGNUP
# lis=[]
# a=int(input("enter how many signups"))
# for i in range(a):
#     print('Enter ',a, 'number of usernames and passwords')
#     a = input("Enter User name")
#     b = input("password")
#     dic={a:b}
#     lis.append(dic)
# print(lis)


#ND ARRAY
#
# l=[]
# n=int(input('enter n numbers'))
# for i in range(5):
#     a=input('enter a number')
#     l.append(a)
# print(l)


#SUM OF 2 ARRAYS
# k=[]
# a=[]
# c=int(input("Enter a n-dimensional array"))
# for i in range(c):
#     li=[]
#     for j in range(c):
#         b=int(input('enter a number'))
#         li.append(b)
#     a.append(li)
# print(a)
# a1=[]
# c1=int(input("Enter a n-dimensional array"))
# for i in range(c):
#     li1=[]
#     for j in range(c):
#         b1=int(input('enter a number'))
#         li1.append(b1)
#     a1.append(li1)
# print(a1)
#
# for i in range(2):
#     li2=[]
#     for j in range(2):
#         m=(a1[i][j]+ a[i][j])
#         li2.append(m)
#     k.append(li2)
# print(k)


#LIST SLICING

# l=[1,2,3,4,5,6,7,8,9,0]
# print(l[::-1])
# for i in range(len(l)-1,-1,-1):
#     print(l[i],end=' ')



#WRITE A PROGRAM TO WRITE 25 NUMBERS IN FIBANOCI SEARIES
# a=0
# b=1
# c=0
# count=0
# while(count<25):
#     print(b)
#     c=a+b
#     a=b
#     b=c
#     count+=1



# a=20
# # print("the sum of {} is {:.2f"}".format(a,a*a))
# print(f"the sun of {a} is {a*a}")


#EXCEPTION HANDLING
# try:
#     a=int(input("enter a num"))
#     b=int(input("enterr a num"))
#     print(a/b)
# except:
#     print("b dont allow 0 value")







#CALCULATOR PROGRAM

# d=int(input(("Select an operator from the following - 1(+) 2(-) 3(*) 4(%)")))
#
# if d==1:
#     a = int(input("Enter operand num 1:"))
#     b = int(input("enter operand num 2:"))
#     c=a+b
#     print(c)
# elif d==2:
#     a = int(input("Enter operand num 1:"))
#     b = int(input("enter operand num 2:"))
#     sub=a-b
#     print(sub)
# elif d==3:
#     a = int(input("Enter operand num 1:"))
#     b = int(input("enter operand num 2:"))
#     mul=a*b
#     print(mul)
# elif d==4:
#     a = int(input("Enter operand num 1:"))
#     b = int(input("enter operand num 2:"))
#     try:
#         div=a/b
#         print(div)
#     except:
#         print("Enter an value except '0'for b ")
# else:
#     print("Enter Correct operator number")
#
# try:
#     a=int(input())
#     b=int(input())
#     c=int(input())
#     d=int(input())
#     e=int(input())
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(e)
# except:
#     print("enter integer number only")





#FUNCTIONS


# a=int(input("Enter a num"))
# b=int(input('enter a num'))
# def add(a,b):
#     return(a+b)
# print(add(a,b))


#PRIME NUMBERS
# def prime(a):
#     for i in range(2,a):
#         if a%i==0:
#             return False
#         else:
#             return True
#
# print(prime(169))
#
#
#PRIME NUMBERS 2ND METHOD
# def prime(a):
#     for i in range(2,a//2):
#         if a%i==0:
#             return False
#         else:
#             return True



# def add(a,b,c,d):
#     print(a,b,c,d)
#
# add(a=10,b=20,c=30,d=40)



#VARIABLE LENGHT ARGUMENT




# def div(a,b):
#     return(a/b)
# print(div(2,3))







# a=input("")
# print(a.swapcase())


# a=int(input())
# for i in range(a):
#     sn=input('enter name')
#
#     rn=int(input('enter rn'))
# dic={}
# dic[sn]=rn
# print(dic)



#TYPES OF FUNCTIONS

# 1.Regular function
# 2.Default value funtion
# 3.Keyword argument function
# 4.Variable length function



#REGULAR FUNCTION
# a=10
# b=20
# def new(a,b):
#     return(a+b)
# print(new(a,b))


#KEYWORD ARGUMENT FUNCTION
# def add(a,b,c):
#     print(a,b,c)
# add(a=1,c=20,b=30)





