import hashlib

password = '123'
hashlib.sha256(password.encode()).hexdigest()

print(hashlib.md5(password.encode()).hexdigest())