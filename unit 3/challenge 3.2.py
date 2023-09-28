"""
Implement a function called sort_student that takes a list of student object as input and sorts the
List based on their CGPA (cumulative Grade Point average) in descending order. Each student object
Has the following attributes:name (string),roll_number(string), and cgpa (float). Test the function
with different input lists of students.
"""

class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  #sort the list of students in descending order of CGPA 
  sorted_students = sorted(student_list, 
                           key=lambda student: student.cgpa, 
                           reverse=True)
  #Syntax-lambda arg:exp
  return sorted_students


#Example usage:
students = [
   Student("Nanthu", "A123", 8.8),
   Student("krish", "A124", 8.1),
   Student("priya", "A125", 9.4),
   Student("krishna", "A126", 7.6)
]

sorted_student = sort_students(students)

#Print the sorted list of students
for student in sorted_student:
  print("Name:{},Roll number:{},CGPA:{}".format(student.name,
                                                
student.roll_number,                                                
  
student.cgpa))






