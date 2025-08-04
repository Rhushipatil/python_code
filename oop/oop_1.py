# class teacher:
#     '''this is a class template'''
#     def __init__(self):
#         self.name="ram"
#         self.roll=33
#         print("constructor executes")
#     def display(self):
#         print(self.name)
#         print(self.roll)
        
# t=teacher()
# t1=teacher()
# t.display()        



# class teacher:
#     '''this is a class template'''
#     def __init__(self):
#         self.name="ram"
#         self.roll=33
#         print("constructor executes")
#     def display(self):                     ------> this way is a wrong way to initilize it
#         print(self.name)
#         print(self.roll)
        
# t=teacher()
# t1=teacher()
# t3=teacher()        



# class teacher:
#     '''this is a class template'''
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("constructor executes")
#     def display(self):
#         print(self.name)
#         print(self.age)

# t=teacher("ram",33)
# t1=teacher("pankaj",98)        
 
# t.display()
# t1.display()



#### static 
# class teacher:
#     institute="scoe"
#     def __init(self):
#         self.name="ram"
#         self.age=20
        
# print(teacher.institute)            ====> it is a class related property not a obj relayed



######## class method
# @classmethod
# def display_classinfo():
#     print(       ,institute)
    
    
class teacher:
    @classmethod
    def fun(cls):
        print(id(cls))    # class level object reference
print(id(teacher))        
   
   
   ## fun is a class method
   
print(teacher.fun()) 
   
   