import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"


class Student:
    def __init__(self, name, surname, index):
        self.name = name
        self.surname = surname
        self.index = index
        self.courses = dict()

    def add_course(self, course_name, points):
        self.courses[course_name] = self.calculate_grade(points)

    def calculate_grade(self, points):
        total_sum = sum(num for num in points)
        if total_sum == 0 or total_sum <= 50:
            return 5
        elif 50 < total_sum <= 60:
            return 6
        elif 60 < total_sum <= 70:
            return 7
        elif 70 < total_sum <= 80:
            return 8
        elif 80 < total_sum <= 90:
            return 9
        else:
            return 10

    def __str__(self):
        res = f"Student: {self.name} {self.surname}\n"
        for course_name in self.courses.keys():
            res += f"----{course_name}: {self.courses[course_name]}\n"
        return res


if __name__ == "__main__":
    students_dict = dict()
    while True:
        inpt = input()
        if inpt == "end":
            break
        inpt = inpt.split(",")
        name = inpt[0]
        surname = inpt[1]
        index = inpt[2]
        if index not in students_dict:
            student = Student(name, surname, index)
            student.add_course(inpt[3], [int(inpt[4]), int(inpt[5]), int(inpt[6])])
            students_dict[index] = student
        else:
            students_dict.get(index).add_course(inpt[3], [int(inpt[4]), int(inpt[5]), int(inpt[6])])

    for student in students_dict.values():
        print(student)
