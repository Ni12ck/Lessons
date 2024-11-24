import hashlib

password = '123'
hashlib.sha256(password.encode()).hexdigest()

print(hashlib.md5(password.encode()).hexdigest())

class User:
    def __init__(self, nickname: str, password, age: int):
        # nickname(имя пользователя, строка)
        self.nickname = nickname
        # password(в хэшированном виде, число)
        self.password = hashlib.md5(password.encode()).hexdigest()
        # age(возраст, число)
        self.age = age

