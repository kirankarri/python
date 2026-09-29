
import random
numbers = [1,2,3]
new_number = [number+1 for number in numbers]

doubles = [num*2 for num in range(1,5) if num >3]
print(doubles)

print('kiran'.upper())

list = ['A','B','C','D','E','F','G','H','I']

student_score = {name:random.randint(1,100) for name in list}
print(student_score)

passed_students = {key:value for (key,value) in student_score.items() if value > 60}
print(passed_students)