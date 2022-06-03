class Person:

    #create your class here
    def setValue(self, name, age):
        self.name = name
        self.age = age
    def getValue(self):
        print("The name of the person is {} and the age is {}.".format(self.name, self.age))


#Driver code goes here.
name = input()
age = input()
obj = Person()
obj.setValue(name, age)
obj.getValue()