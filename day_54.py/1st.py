from collections import namedtuple
n = int(input())
Student = namedtuple('Student', input().split())
total_marks = 0
for _ in range(n):
    row = input().split()
    student_data = Student(*row) # Unpacks the row list into the namedtuple
    total_marks += int(student_data.MARKS)
print("{:.2f}".format(total_marks / n))
