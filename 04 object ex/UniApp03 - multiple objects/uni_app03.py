import database03 as db

users = db.get_users()

# print out all the user details
for user in users:
    print(f"name:      {user.name}")
    if hasattr(user, "user_id"):
        print(f"user id:   {user.user_id}")
    if hasattr(user, "job"):
        print(f"job title: {user.job}")
    if hasattr(user, "programme"):
        print(f"programme: {user.programme}")
    if hasattr(user, "modules"):
        for module in user.modules:
            print(f" {module}")
    print()

while True:
    group = input("Group (staff, students, all or module)? ")
    if group == "":
        break
    message = input("Message? ")
    if message == "":
        break
    for user in users:
        if group == "all" or group == user.group:
            user.send_message(message)
        if hasattr(user, "modules") and group in user.modules:
            user.send_message(message)

