# practice module import the class
from student import Student, get_user_input

# separate the section from module file and import file
print()
print()
print()
print()
print("result of module program")
# This part is for increased visibility

# get average with using module
# get the input for test
test_student = Student("module_Seongjun", 100, 100, 100)
test_student_2 = Student("module dain", 100, 100, 100)

# print the average
test_student.get_average()
test_student_2.get_average()