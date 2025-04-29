# import random as rand
# import string as str
# passwd_lngth=int(input('input the length of password you want to generate'))
# characters=str.ascii_letters + str.digits + str.punctuation
# password=''
# for x in range(passwd_lngth):
#     password+=rand.choice(characters)    
# print(password) 
import random as rand
import string as str

passwd_lngth = int(input('Input the length of password you want to generate: '))

characters = str.ascii_letters + str.digits + str.punctuation
password = ""  # Initialize an empty string to store the password

for _ in range(passwd_lngth):
    password += rand.choice(characters)  # Append a random character to the password string

print(password)  # Print the complete password after the loop finishes


