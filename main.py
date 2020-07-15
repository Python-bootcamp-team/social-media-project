def get_valid_input(msg):
    valid = False
    while not valid:
        try:
            choice = int(input(msg))
            return choice
        except ValueError:
            print("Invalid input")


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
                    print("logged in")
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


def create_post(user, post_count, posts):
    border()
    print("Type your post below\n")
    post = input(">> ")
    posts.append("#" + str(post_count + 1) + ": " + user + "\n\t" + post + "\n")


def view_posts(user, posts):
    border()
    for i in posts:
        print(i, end="")
    print("[1] Comment")
    print("[2] Delete post")
    print("[3] Back")
    choice = get_valid_input(">> ")
    if choice == 1:
        post_num = get_valid_input("Enter post number: ")
        print(posts[post_num - 1])
        print("Type your comment below\n")
        comment = input(">> ")
        posts[post_num - 1] += "\n\tcomments:\n\t\t" + user + ": " + comment + "\n"
    elif choice == 2:
        pass


def finalize(posts):
    with open("data.txt", "a") as data:
        for i in posts:
            data.write(i)


def get_correct_posts(temp_posts):
    new_posts = []
    slash_counter = 0
    temp_string = ""
    for i in temp_posts:
        for j in i:
            temp_string += j
            if j == "\n" or j == "\t":
                slash_counter += 1
            if slash_counter == 3:
                new_posts.append(temp_string)
                temp_string = ""
                slash_counter = 0
    return new_posts


def main():
    user = login()
    done = False
    posts = []
    temp_posts = []
    with open("data.txt", "r") as data:
        temp_posts.append(data.read())
        post_count = len(posts)
    with open("data.txt", "w"):
        pass
    posts = get_correct_posts(temp_posts)
    while not done:
        menu(user)
        choice = get_valid_input(">> ")
        if choice == 1:
            create_post(user, post_count, posts)
            post_count += 1
        elif choice == 2:
            view_posts(user, posts)
        elif choice == 3:
            done = True
    print(posts)
    finalize(posts)


main()
'''
Need to write one time only!

read from the file in the beginning just to fill the list.
when the user is done making changes, locally, then write to the file.
'''