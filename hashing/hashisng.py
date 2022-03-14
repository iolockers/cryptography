from hashlib import sha256

s1 = 'Hello world!'

result = sha256(s.encode())
print(result.hexdigest())