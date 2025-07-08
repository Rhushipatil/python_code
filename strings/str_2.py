### SPLIT Function

# s="my name is rhushi"
# l=s.split()
# print(l)

# a="22/1/2025"
# l=a.split('/')
# print(l)


# l=['my', 'name', 'is', 'rhushi']
# a=' '.join(l)
# print(a)

# l=['my', 'name', 'is', 'rhushi']
# a=' --'.join(l)
# print(a)


### print even length words in string
# s="my name isa rhushi"
# for word in s.split():                 -----------> imp
#     if len(word)%2==0:
#         print(word)


## rhushi vikas patil----->r v patil
# s=input()
# a=s.split()
# update=[]
# for word in a[:len(a)-1]:           # iterate over all but last
#     update.append(word[0])
# update.append(a[len(a)-1])    
# print(''.join(update))



# s=input()
# a=s.split()
# l=[]
# for word in a[:len(a)-1]:
#     l.append(word[0])
# l.append(a[len(a)-1])
# print(" ".join(l))    

# s='rhushi v patil'
# a=s.find('h')
# print(a)                          ---------->find & rfind 

# s=input().split()
# l=[]
# for word in s:
#     l.append(word[::-1])
# print(" ".join(l))                        #======> reverse word rhushi v pail
#                                                       ihsuhr v litap


# s="my name is rhushi"     =====>MY NAME IS RHUSHI
# print(s.swapcase())



# s="my name is rhushi"
# print(s.islower())   # True
# print(s.isupper())   # False
# print(s.capitalize())# My name is rhushi
# print(s.title())     # My Name Is Rhushi
# print(s.upper())     # MY NAME IS RHUSHI
# print(s.lower())     # my name is rhushi

# s="my name is rhushi"
# print(s.count('h'))

