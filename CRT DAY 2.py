#a=int(input('enter a number'))
# if a%2==0:
#     if a==0:
#         print("sunday")
#     if a==1:
#         print("Monday")
#     if a==2:
#         print("Tuesday")
#     if a==3:
#         print("Wednesday")
# else :
#     print("Enter a correct number")

# if a>=0 and a<20:
#     if a%2==0:
#         print("yes")
#     else:
#         print("No")
# if a>=20 and a<30:
#     print("Normal")
# else:
#     if a%2==0:
#         print("Yes")
#     else:
#         print("No")
#

#DICTIONARY
#
# d={48:['nag','cse-ds']}
# print(d[48])

# d={}
# d.update({448:['Nag','cse-ds'],449:['Gopi','cse-ds']})
# print(d[448])



#Loops

# print(list(range(1,10,2)))
#  1= starting   , 10= ending   , 2= step size

# for i in range(1,10):
#     print("Nag")
# print ("gopi")


# a=[40,30,54,21,33,45,67]
# for i in a:
#      print(i*i)
# for i in range(0,len(a),2):
#     print(a[i])


# a=int(input("enter a number"))
# f=False
# lst=[10,21,33,22,58,76,94]
# for i in range(0,len(lst)):
#     if a==lst[i]:
#         d=i
#         f=True
#         break
# if(f):
#     print(d)
# else:
#     print("invalid")




# a=[i for i in range(1,101) if i%7==0 and i%11==0]
# print(a)


#WHILE LOOP

# a=[10,20,32,21,32,43]
# for i in range(len(a)-1,-1,-1):
#     print(a[i])



l=[]
n=int(input('enter a number'))
print("enter ",n,"numbers")
for i in range(n):
    num=int(input())
    l.append(num)
positive=0
negitive=0
for i in range(0,len(l)):
    if l[i]<0:
        negitive+=l[i]
    else:
        positive+=l[i]
print(positive)
print(negitive)
