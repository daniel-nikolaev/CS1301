#Write a function called course_info that takes as input a
#list of tuples. Each tuple contains two items: the first
#item in each tuple is a student's name as a string, and the
#second item in each tuple is that student's age as an
#integer.
#
#The function should return a dictionary with two keys.
#The key "students" should have as its value a list of all
#the students (in other words, a list made from the first
#value of each tuple), in the original order in which they
#appeared in the list. The key "avg_age" should have as its
#value a float representing the average age of all the
#students in the list (in other words, the average of all
#the second items in the tuples).
#
#For example:
#
#  course_info([("Jackie", 20), ("Marguerite", 21)])
#  -> {"students": ['Jackie', 'Marguerite'], "avg_age": 20.5}
#
#Hint: Concentrate first on building the list of students
#and calculating the average age. Save creating the
#dictionary for last.


#Write your function here!
def course_info(student_info):
    student_names = []
    total_age = 0
    num_students = 0
    
    # Iterate through each tuple (name, age)
    for name, age in student_info:
        student_names.append(name)  # Collect student names
        total_age += age  # Sum of ages
        num_students += 1  # Count number of students
    
    # Calculate average age
    avg_age = total_age / num_students if num_students > 0 else 0
    
    # Create and return the dictionary
    return {"students": student_names, "avg_age": avg_age}


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'avg_age': 20.5, 'students': ['Jackie', 'Marguerite']}
print(course_info([("Jackie", 20), ("Marguerite", 21)]))



