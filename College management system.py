import mysql.connector as mysql

db = mysql.connect(host="localhost",user="root",password="",database="college")
command_handler=db.cursor(buffered=True)

# Student session
def student_session(username):
    while 1:
        print("")
        print("Student's menu")
        print("")
        print("1. View Register")
        print("2. Download Register")
        print("3. Logout")

        user_option = input("Option: ")
        if user_option == "1":
            query_vals =(str(username),)
            command_handler.execute("SELECT date,username,status FROM attendence WHERE username=%s",query_vals)
            records=command_handler.fetchall()
            for record in records:
                print(record)
        elif user_option == "2":
            print("Downloading Register")
            query_vals = (str(username),)
            command_handler.execute("SELECT date,username,status FROM attendence WHERE username=%s", query_vals)
            records = command_handler.fetchall()
            for record in records:
                with open("register.txt","w") as f:
                    f.write(str(records)+"\n")
                f.close()
            print("All records saved")
        elif user_option=="3":
            break
        else:
            print("Invalid option")
def auth_student():
    print("")
    print("Student's Login")
    print("")
    username = input("Username: ")
    password = input("Password: ")
    query_vals = (username, password)
    command_handler.execute("SELECT *FROM users WHERE username=%s AND password=%s AND privilege='student'", query_vals)
    if command_handler.rowcount <= 0:
        print("Login not recognized")
    else:
        student_session(username)


# Teacher session
def teacher_session():
    while 1:
        print("")
        print("Teacher's Menu")
        print("")
        print("1. Mark student register")
        print("2. View register")
        print("3. Logout")

        user_option = input("Option :")
        if user_option=="1":
            print("")
            print("Mark student register")
            command_handler.execute("SELECT username FROM users WHERE privilege='student'")
            records = command_handler.fetchall()
            date = input("Date : DD/MM/YYYY :")
            for record in records:
                record = str(record).replace("'","")
                record = str(record).replace(",","")
                record = str(record).replace("(","")
                record = str(record).replace(")","")

                #Present | Absent |Late
                status=input("status for "+record+ " P/A/L: ")
                query_vals=(str(record),date,status)
                command_handler.execute("INSERT INTO attendence (username,date,status) VALUES (%s,%s,%s)",query_vals)
                db.commit()
                print(record+" Marked as "+status)
        elif user_option=="2":
            print("")
            print("Viewing all student registers")
            command_handler.execute("SELECT username,date,status FROM attendence")
            records=command_handler.fetchall()
            for record in records:
                print(record)

        elif user_option=="3":
            break
        else:
            print("Ivalid option")
def auth_teacher():
    print("")
    print("Teacher's Login")
    print("")
    username = input("Username: ")
    password = input("Password: ")
    query_vals = (username,password)
    command_handler.execute("SELECT *FROM users WHERE username=%s AND password=%s AND privilege='teacher'",query_vals)
    if command_handler.rowcount <=0:
        print("Login not recognized")
    else:
        teacher_session()

# Admin session
def admin_session():
    while 1:
        print("")
        print("Admin's Menu")
        print("1. Register new student")
        print("2. Register new teacher")
        print("3. Delete existing student")
        print("4. Delete existing teacher")
        print("5. Logout")

        user_option = input("option: ")
        if user_option == "1":
            print("")
            print("Register new student")
            username = input("Student username: ")
            password=input("Student password: ")
            query_vals=(username,password)
            command_handler.execute("INSERT INTO users(username,password,privilege) VALUES (%s,%s,'student')",query_vals)
            db.commit()
            print(username+ " has been registered as a student")
        elif user_option == "2":
            print("")
            print("Register new teacher")
            username = input("Teacher username: ")
            password=input("Teacher password: ")
            query_vals=(username,password)
            command_handler.execute("INSERT INTO users(username,password,privilege) VALUES (%s,%s,'teacher')",query_vals)
            db.commit()
            print(username+ " has been registered as a teacher")
        elif user_option == "3":
            print("")
            print("Delete existing student account")
            username=input("Student username :")
            query_vals=(username,'student')
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username+ " has been deleted")
        elif user_option == "4":
            print("")
            print("Delete existing teacher account")
            username=input("Teacher username :")
            query_vals=(username,'teacher')
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username+ " has been deleted")
        elif user_option=="5":
            break
        else:
            print("Ivalid option")
def auth_admin():
    print("")
    print("Admin's Login")
    print("")
    username=input("Username: ")
    password=input("Password: ")
    if username == "admin":
        if password == "password":
            admin_session()
        else:
            print("Incorrect password !")
    else:
        print("Login details not recognise")

def main():
    while 1:
        print("WELCOME TO COLLEGE MANAGEMENT SYSTEM")
        print("")
        print("1. Login as a student")
        print("2. Login as a teacher")
        print("3. Login as a admin")
        print("4. Quit")

        user_option=input("option: ")
        if user_option == "1":
            auth_student()
        elif user_option == "2":
            auth_teacher()
        elif user_option == "3":
            auth_admin()
        elif user_option == "4":
            quit()
        else:
            print("invalid option")

main()