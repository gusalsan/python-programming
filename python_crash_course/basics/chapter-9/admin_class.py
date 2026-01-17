from user_class import User
class Admin(User):
    """Lista de privilegios que tiene el administrador"""
    def __init__(self, first_name, last_name, country, city, age):
        """Lista inicial como usuario mas a mayores añadimos los privilegios"""
        super().__init__(first_name, last_name, country, city, age)

class Privileges:
    """Los privilegios del admin"""
    def __init__(self, privileges):
        """Hacemos la lista de privilegios y le añadimos self"""
        privileges = ("Can delete post", "Can ban user", "Can add post")
        self.privileges = privileges

    def show_privileges(self):
        """Imprimimos la lista de privilegios del admin"""
        print(f"Admin have these privileges:\n{self.privileges}")