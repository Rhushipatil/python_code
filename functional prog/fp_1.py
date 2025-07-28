# def factorial(n):
#     prod=1
#     for i in range(1,n+1):
#         prod=prod*i
#     return prod
    
# a=factorial(5)
# print(a)    

# for w in range(1,11):
#     print(factorial(w))        ------> using function to print factorial 1 to 10

# p=int(input("enter your no"))
# sum=0.0
# for r in range(1,p+1):
#     prod=1
#     for k in range(1,r+1):
#         prod=prod*k
#     prod1=1
#     for j in range(1,r+2):
#         prod1=prod1*j
#     sum=sum+prod/prod1        
# print(sum)


#### to check whether the no is prime or not


# def prime(n):
#     if n==1:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             break
#     else:
#         return True
#     return False   
    
    
# for i in range(1,101):
#     if prime(i):
#         print(i,"is prime")



# def even(n):
#     if n%2==0:
#         return "is even"
#     else:
#         return False
    
# for i in range(1,101):
#     if even(i):
#         print(i,"is even")    
        
        
# def odd(n):
#     if n%3==0:
#         return "is odd"
#     else:
#         return False
    
# for j in range(1,101):
#     if odd(j):
#         print(j,"is odd")            
        
        
        
        
# def twice(n):
#     n=2*n
#     return n          ---------->> in this 2 and 2 point same reference so it will show the same thing
# w=2
# twice(w)
# print(w)        





# def twice(l):
#     for i in range(len(l)):
#         l[i]=l[i]*2                  ------------------->> this will give us the double of that list it will change the value of list1
# l1=[1,2,3,4,5]
# twice(l1)
# print(l1)        

# def twice(n):
#     n=n*2              ---------> it will not work as it is a string
    
# w="ram"
# twice(w)
# print(w)    









#### local global


# def f():
#     a=10
#     a=a+2          ----------> not defined as a is in local variable
#     print(a)
# f()
# print(a)    

# a=10111111
# def f():
#     a1=10
#     print(a1)
# f()
# print(a)    


# x=10
# def s():
#     y=200
#     print(y)
#     print(x)

# x=400       ###### because here we updated global variable
# s()
# print(x)    

# x=10
# def s():
#     y=200
#     print(y)
#     print(x)
      
# s()           >>>>>>>>>>>>>. o/p===200,10,400
# x=400    
# print(x)    


