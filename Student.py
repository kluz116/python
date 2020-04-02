class Student():
    
    def __init__(self,name,age,location):
        self.name = name
        self.age = age
        self.location = location
    
    def getNameAge(self,name,age):
        response = "The Name Is {} and Age Is {}"
        return response.format(self.name,self.age)

obj = Student('Allan Musembya',12,'Jinja')

print(obj.getNameAge(obj.name,obj.age))