from user_class import User, Admin, Privileges

admin_edu = Admin("edu", "lopez", "Spain", "Toledo", 42)
print(admin_edu.describe_user())
admin_edu_privileges = Privileges("p")
print(admin_edu_privileges.show_privileges())