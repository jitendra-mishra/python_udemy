class Teacher:

    def __init__(self, full_name, teacher_id):
        self.full_name = full_name
        self.teacher_id = teacher_id

    def welcome_students(self):
        print(f"I am your teacher. My name is {self.full_name}")

class ScienceTeacher(Teacher):

    def welcome_students(self):
        super().welcome_students()
        print(f"Welcome to class of Science. I am {self.full_name}")

my_science_tacher = ScienceTeacher("Jitendra Mishra", "A101")
my_science_tacher.welcome_students()