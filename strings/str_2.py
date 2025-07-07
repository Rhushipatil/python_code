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
s=input()
a=s.split()
update=[]
for word in a[:len(a)-1]:           # iterate over all but last
    update.append(word[0])
update.append(a[len(a-1)])    
print(''.join(update))