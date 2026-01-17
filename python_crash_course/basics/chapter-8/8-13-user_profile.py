def build_profile(first, last, **user_info):
    """Hacemos un diccionario con todo lo que sabemos sobre un usuario"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("gustavo", "alvarez", 
                             location="ourense", 
                             team_of_football= "celta de vigo")
print(user_profile)