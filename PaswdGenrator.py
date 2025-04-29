import random as rand
import string as str

passwd_lngth=int(input('input the length of password you want to generate'))
found=True

# while True:
for x in range(passwd_lngth):
    characters=str.ascii_letters + str.digits + str.punctuation
    paswrd=[]

    if True:
        password=rand.choice(characters)
        for x in password:
            paswrd.append(password)
            print(paswrd)
        # return(paswrd)
    # return
    # break


