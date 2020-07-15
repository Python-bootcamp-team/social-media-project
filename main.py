def get_valid_input():
    choice = 0
    valid = False
    while not valid:
        try:
            choice = int(input(">> "))
            valid = True
        except ValueError:
            print("Invalid input")
    return choice


def border():
    temp_string = ""
    for i in range(20):
        temp_string += "-"
    temp_string += "\n"
    print(temp_string)


def login():
    valid_login = False
    user = ""
    while not valid_login:
        border()
        user = input("User name: ")
        password = input("\nPassword: ")
        users = []
        with open("accounts.txt") as accounts:
            for i in accounts:
                users.append(i)
        counter = 0
        for i in users:
            if user == users[counter][:-1]:
                if password == users[counter + 1][:-1]:
                    valid_login = True
                    print("logged in\n")
            counter += 1
        if not valid_login:
            print("Invalid login\n")
    return user


def menu(user):
    border()
    print("Welcome, " + user + "!\n")
    print("[1] Create new post")
    print("[2] View posts")
    print("[3] Logout")


def create_post(user, post_count):
    border()
    print("Type your post below\n")
    post = input(">> ")
    with open("data.txt", "a") as posts:
        posts.write("\n#" + str(post_count + 1) + ": " + user + "\n\t" + post)


def view_posts(user, posts):
    with open("data.txt", "a") as data:
        for i in posts:
            data.write(i)
    with open("data.txt", "r") as data:
        print(data.read())
    print("[1] Comment on a post")
    print("[2] Delete one of your posts")
    print("[3] Back")
    choice = get_valid_input()
    if choice == 1:
        '''
        temp_string = ""
        post_num = get_valid_input()
        for i in posts:
            if post_num in i[1]:
                temp_string = i
        '''
    elif choice == 2:
        pass


def finalize(posts):
    posts.remove(posts[len(posts) - 1])
    with open("data.txt", "a") as data:
        for i in posts:
            data.write(i)


def main():
    user = login()
    done = False
    posts = []
    post_count = 0
    while not done:
        with open("data.txt", "r") as data:
            posts.append(data.read())
        with open("data.txt", "w") as data:
            pass
        menu(user)
        choice = get_valid_input()
        if choice == 1:
            create_post(user, post_count)
            post_count += 1
        elif choice == 2:
            view_posts(user, posts)
        elif choice == 3:
            done = True
    finalize(posts)


main()