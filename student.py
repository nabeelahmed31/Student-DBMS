import sqlite3


def connection():
    conn = sqlite3.connect("student.db")
    return conn


def search():
    conn = connection()
    print("Search By:")
    print("1.Name")
    print("2.section")
    print("3.Roll No")
    print("4.Phone number")
    n = int(input("Select one attribute:"))
    while True:
        if n == 1:
            m = input("Enter a name:")
            record = conn.execute("select name from students")
            break
        if n == 2:
            m = input("Enter a section:")
            record = conn.execute("select section from students")
            break
        if n == 3:
            m = int(input("Enter a roll no:"))
            record = conn.execute("select roll_no from students")
            break
        if n == 4:
            m = int(input("Enter a phone number:"))
            record = conn.execute("select phone_no from students")
            break
        if n < 1 or n > 4:
            print("Invalid selection!")

    check_list = []
    cnt = 0
    for i in record:
        for j in i:
            check_list.append(j)
    record = conn.execute("select * from students")
    j = 0
    for i in record:
        if m == check_list[j]:
            print(i)
            cnt = cnt + 1
        j = j + 1
    if cnt == 0:
        print("Entry not found!")


def check_roll(roll_no):
    conn = connection()
    record = conn.execute("select roll_no from students")
    check_list = []
    for i in record:
        for j in i:
            check_list.append(j)
    for i in check_list:
        if i == roll_no:
            return 1
    return 0


def add():
    conn = connection()
    conn.execute(
        "create table if not exists students(name text,roll_no integer,branch text,section text,phone_no integer,address text)")

    name = input("Enter Student Name:")
    while True:
        roll_no = int(input("Enter Student Roll No:"))
        if check_roll(roll_no) == 1:
            print("Roll Number Already Exists, Please Try Again!")
        else:
            break
    branch = input("Enter Student Branch:")
    section = input("Enter Student Section:")
    phn = int(input("Enter Student Phone No:"))
    address = input("Enter Student Address:")

    conn.execute("insert into students values(?,?,?,?,?,?)", (name, roll_no, branch, section, phn, address))
    print("Added Successfully")

    conn.commit()
    conn.close()


def view():
    conn = connection()
    records = conn.execute("select * from students")
    for i in records:
        print(i)
    conn.commit()
    conn.close()


def delete():
    conn = connection()

    while True:
        roll_no = int(input("Enter the roll no you want to delete:"))
        if check_roll(roll_no) == 0:
            print("Roll Number Does Not Exists, Please Try Again!")
        else:
            break

    conn.execute("delete from students where roll_no=?", (int(roll_no),))

    print("Deleted successfully")

    conn.commit()
    conn.close()


def update():
    conn = connection()

    roll_no = int(input("Enter the roll no you want to update:"))
    name = input("Enter Student Name:")
    new_roll_no = int(input("Enter Student Roll No:"))
    branch = input("Enter Student Branch:")
    section = input("Enter Student Section:")
    phn = int(input("Enter Student Phone No:"))
    address = input("Enter Student Address:")

    conn.execute("update students set name=?,roll_no=?,branch=?,section=? ,phone_no=?,address=? where roll_no=?",
                 (name, new_roll_no, branch, section, phn, address, roll_no))
    print("Modified Successfully")

    conn.commit()
    conn.close()


while True:
    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("1.View complete record")
    print("2.Search")
    print("3.Add an entry")
    print("4.Delete an entry")
    print("5.Modify an entry")
    print("6.Close\n")

    n = int(input("Select your command:"))
    if n == 1:
        view()

    if n == 2:
        search()

    if n == 3:
        add()

    if n == 4:
        delete()

    if n == 5:
        update()

    if n == 6:
        break

    if n < 1 or n > 5:
        print("Selection Invalid!")
