class Student:
    """
    Represents a student
    """
    school_name = "Example School"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
