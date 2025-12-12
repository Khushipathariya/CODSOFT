import random
import string

charVal = string.ascii_letters + string.digits + string.punctuation
pass_len = 8

password = "".join(random.choice(charVal) for i in range(pass_len))
print(password)
