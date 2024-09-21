#Нейрокот, [21.09.2024 14:37]
#Для создания системы управления учетными записями пользователей,
# соответствующей указанным требованиям, мы разработаем два класса:
# `User` и `Admin`. Класс `User` будет инкапсулировать базовые данные
# о пользователе, а класс `Admin` будет наследоваться от `User` и
# расширять его функциональность для работы с учетными записями.

#Вот пример реализации:

#```python
class User:
    def __init__(self, user_id, name):
        self._user_id = user_id  # Защищенный атрибут
        self._name = name        # Защищенный атрибут
        self._access_level = 'user'  # Уровень доступа по умолчанию
        # для обычного пользователя

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Уровень доступа для администратора

    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Ошибка: передан объект не является экземпляром класса User.")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь с ID {user_id} удален.")
                return
        print(f"Ошибка: Пользователь с ID {user_id} не найден.")


# Пример использования:

# Создание списка пользователей
user_list = []

# Создание администратора
admin = Admin(1, "Admin User")

# Создание пользователей
user1 = User(2, "John Doe")
user2 = User(3, "Jane Smith")

# Администратор добавляет пользователей
admin.add_user(user_list, user1)
admin.add_user(user_list, user2)

# Администратор удаляет пользователя
admin.remove_user(user_list, 2)

# Проверка списка пользователей
for user in user_list:
    print(f"ID: {user.get_user_id()},"
          f" Name: {user.get_name()},"
          f" Access Level: {user.get_access_level()}")
#```

### Описание:
#1. **Класс `User`:**
#   - Инкапсулирует данные о пользователе: уникальный идентифик
#Нейрокот, [21.09.2024 14:37]
#атор, имя и уровень доступа.
#   - Методы `get_user_id`, `get_name`, `get_access_level` и
#   `set_name` предоставляют доступ к атрибутам.
#2. **Класс `Admin`:**
#   - Наследуется от `User` и задает уровень доступа администратора.
#   - Методы `add_user` и `remove_user` позволяют добавлять и
#   удалять пользователей из списка.
#3. **Инкапсуляция:**
#   - Защищенные атрибуты `_user_id`, `_name` и `_access_level`
#   предотвращают прямой доступ и модификацию извне. Доступ к ним
#   осуществляется через методы.