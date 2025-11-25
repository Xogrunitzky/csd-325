import json

# Function to loop through and print student list
def print_students(students):
    for s in students:
        print(f"{s['L_Name']}, {s['F_Name']} : ID = {s['Student_ID']} , Email = {s['Email']}")
    print()  # spacing


# --- 1. Load the JSON file into a class list ---
with open("students.json", "r") as file:
    students_list = json.load(file)

print("=== Original Student List ===")
print_students(students_list)


# --- 2. Add your information using append() ---
new_student = {
    "F_Name": "Xavier",
    "L_Name": "Grunitzky",
    "Student_ID": 11111,             # fictional ID
    "Email": "xgrunitzky@my365.bellevue.edu"
}

students_list.append(new_student)

print("=== Updated Student List ===")
print_students(students_list)


# --- 3. Save updated list back to the JSON file ---
with open("students.json", "w") as file:
    json.dump(students_list, file, indent=4)

print("=== JSON file has been updated ===")