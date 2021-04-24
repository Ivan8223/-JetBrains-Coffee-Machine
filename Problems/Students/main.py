class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.student_id = f"{self.name[:1]}{self.last_name}{self.birth_year}"

    def get_student_id(self):
        return self.student_id


def main():
    new_student = Student(
        input(),
        input(),
        input(),
    )

    print(new_student.get_student_id())


if __name__ == '__main__':
    main()
