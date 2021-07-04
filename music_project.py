class MusicSchool:

    students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
                "Talina": [28, "555-765-452", ["Cello"]],
                "Eric":   [12, "583-356-223", ["Singing"]]}

    def __init__(self, working_hours, revenue):
        self.working_hours = working_hours
        self.revenue = revenue

    def print_student(self, name):
        if name in MusicSchool.students.keys():
            print("Student: {} who is {} years old and is taking {}".format(name, MusicSchool.students[name][0], MusicSchool.students[name][2]))

    def print_students_data(self):
        for student in MusicSchool.students:
            self.print_student(student)

    def add_student(self, name, data):
        MusicSchool.students[name] = data

my_school = MusicSchool(8, 100)
my_school.print_students_data()
my_school.print_student("Gino")
my_school.add_student("Jack", [60, "562-234-234", ["Piano"]])
