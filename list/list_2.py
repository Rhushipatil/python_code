## aliasing
# # =====>
# x=[10,20,30,40]
# y=x
# print(id(x))
# print(id(y))           ---->same


#### list of list
# l=[[1,2,3],[4,3,2],[2.,1,2]]
# print(l[1][1])

dimension=input().split()
m=int(dimension[0])
n=int(dimension[1])
l=[]
for i in range(m):
    ne_row=[int(i) for i in input().split()]
    l.append(ne_row)
    print(l)