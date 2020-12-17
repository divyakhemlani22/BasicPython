
# Creating a student class
class Student:
    # initialise a function and define what functions they should have
    def __init__(self, name, major, gpa, is_on_probation):
        # Self refers to the actual object
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
