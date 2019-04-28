
#Define a class, with one function with two parameters and one class variable 
class People:
    number = 12
    def __init__(self,name,age):
        
        self.name = name
        self.age = age
p1 = People("John",36)
print(p1.name)
print(p1.age)
print(People.number)

#Define a function which can compute the sum of two numbers.
def Totals(x,y):
    total = x + y
    return total
sum1 = Totals(12,12)
print(sum1)
    
#Define a function that will accept two strings and print the string that is longer
def PickLonger(string1,string2):
    
    if len(string1)>len(string2):
        
        return(string1)
    
    if len(string2)>len(string1):
                        
        return(string2)
stringz = raw_input("Please input first string")
stringy = raw_input("Please input second string")

funn = PickLonger(stringz, stringy)
print(funn)
