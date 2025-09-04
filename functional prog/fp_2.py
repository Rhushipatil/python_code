#### Argumentsz
# #can we return more than one value by a function
# def f(a,b):
#     '''this is function returning sum and difference'''
#     return a+b , a-b    

## x,y=f(10,20)
# print(x,y)

# ##to call docstrinf we have to erite function name inthis case[f]

# print(f.__doc__)



####### positional arguments

# def f(a,b,c):
#     return(a+b*c)

# ##whenever we csll a argument 3 values are always requrred
# #input matters
# print(f(10,20,30))





#keyword argument                      ## at the time of call we can give specific to every specific word
## order atter nahi karta
# def f(a,b,c,d):
#     return a*b/c-d

# print(f(d=40,c=30,b=20,a=10)) 
            


#### default argument
## in this case c is taken zero
# def sum(a,b,c=0):       ## c=0 is a default argument
#                           ## default must after positional argument
#     return a+b+c

# print(sum(10,20))



## for any no of argument
def f(*n):
    sum=0
    for ele in n:
        sum=sum+ele
    return sum             
        
print(f(1,5,6,8)   )     

# def f(*n):
#     sum=1
#     for ele in n:
#         sum=sum*ele
#         print(sum)             
        
# f(1,5,6,8)  

# def f(*n):
  
#     for ele in n:
        
#         print(ele)             
        

# f(1,5,6,8,"ram",[1,2,3],(2,"raj"))  
