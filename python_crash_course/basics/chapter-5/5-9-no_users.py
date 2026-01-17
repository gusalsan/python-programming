usernames = []
if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, the world looks better with you")
        else:
            print(f"Hello {username}, welcome to the jungle")
else:
    print("We need to find users!!!!")