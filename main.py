'''
Name, type: get_valid_input(msg), boolean.
Calls: none.
Called by: view_posts(user, posts), main().

Description:
    Loop until we get valid int input from the user. Give a string "msg" parameter so
    we can decide between arrows ">> " or a message "Enter post number: ". Return
    true when the user enters an int value.
'''


def get_valid_input(msg):
    valid = False
    while not valid:
        try:
            choice = int(input(msg))
            return choice
        except ValueError:
            print("Invalid input")


'''
Name, type: login(), string.
Calls: none.
Called by: main().

Description:
    Prompt the user for a user name and password. If the entered credentials match an account
    saved in accounts.txt, then the existing data in data.txt is stored in the list posts and
    the user moves on to the menu.
'''


def login():
    valid_login = False
    user = ""
    while not valid_login:
        print("--------------------\n")
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


'''
Name, type: menu(user), void.
Calls: none.
Called by: main().

Description:
    Print a menu showing the user.
'''


def menu(user):
    print("--------------------\n")
    print("Welcome, " + user + "!\n")
    print("[1] Create new post")
    print("[2] View posts")
    print("[3] Logout")


'''
Name, type: create_post(user, posts), void.
Calls: none.
Called by: main().

Description:
    Takes string input to append to the posts list. The post cannot contain
    the special character "~". The tilde is used for parsing the original
    string that stores all data in data.txt.
'''


def create_post(user, posts):
    print("--------------------\n")
    print("Type your post below\n")
    post = input(">> ")
    if "~" in post:
        print("Invalid character: ~\n")
    else:
        posts.append(user + ":\n\t" + post + "\n\n\tcomments:\n")


'''
Name, type: view_posts(user, posts), void.
Calls: none.
Called by: main().

Description:
    Use a for loop to generate the correct post number for each post.
    Give the user a menu of options. If the user selects '1' then
    prompt them to enter a post number. If the post number exists,
    then the user can add a comment to the post. Again, the tilde
    is not allowed in comments since we use that to parse the
    string in the beginning of the program. If the user selects '2'
    then prompt them for a post number. If the post number exists
    and the user made the post, then allow them to delete the post.
'''


def view_posts(user, posts):
    print("--------------------\n")
    counter = 0
    for i in posts:
        print("Post #" + str(counter + 1) + "\n" + i + "\n", end="")
        counter += 1
    print("\n[1] Comment")
    print("[2] Delete post")
    print("[3] Back")
    choice = get_valid_input(">> ")
    if choice == 1:
        post_num = get_valid_input("\nEnter post number: ")
        if post_num > counter or post_num < 1:
            print("Invalid post number")
        else:
            print(posts[post_num - 1])
            print("Type your comment below\n")
            comment = input(">> ")
            if "~" in comment:
                print("Invalid character: ~\n")
            else:
                posts[post_num - 1] += "\t\t" + user + ": " + comment + "\n"
    elif choice == 2:
        post_num = get_valid_input("\nEnter post number: ")
        if post_num > counter or post_num < 1:
            print("Invalid post number\n")
        else:
            poster = ""
            is_poster = False
            for i in posts[post_num - 1]:
                for j in i:
                    if poster == user:
                        is_poster = True
                    poster += j
            if not is_poster:
                print("You can't delete that post since you didn't create it.\n")
            else:
                print(posts[post_num - 1])
                print("Delete this post?")
                print("[1] Yes")
                print("[2] No")
                delete_post = get_valid_input(">> ")
                if delete_post == 1:
                    posts.remove(posts[post_num - 1])


'''
Name, type: finalize, void.
Calls: none.
Called by: main()

Description:
    Append each item in the posts list with a tilde and write these items
    to data.txt.
'''


def finalize(posts):
    counter = 0
    for i in posts:
        posts[counter] += "~"
        counter += 1
    with open("data.txt", "a") as data:
        for i in posts:
            data.write(i)


'''
Name, type: get_correct_posts(temp_posts), list.
Calls: none.
Called by: main()

Description:
    Scan temp_posts and parse the data such that each post with
    comments is separated by a tilde. Return the formatted list
    new_posts and store these values in the posts list.
'''


def get_correct_posts(temp_posts):
    new_posts = []
    temp_string = ""
    for i in temp_posts:
        for j in i:
            if j == "~":
                new_posts.append(temp_string)
                temp_string = ""
            else:
                temp_string += j
    return new_posts


'''
Name, type: main(), void.
Calls: login(), get_correct_posts(temp_posts), menu(user), create_post(user, posts), 
       view_posts(user, posts), finalize(posts).
Called by: none.

Description:
    Call the login() function. On successful login, store the existing data in data.txt
    in the list temp_posts. Call get_correct_posts(temp_posts) passing temp_posts and
    store its return value in posts. Begin the while loop and call the menu(user) passing
    the user. Based on the user's input, call create_posts(user, posts) or view_posts(user, posts).
    When the user selects to logout, call the finalize(posts) function to store the data in
    the posts list in data.txt.
'''


def main():
    user = login()
    done = False
    temp_posts = []
    with open("data.txt", "r") as data:
        temp_posts.append(data.read())
    with open("data.txt", "w"):
        pass
    posts = get_correct_posts(temp_posts)
    while not done:
        menu(user)
        choice = get_valid_input(">> ")
        if choice == 1:
            create_post(user, posts)
        elif choice == 2:
            if posts:
                view_posts(user, posts)
            else:
                print("No posts yet\n")
        elif choice == 3:
            done = True
    finalize(posts)


main()