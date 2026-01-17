current_users = ["manolo69", "javier73838", "jesulin_14", "cr7777", "papi418"]
new_users = ["manolo69", "javier73838", "congui_perros", "toni_chapas", "tupu_tamadre", "CR7777"]
for new_user in new_users: 
    if new_user.lower() in current_users:
        print(f"Sorry, your shit name {new_user} is not avaliable")
    else:
        print(f"Welcome {new_user}, you have a new shit name")