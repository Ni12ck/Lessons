# Создать персональную функции для подробной интроспекции объекта.
# Задание:
# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого
# объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).

# Создал функцию introspection_info(obj), которая принимает объект obj
def introspection_info(obj):
    # Тип объекта
    type_obj = type(obj).__name__
    # Атрибуты объекта
    attributes_obj = [attribute for attribute in dir(obj) if not callable(getattr(obj, attribute))]
    # Методы объекта
    methods_obj = [method for method in dir(obj) if callable(getattr(obj, method))]
    # Модуль, к которому объект принадлежит
    module_obj = obj.__class__.__module__
    # Является ли объект экземпляром того или иного типа
    obj_is_str = isinstance(obj, str)
    obj_is_int = isinstance(obj, int)
    # Вернул строку с описанием
    return (f'Тип объекта "{obj}": {type_obj}\n'
            f'Атрибуты объекта "{obj}": {attributes_obj}\n'
            f'Методы объекта "{obj}": {methods_obj}\n'
            f'Модуль, к которому принадлежит объект "{obj}": {module_obj}\n'
            f'Является ли {obj} экземпляром str? - {obj_is_str}\n'
            f'Является ли {obj} экземпляром int? - {obj_is_int}\n')


# Примеры работы
obj_1 = introspection_info('Ni12ck')
obj_2 = introspection_info(12)

print(obj_1)
print(obj_2)
