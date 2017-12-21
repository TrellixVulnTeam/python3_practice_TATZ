class Dog:
    """模拟小狗"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+'is now sitting')

    def roll(self):
        print(self.name.title() +'is rolling')


my_dog = Dog('black', 6)

print('my dog is name is '+my_dog.name)
print('my dog is age is '+str(my_dog.age))

my_dog.sit()
my_dog.roll()

   



