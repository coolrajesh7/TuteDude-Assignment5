student = {'John': 85, 'Rajesh': 99, 'Soumik': 90}

user_input = input("Enter the student's name: ")

if user_input in student:
    print(f"{user_input}'s marks: " + str(student.get(user_input)))
else:
    print('Student not found.')