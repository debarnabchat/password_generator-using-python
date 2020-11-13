import random
import string
import time


def pass_generate():
    print("Welcome to the Password Generation Tool!")
    time.sleep(0.8)
    print("Upon specifying the number of characters, we will generate a random password containing an amalgamation of letters and numbers.")
    time.sleep(2)
    user_input = input("Please enter the number of characters:")
    user_input = int(user_input)
    integers = random.randint(0,user_input)
    letters = user_input - integers
    mintchoice = str(random.randint((10**(integers-1)),((10**integers)-1)))
    mletterchoice = ''.join(random.choice(string.ascii_letters) for i in range(letters))
    password = str(mintchoice+mletterchoice)
    password_final = ''.join(random.sample(password,len(password)))
    print(password_final)
    time.sleep(60)

pass_generate()



