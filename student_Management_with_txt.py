def addstud(x):
    x = open(x, "a+")
    x.seek(0)
    exist = False
    rollno = int(input("Enter roll no: "))
    for i in x.readlines():
        r = i.strip().split(",")[0]
        if r == str(rollno):
            exist = True
    if not exist:
        name = input("Enter student name: ")
        math = int(input("Enter math marks: "))
        science = int(input("Enter science marks: "))
        english = int(input("Enter english marks: "))
        totalmarks = math + science + english
        if totalmarks >= 258 and totalmarks <= 300:
            grade = "A"
        elif totalmarks >= 200 and totalmarks <= 258:
            grade = "B"
        elif totalmarks >= 150 and totalmarks <= 200:
            grade = "C"
        else:
            grade = "D"

        x.writelines(f"{rollno},{name},{totalmarks},{grade}\n")
        x.close()
    else:
        print("Roll no already exist")
        x.close()


def showall(x):
    x = open(x, "r")
    if len(x.readlines()) == 0:
        print("Database is empty!")

    else:
        x.seek(0)
        for i in x.readlines():
            roll, name, totalmarks, grade = i.strip().split(",")
            print(
                f"Rollno : {roll} | Name: {name.capitalize()} | Totalmarks : {totalmarks} | Grade : {grade}"
            )
    x.close()


def search(x):
    x = open(x, "r")
    sr = input("Enter roll no to search: ")
    for i in x.readlines():
        roll, name, totalmarks, grade = i.strip().split(",")
        if roll == sr:
            x.seek(0)
            print(f"Rollno : {roll} | Name: {name.capitalize()} | Totalmarks : {totalmarks} | Grade : {grade}")
        else:
            print("Rollno not found")
    x.close()


def delete(x, y):
    m = open(x, "r")
    c = open(y, "w")
    delete = False
    sr = input("Enter roll no to delete: ")
    for i in m.readlines():
        roll, name, totalmarks, grade = i.strip().split(",")
        if roll != sr:
            c.writelines(f"{roll},{name},{totalmarks},{grade}\n")
            c.close()
        else:
            delete = True
    if delete:
        print("found and deleted")
        c = open(y, "r")
        b = c.readlines()
        n = open(x, "w")
        n.writelines(b)
        c.close()
        n.close()
    else:
        print("Given Roll not found")
    m.close()
# this is a experiment section down there
# For creating function to update data in database
def update(x, y):
    # x = main file name, y = temp file name
    m = open(x, "r")
    lines = m.readlines()
    m.close()

    sr = input("Enter roll no to update: ").strip()
    updated = False

    c = open(y, "w")
    for i in lines:
        roll, name, totalmarks, grade = i.strip().split(",")
        if roll == sr:
            print("Enter new details (leave blank to keep current value):")
            new_roll = input(f"Roll no [{roll}]: ").strip()
            if not new_roll:
                new_roll = roll

            new_name = input(f"Name [{name}]: ").strip()
            if not new_name:
                new_name = name

            # If user wants to keep the existing total, leave marks blank.
            math_in = input("Math marks (leave blank to keep current total): ").strip()
            if math_in == "":
                new_total = totalmarks
            else:
                math = int(math_in)
                science = int(input("Science marks: "))
                english = int(input("English marks: "))
                new_total = str(math + science + english)

            t = int(new_total)
            if t >= 258 and t <= 300:
                new_grade = "A"
            elif t >= 200 and t <= 258:
                new_grade = "B"
            elif t >= 150 and t <= 200:
                new_grade = "C"
            else:
                new_grade = "D"

            c.writelines(f"{new_roll},{new_name},{new_total},{new_grade}\n")
            updated = True
        else:
            c.writelines(i)
    c.close()

    if updated:
        # copy temp back into main file
        c = open(y, "r")
        b = c.readlines()
        n = open(x, "w")
        n.writelines(b)
        c.close()
        n.close()
        print("Record updated")
    else:
        print("Given Roll not found")


def ensurefile(x):
    return open(x, "a")


x = "students.txt"  # this is a main file for main data
y = "studtemp.txt"  # this is temporary file f
while True:
    print("Student Management System")
    pr = """1. Add Student\n2. Search Student\n3. Show all Student\n4. Delete Student\n5. Exit\n6. Student detail update"""
    print(pr)
    choice = input("Enter choice: ")
    if not choice or not choice.isdigit():
        print("Enter valid choice")
        continue
    else:
        choice = int(choice)
        if choice == 1:
            ensurefile(x)
            print("Enter detail of New Student below")
            addstud(x)
        elif choice == 2:
            print("Enter detail of Student you want to search below")
            search(x)
        elif choice == 3:
            ensurefile(x)
            showall(x)
        elif choice == 4:
            print("Enter detail of Student you want to delete below")
            delete(x, y)
        elif choice == 5:
            break
        elif choice==6:
            print("Enter detail of Student you want to update below")
            update(x, y)
        else:
            continue
