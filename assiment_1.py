
students = {}

print("What do you want")

def menu():
    print("1. Add student")
    print("2. Check status")
    print("3. Search student")
    print("4. Exit")

def add_student():
    s_name = input("Enter student name: ")
    s_status = input("Enter student status (Present/Absent): ").lower()
    if s_status in ['present', 'absent']:
        students[s_name] = s_status
        print("Student added")
    else:
        print("Invalid status! Use 'Present' or 'Absent'.")

def status():
    pre = 0
    abs = 0
    for s in students.values():
        if s == "present":
            pre += 1
        elif s == "absent":
            abs += 1
    print("Total present students:", pre)
    print("Total absent students:", abs)

def search():
    name = input("Enter student name: ")
    if name in students:
        print(f"{name} is {students[name]}")
    else:
        print("Student not found")

while True:
    menu()
    ans = input("Enter your choice: ")
    if ans == "1":
        add_student()
    elif ans == "2":
        status()
    elif ans == "3":
        search()
    elif ans == "4":
        break
    else:
        print("Please choose a valid option.")
