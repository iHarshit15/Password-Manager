# master password which doesn't matter
master_pass = input("Enter Master Password: ")
# added a function so that we can save input and call later
def add():
    name = input("Enter your Username: ")
    pwd = input("Enter your Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n   ")\

# view function to view what we have saved
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("|")
            print("User:", user +"\n" "Password:", passw )


# loop so that program must not end as soon as we input something wrong or in just one operation
while True:
    mode = input("Would you like to add a new password or view existing, q to quit, (add/view/quit): ").lower()
    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("invalid mode")
        continue
