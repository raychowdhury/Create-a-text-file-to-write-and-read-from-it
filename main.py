def signup():
    with open('test3.txt', 'w') as f:
        print("For sign up please fill up the form.")
        f_name = str(input("Enter your first name: "))
        f.write("first name: " + f_name + "\n")
        l_name = str(input("Enter your last name: "))
        f.write("last name: " + l_name + "\n")
        full_name = f_name + " " + l_name
        f.write("full name: " + full_name + "\n")
        email = f_name + l_name + "@mail.com"
        f.write("email: " + email + "\n")
        password = str(input("Enter your password: "))
        f.write("Password: " + password + "\n")

    with open('test3.txt', 'r') as p:
        print("Welcome to 420.")
        print(p.read())


print("Welcome to your company.")
print("---------------------------")
print("To join our company sign up.")
print("For log in.")
print(signup())
