class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, 'admin')
        self.__users_list = []

    def add_user(self, user):
        self.__users_list.append(user)

    def remove_user(self, user):
        if user in self.__users_list:
            self.__users_list.remove(user)

    def get_users_list(self):
        return self.__users_list


user1 = User(1, 'Люся')
user2 = User(2, 'Миша')
admin = Admin(3, 'Admin')

admin.add_user(user1)
admin.add_user(user2)

print(f"Admin {admin.get_name()} has access level: {admin.get_access_level()}")
print(f"Users managed by {admin.get_name()}:")
for user in admin.get_users_list():
    print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")