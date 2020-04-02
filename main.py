class Employee():
    def __init__(self,name,age,job):
        self.name = name
        self.age = age
        self.job = job


class HourlyEmployee(Employee):
    def __init__(self,name,age,job,hourly_salary):
        super().__init__(name,age,job)
        self.hourly_salary = hourly_salary
    
    def getHourlySalary(self):
        return self.hourly_salary

obj = HourlyEmployee("Allan",25,"Software Engineer",3000)
print(obj.getHourlySalary())
     