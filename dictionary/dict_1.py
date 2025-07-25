# d={1:"amit" , 2:"ram" , 3:"sita"}
# print(d)

######empty dict
# d={}
# a={1:"amit" , 2:"ram" , 3:"sita"}
# d={"amit":1 , "ram":2 , "sita":3}
# print(a,d)

# (1,"pankaj")
# (2,"pankaj")               ----------> for pair of list we have to give ,,,,,,,  not ::
# (3,"pankaj")
# l=[(1,"pankaj"),(2,"pankaj"),(3,"pankaj")]
# print(l)
# d=dict(l)
# print(d)

# ###creating a dictionary by providing alist of keys
# d=dict.fromkeys(["ram",12.5,3])
# print(d)               -----> it is for only keys and none will print to the op

# d=dict.fromkeys(["ram",12.5,3] ,  5)
# print(d)                     -----> will give 5 to the value

# l=[(1,"ram" ),(1,"ram"  )]
# d=dict(l)
# print(d[1])      ------> doubt


# a={1:"amit" , 2:"ram" , 3:"sita"}
# print(a[3])             ----> accessing the value

# ###### another way of accessing meyhod is ((((  get))))
# a={1:"amit" , 2:"ram" , 3:"sita" , 4:5}
# print(a.get(4))

# a={1:"amit" , 2:"ram" , "sita":[1,2,3,4,"ram"] , 4:5}
# print(a.get("sita"))


# a={1:"amit" , 2:"ram" , "sita":[1,2,3,4,"ram"] , 4:5}
# print(a.keys())             # -----> to print keys
# print(a.values())    
# print(a.items())    



#######to iterate a dict

# d={1:"amit" , 2:"ram" , "sita":[1,2,3,4,"ram"] , 4:5}
# for x in d:                        # >>>>>>>>>>d[x]  gives values
    
#     print(x, ":",d[x])



#### update
# d={1:"amit" , 2:"ram" , "sita":[1,2,3,4,"ram"] , 4:5}
# a={1:"amit" , 2:"ram" , 3:"sita"}

# a.update(d)
# print(a)       ---------> in this a got updated and b remains the same
# print(d)


# s=input("enter your string")
# wordskilist=s.split()
# d={}
# for words in wordskilist:
#     if words in d:
#         d[words]=d[words]+1
#     else:                              ============> to print the no of words occered in a string
#         d[words]=1
# print(d)        
            
  # s=input("enter your string")
# wordskilist=s.split()
# d={}                        -----------> we can use GET FUNCTION alse o print the no of words occered in a string
# for word in wordskilist:
#     d[word]=d.get(word,0) +1
# print(d)    


      
# d={1:3,3:4}
# print(2 in d)    
# print(1 in d)    



##### print frequency of eack character
# s=input()
# d={}
# for ele in s:
#     if ele in d:
#         d[ele] += 1
#     else:
#         d[ele]=1    
# print(d)


# s = "GeeksforGeeks"
# freq = {}

# for c in s:
#     if c in freq:
#         freq[c] += 1
#     else:
#         freq[c] = 1

# print(freq)
