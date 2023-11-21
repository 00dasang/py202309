#HW_Student_grade_management
#readlines the file
lines = open("student.csv","r",encoding="utf8").readlines()

### class_student_grade ###
class Student:
    def __init__(self, name, korean, math, eng):
        self.name = name
        self.korean = korean
        self.math = math
        self.eng = eng

    def get_average(self):
        stu_average =  ((self.korean+self.math+self.eng)/3)
        print('---평점 및 성적---')
        print('name:',self.name)
        print('korean:', self.korean)
        print('math:', self.math)
        print('eng:', self.eng)
        print('average:', stu_average)
    
# get the input from user 
def get_user_input():
    name = input("input your name: ")
    korean = float(input("input your korean score: "))
    math = float(input("input your math score: "))
    eng = float(input("input your english score: "))
    return name, korean, math, eng 

name, korean, math, eng = get_user_input()

# making_the_instance_for_class
student_instance = Student(name, korean, math, eng)

# print the instance score
student_instance.get_average()


# 1.1 To do 1 _ save the student's grade in dictionary

students_grade = {}

for line in lines[1:]:
    separate_lines = line.strip().split(",")
    student_name = separate_lines[0]
    grades = []
    for grade_str in separate_lines[1:]:
        try:
            grade = float(grade_str)
            grades.append(grade)
        except ValueError:
            print(f'{student_name}의 성적 중 올바르지 않은 형식의 값이 있습니다')
            
    students_grade[student_name] = grades




# 1.3 To do 3 _ make the result file
result_file = open("average.txt","w",encoding="utf8")
result_file.write("-----학생들의 평균 점수-----\n")
for student,grades in students_grade.items():
    average = sum(grades)/len(grades)
    result_file.write(f'{student}의 평균 점수는 {average} 입니다.\n')
result_file.close()

#define the functions and call them

# 2.1 function_loadData
def loadData(lines):
    students_grade = {}
    student_list = []

    for line in lines[1:]:
        separate_lines = line.strip().split(",")
        student_name = separate_lines[0]

        ## Instance for class
        #student_instance = Student()
        #student_instance.name = student_name
        #student_instance.korean = float(separate_lines[1])
        #student_instance.math = float(separate_lines[2])
        #student_instance.eng = float(separate_lines[3])
        #student_list.append(student_instance)
        
        # Instance for class
        student_instance = Student(
            student_name,
            float(separate_lines[1]),
            float(separate_lines[2]),
            float(separate_lines[3])
        )
        student_list.append(student_instance)

        ## dictionary for the grade
        grades = [float(grade_str) for grade_str in separate_lines[1:]]
        students_grade[student_name] = grades

    return students_grade, student_list

# 2.2 function_getAverage
def getAverage(students_grade):
    print("-----학생들의 평균 점수-----")
    averages = []
    for student,grades in students_grade.items():
        average = sum(grades)/len(grades)
        averages.append((student, average))
    
    return averages



### call_the_functions ###
result_loadData = loadData(lines)
print(result_loadData)
print()


### call_the_functions_2 ###
result_getAverage = getAverage(result_loadData[0])
print(result_getAverage)
print()


# checking_class
print("---checking the grade from the class---")
for student_instance in result_loadData[1]:
    student_instance.get_average()