# TASK 1

# class Cat:
#     def __init__(self):
#         self.name = None
#         self.age = None
#         self.favorite_food = None

#     def get_name(self):
#         return self.name

#     def get_age(self):
#         return self.age

#     def get_favorite_food(self):
#         return self.favorite_food

#     def set_name(self, new_name):
#         self.name = new_name

#     def set_age(self, new_age):
#         self.age = new_age

#     def set_favorite_food(self, new_favorite_food):
#         self.favorite_food = new_favorite_food


# TASK 2

import random

class Cat:
    def __init__(self, name=None):
        self.age = random.randint(5, 10)
        self.name = name
        self.favorite_food = None
        self.names_history = [name] if name else [None]
        self.speak_count = 0

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_favorite_food(self):
        return self.favorite_food

    def set_name(self, new_name):
        self.name = new_name
        self.names_history.append(new_name)

    def get_names(self):
        return self.names_history

    def speak(self, sound="meow"):
        print(sound)
        self.speak_count += 1
        if self.speak_count % 5 == 0:
            self.age += 1

    def get_average_name_length(self):
        if not self.names_history:
            return 0
        return sum(len(name) for name in self.names_history if name is not None) / len([name for name in self.names_history if name is not None])
