class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def description(self):
        return 'My name is {} and I am{}'.format(self.name,self.age)
    def sleep(self,hours):
        print('I sleep for {}'.format(hours))

class Student(Person):
    def __init__(self,name,age,university,degree):
        super().__init__(name,age)
        self.university=university
        self.degree=degree
    def description(self):
        return 'My name is {} and I am{}.I am at {} and have a {}'.format(self.name,self.age,self.university,self.degree)

class Worker (Person):
    def __init__(self,name,age,company,salary):
        super().__init__(name,age)
        self.company=company
        self.salary=salary
    def description(self):
        return 'My name is {} and I am{}.I am at {} and I earn {}'.format(self.name,self.age,self.company,self.salary)

    #def description(self):
        desc_person=super().desc()
        desc_worker=desc_person+''
        return desc_worker

p=Person('neil', 23)
s=Student('neil',23,'unisa','BA')
w=Worker("neil",36,'KPMG',6000)

print(p.description())
print(s.description())
print(w.description())
