# TASK 1

# from Cat import Cat
# from Data import Data

# cat = Cat()
# print("Name is currently " + str(cat.get_name()))

# cat.set_name("Garfield")

# print("Name has been changed to " + str(cat.get_name()))

# data = Data("database")

# data.insert("Cat", cat)

# TASK 2

from Cat import Cat
from Dog import Dog
from Data import Data

# Demonstrate Cat functionality
cat = Cat("Whiskers")
print("Initial name:", cat.get_name())
print("Initial age:", cat.get_age())

cat.speak()
cat.speak("purr")
cat.speak("hiss")
cat.speak()
cat.speak()

cat.set_name("Garfield")
cat.speak("meow")
print("Names history:", cat.get_names())
print("Current name:", cat.get_name())
print("Current age:", cat.get_age())
print("Average name length:", cat.get_average_name_length())

# Demonstrate Data functionality
data = Data("database")
data.insert("Cat", cat)

# Demonstrate Dog functionality
dog = Dog("Rex")
print("Initial name:", dog.get_name())
print("Initial age:", dog.get_age())

dog.speak()
dog.speak("bark")
dog.speak("growl")
dog.speak()
dog.speak()

dog.set_name("Buddy")
dog.speak("woof")
print("Names history:", dog.get_names())
print("Current name:", dog.get_name())
print("Current age:", dog.get_age())
print("Average name length:", dog.get_average_name_length())

data.insert("Dog", dog)
