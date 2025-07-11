def menu():
    print("Student Record Menu")
    print("1 Add Student")
    print("2 Show all students")
    print("3 Search by name")
    print("4 Exit")

def add_student():
    print("add student")
    name = input("enter name: ")
    marks = input("enter marks: ")
    with open("pratice.txt" , "a") as f:
        f.write(f"{name} , {marks} \n")
        print("student added")

def show_students():
    print("all students:")
    with open("pratice.txt" , "r") as f:
        lines = f.readlines()
        if lines == []:
            print("no records")
        else:
            for line in lines:
                if "," in line:
                    data = line.strip().split(",")
                    print("name:", data[0], "marks:", data[1])

def search_student():
    name = input("enter name : ")
    with open("pratice.txt" , 'r') as f:
        data = f.read()
        data.find(name)

print("welcome to record systm")

while True:
    menu()
    ch = input("enter choise: ")
    if ch == "1":
        add_student()
    elif ch == "2":
        show_students()
    elif ch == "3":
        search_student()
    elif ch == "4":
        print("bye")
        break
    else:
        print("wrong input")
1