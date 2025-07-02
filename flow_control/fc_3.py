###to write code for a^b
##4^3
# prod=1
# for i in range(1,4+1):
#     prod=prod*3
# print(prod)

##a^7
# a=int(input("enter a:"))
# prod=1
# for i in range(1,a+1):
#      prod=prod*7
# print(prod)

##a^b
# a=int(input("enter a:"))
# b=int(input("enter b:"))
# prod=1
# for i in range(1,a+1):
#     prod=prod*b
#     print(prod)


##table of 5
# a=int(input("enter a:"))
# prod=1
# for i in range(1,10+1):
#     prod=i*a
#     print(prod)

#########armstrong number

# n=int(input("enter a:"))
# a=n
# prod=1
# sum=0
# while n!=0:
#     last=n%10
#     cube=last*last*last
#     sum=sum+cube
#     n=n//10
# if sum==a:    
#     print("armstrong")
# else:
#     print("not armstrong")    


###to finf no of digit

# n=int(input("enter a:"))
# a=n
# count=0
# sum=0
# while n!=0:
#     last=n%10
#     sum=sum+last
#     count=count+1
#     n=n//10                --------->for count print_count,for sum print sum
# print(count)


###############   continue

# for i in range(1,11):
#     print("ram")                  ------>continue the loop 
#     if i%3==0:
#         continue
#     print(i)


######break
for i in range(1,11):
    print("ram")                  
    if i%3==0:
        break              -----------------> break the loop and not print i (the next line)
    print(i)


