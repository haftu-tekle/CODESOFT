import random as rand
import string as str
passwd_lngth=int(input('input the length of password you want to generate'))
characters=str.ascii_letters + str.digits + str.punctuation
password=''
for x in range(passwd_lngth):
    password+=rand.choice(characters) 
print(list(password)) 
