# class demo:
#     def __init__(self):
#         self.x=12
#         self.y=19

# d=demo()
# print(d.x)     

# print(d.__dict__)       # =============> for dictionary

 
 
 
# class demo:
#     def __init__(self):
#         self.x=12
#         self.y=19
#     def fun(self):
#         self.z=100    


# d1=demo()
# d2=demo()
# d1.fun()
# print(d1.__dict__)


##### employee data

# class employee:
#     def __init__(self):
#         self.__name="ram"                    ### giving __ make the variablr private
#         self.age=44
#     def marriage(self):
#         self.wife="sita"  
   
   
# d=employee()        
# d.marriage()
# print(d.__dict__)          

#### to add complex no



# class Comp:
#     def __init__(self, real=0, imag=0):
#         self.real = real
#         self.imag = imag

#     def print(self):
#         print(self.real, "+", self.imag, "i")
    
#     def adding(self,dusra_comp):
#         self.real=self.real+  dusra_comp.real
#         self.imag=self.imag+  dusra_comp.imag

# # Creating object with proper arguments
# s = Comp(2, 3)
# s1= Comp(5,6)
# # Calling the method
# s.print()

# s.adding(s1)
# s.print()                           #>>>>>>>>>>>why?????







#### fraction
class fraction:
    def __init__(self,neo,deno):
        self.neo=neo
        self.deno=deno
    def print(self):
        print(self.neo, "/" , self.deno)
     
    def normal(self):                                               ####normalize    
        min_value=min(self.neo,self.deno)
        while min_value>1:
            if self.neo%min_value==0 and self.deno%min_value==0:
                break
            min_vlaue=min_value-1
        self.neo=self.neo//min_value    
        self.deno=self.deno//min_value    
        
        
        
        
        
        
        

w=fraction(2,6)
w.normal()
w.print()