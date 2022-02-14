# making a gradebook
# charlotte niblett
# january 20, 2022

lloyd = {
    "name" : "Lloyd",
    "homework" : [90.0, 97.0, 75.0, 92.0],
    "quizzes" : [88.0, 40.0, 94.0],
    "tests" : [75.0, 90.0],
    }

alice = {
    "name" : "Alice",
    "homework" : [100.0, 98.0, 89.0, 93.0],
    "quizzes" : [99.0, 97.0, 77.0],
    "tests" : [96.0, 93.0],
    }

tyler = {
    "name" : "Tyler",
    "homework" : [ 66.0, 34.0, 76.0, 22.0],
    "quizzes" : [56.0, 42.0, 67.0],
    "tests" : [45.0, 88.0],
    }

students = [lloyd, alice, tyler]


for x in students:
    print (x)
    
def average(num):
    total = float(sum(num))
    avg = total / len(num)
    return avg

def get_average(student):
    homework = student["homework"]
    quizzes = student["quizzes"]
    tests = student["tests"]
    avg = average(homework)*0.1 + average(quizzes)*0.3 + average(tests)*0.6
    return avg

print("Lloyd Grade Average:", get_average(lloyd))

print("Lloyd Homework Average:", average(lloyd["homework"]))
    
#get a latter grade instead of a number
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
print (get_letter_grade(get_average(lloyd)))

#get average for the whole class
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

print("Class Average Grade", get_class_average(students))
print("Class Average Letter Grade:", get_letter_grade(get_class_average(students)))