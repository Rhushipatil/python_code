###   WHILE LOOP  [JAB-TAK ---->WHILE MEANING]

# for i in range(1,6):
#     print(i)

# i=1
# while i<=5:
#     i=i+1  ----> this will print 2,3,4,5,6 as it is before print
#     print(i)
    # i=i+1 ----> this is correct
    
    
# i=1
# prod=1
# while i<=5:
#     prod=prod*i       --------------------> doubt(how  )
#     i=i+1
#     print(prod)
    
# n=int(input("enter the no to finf factorial :")) 
# i=1
# prod=1
# while i<=n:
#     prod=prod*i
#     i=i+1
#     print(prod)


#float to integer -----> //
# n=1234
# n=n//10
# print(n)


# n=int(input("n=n//10 :"))
# count=0
# while n!=0:
#     n=n//10                    ------------> intro of count
#     count=count+1
# print("the no of digit present are :",count)
    
    
#####   factors of a no
# n=int(input("to finf factors of a givrn no :"))
# count=0
# for i in range(1,n+1):                     -----------------> to find factors
#     if n%i==0:
#         print(i)

# n=int(input("to finf factors of a givrn no :"))
# l=[]
# for i in range(1,n+1):
    
#      if n%i==0:
#          l.append(i)               ---------------> to append factors in a list
#          print(i)
# print(l)         
# print(type(l))

# n=int(input("enter the no to finf if its a perfect no  "))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
#         print(i)                -------------> for perfect no
# if sum==n:
#     print("it is a perfect no")
# else:
#     print("not a perfect no")    
        
########### the sum of given digits


# num = input("Enter a number: ")
# total = 0

# for digit in num:
#     total += int(digit)

# print("Sum of digits:", total)

# num = input("Enter a number: ")
# s=0
# for i in num:
#     s =s+int(i)
# print(s)

#n = int(input("Enter a number: "))
# i=1
# for n in range(1,n+1):
#     i=i*n
#     print(i)

#################to find strong number
n = int(input("Enter a number: "))
# prod=1
# for i in range(1,n+1):
#     prod=prod*i
#     print(prod)

a=n
sum=0
while n!=0:
    last=n%10
    prod=1
    for i in range(1,n+1):
        prod=prod*i
sum=sum+prod
n=n//10
if sum==n:
    print("strong no")
else:
    print("nit strong")       
