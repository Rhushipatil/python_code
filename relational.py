#<,<=,>,>=
print(bool(10<20))
print(bool(10>20))
print(bool(10==20))
print(bool(10<=10))

# for complex
a=1+2j
b=2+3j
print(a+b)
#print(a<b) TypeError: '<' not supported between instances of 'complex' and 'complex'
#print(a>b)
#print(a<=b)

a="rhushi"# r comes later thaa p so true
b="patil" # and a<b will falsw because pcome first  than r
print(a>b)
print(a<b)