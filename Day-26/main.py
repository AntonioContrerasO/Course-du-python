# names = ["Manuel","Ivan","Saul","Rosa","Andy","Vale"]
#
# import random
#
# students_score = {student:random.randint(1,100) for student in names}
#
# passed_students = {student:score for (student,score) in students_score.items() if int(score) >= 70}
#
# print(passed_students)
#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day:weather_c[day] * 9/5 + 32 for (day,temperature) in weather_c.items()}
#
# print(weather_f)
#
import pandas

student_dict = {"student": ["Angela", "James", "Lily"],
                "score": [56, 76, 98]}

student_data_frame = pandas.DataFrame(student_dict)

# loop rows of the data

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row)
