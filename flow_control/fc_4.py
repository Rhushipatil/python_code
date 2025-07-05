################ nested loop
# for i in range(1,4):
#     for j in range(1,5):
#         print(j ,end=" ")


# for i in range(1,3):
#     for j in range(1,5):   ---->o/p--->1-1
#                                        1-2
#                                        1-3
#                                        1-4
#                                        2-1
#                                        2-2
#                                        2-3
#                                        2-4
#         print(i,j)

# for i in range(1,4):
#     for j in range(1,5):         # ------------> this last print will give a space   1 1 1 2 1 3 1 4 
#                                                                                      2 1 2 2 2 3 2 4 
#                                                                                      3 1 3 2 3 3 3 4 
#         print(i,j ,end=" ")
#     print()  
    
    
# for i in range(1,4):
#     for j in range(1,5):         
#         print(i,j ,sep='',end=" ")         ------> sep give space i the intervals    11 12 13 14 
#                                                                                      21 22 23 24
#                                                                                      31 32 33 34
#     print()   


#########patterns (looping questions)
# for i in range(1,5):
#     print("ram", end="   ")     -------->end print the text sidewise(row <--->) & normal print print all elemrnt in seprate coloumn|
    
    
    
# for row in range(1,6):
#     for col in range(1,row+1):
#         print(col,sep='',end='')
#     print()
         
    
    
    
# for row in range(10,1,-2):
#     for col in range(1,row+1):
#         print(col,end=" ")         -------> reverse no
#     print()      


# size=6

# for row in range(size):
#     for col in range(size):
#         print('*',end=" ")          ------> square
#     print()


# length=5
# width=20
# for row in range(length):
#     for col in range(width):
#         print('*',sep='',end="")
#     print()    


#####HOMEWORK
# for row in range(6,1,-1):
#     for col in range(1,row-1):                                 1 2 3 4 
#                                                                1 2 3 
#                                                                1 2 
#                                                                1 
#         print(col,sep='',end=' ')
#     print()



# for row in range(1,5):                                    *
#                                                             ***
#                                                                 *****
#                                                                     *******
#     print(" " *(4*row),end='')               
#     print("*"*(2*row-1))
    
    
# for upper triangle
# for row in range(1,5):
#     print(" "*(4-row),end='')
#     print("*"*(2*row-1),)
#   #for lower triangle
# for row in range(5,0,-1):
#      print(" "*(4-row),end='')
#      print('*'*(2*row-1))
  
    
# for row in range(1,6):
#     print(" "*(5-row),end='')                                1
#                                                             12
#                                                            123
#                                                           1234
#                                                          12345
#     for col in range(1,row+1):
#         print(col,end='')    
#     print()
    