from user_class import User
from admin_class import Admin, Privileges

otro_admin = Admin ("fernando", "gomez", "españa", "palencia", 55)
print(otro_admin.describe_user())
otro_admin_privilegios = Privileges("p")
print(otro_admin_privilegios.show_privileges())