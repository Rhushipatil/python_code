#1 operand  +7,+9

# binary operator    ==> 2+3,3-5,1**3,10//5
# [first value] if (condition) ----> else [second value]

# a=10
# b=20
# c= 100 if a<b else 1000
# print(c)

####Q]take two no and print largest among them

# a=int(input("enter first no"))
# b=int(input("enter second no"))
# if a==b:
#     print(" both are equla")
# elif a<b:
#     print(b," is greater")
# elif a>b:
#      print(a," is greater")


#### q] take three no and print the largest one

# a=int(input("enter first no"))
# b=int(input("enter second no"))
# c=int(input("enter third no"))
# if a==b and c ==b :
#     print(" they are equla")
# elif a>b and a>c:
#     print(a," is greater")
# elif b>a and b>c:
#      print(b," is greater")
# else:
#      print(c," is greater")     

#  another approach 
# a=int(input("enter first no"))
# b=int(input("enter second no"))
# c=int(input("enter third no"))
# d= a if a>b and a>c else(b if b>c else c)  ======> easy approach
# a if a>b and a>c      else  b if b>c    else c         ##############

#a=10
#b=20            ====> a,b =10,20


###### IS operator     =====> compare th id's of the variabies

#a,b = 10,30
# print(id(a))
# print(id(b))
# print(id(a)==id(b))  ====> false

# print(a is b) ==============> is operator compares the id of the variables

#############  membership operator (in)

# s="ram is a good boy"
# print('r' in s)
# print('R' in s)

# l=[1,3,4,"kiran"]
# print("kiran" in l)

