class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_in_progress = []

    def average_grade_for_course(self):
        #Расчет среднего балла за курс по каждому лектору
        sum_num = 0
        sum_num_len = 0
        for grade in self.grades.values():
            sum_num_len += len(grade)
            for i in grade:
                sum_num += i
        if sum_num_len:
            return round(sum_num / sum_num_len, 1)
        else:
            return 'Оценок нет'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade_for_course()}'

    def __lt__(self, other):
        #Сравнение лекторов по оценке
        return self.average_grade_for_course() < other.average_grade_for_course()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        #Выставление оценок студентам
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_hw(self, lecturer, course, grade):
        #Выставление оценок лекторам
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_homework_grade(self):
        #Расчет среднего балла за домашнее задание каждого студента по всем курсам
        sum_num = 0
        sum_num_len = 0
        for grade in self.grades.values():
            sum_num_len += len(grade)
            for i in grade:
                sum_num += i
        if sum_num_len:
            return round(sum_num / sum_num_len, 1)
        else:
            return 'Оценок нет'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_homework_grade()}\nКурсы в процессе обучения: {" ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}'

    def __lt__(self, other):
        return self.average_homework_grade() < other.average_homework_grade()

student_list = [] #Добавление студентов в список
student_list.append(Student('Питер', 'Паркер', 'Мужской'))
student_list.append(Student('Наташа', 'Романова', 'Женский'))

student_list[0].courses_in_progress += ['Python']
student_list[0].finished_courses += ['Git']
student_list[0].courses_attached += ['Python', 'Git' ]

student_list[1].courses_attached += ['Python', 'Git' ]
student_list[1].courses_in_progress += ['Python']
student_list[1].finished_courses += ['Git']

lecturer_list = [] #Добавление лекторов в список
lecturer_list.append(Lecturer('Стивен', 'Стрэндж'))
lecturer_list.append(Lecturer('Тони', 'Старк'))

lecturer_list[0].courses_in_progress += ['Python', 'Git']
lecturer_list[1].courses_in_progress += ['Python', 'Git']

reviewer_list = [] #Добавление проверяющих в список
reviewer_list.append(Reviewer('Ник', 'Фьюри'))
reviewer_list.append(Reviewer('Роуди', 'Роудс'))
reviewer_list[0].courses_attached += ['Python', 'Git' ]
reviewer_list[1].courses_attached += ['Python', 'Git' ]

student_list[0].rate_hw(lecturer_list[0], 'Python', 10)
student_list[0].rate_hw(lecturer_list[1], 'Git', 10)
student_list[1].rate_hw(lecturer_list[0], 'Python', 9)
student_list[1].rate_hw(lecturer_list[1], 'Git', 9)

reviewer_list[0].rate_hw(student_list[0], 'Python', 8)
reviewer_list[1].rate_hw(student_list[0], 'Python', 8)
reviewer_list[0].rate_hw(student_list[1], 'Python', 7)
reviewer_list[1].rate_hw(student_list[1], 'Python', 7)

print(student_list[0])
print(student_list[1])
print(reviewer_list[0])
print(reviewer_list[1])
print(lecturer_list[0])
print(lecturer_list[1])
print(lecturer_list[0] < lecturer_list[1])
print(student_list[0] > student_list[1])

def total_average_homework_grade_all_students (student_list, course):
    #Расчет общего балла по домашнему заданию всех студентов за конкретный курс
    all_grades = []
    for student in student_list:
        for key, value in student.grades.items():
            if key == course:
                all_grades.extend(value)
            return sum(all_grades) / len(all_grades)

print(total_average_homework_grade_all_students(student_list, 'Python'))

def total_average_grade_for_course (lecturer_list, course):
    # Расчет общего балла по лекциям всех лекторов за конкретный курс
    all_grades = []
    for lecturer in lecturer_list:
        for key, value in lecturer.grades.items():
            if key == course:
                all_grades.extend(value)
            return sum(all_grades) / len(all_grades)

print(total_average_grade_for_course(lecturer_list, 'Python'))








