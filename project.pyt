import random
import string

print("---------WELCOME TO THE PASSWORD GENERATOR APP--------")

# This is the app for password generation 
while True:
    print("....SETTINGS FOR PASSWORD GENERATOR.....")

    # 1. ask for length of the password.
    while True:
        try:
            length = int(input("enter length of the password(minimum limit is 6):"))
            if length >= 6:
                break
            print("Password should be more than 6 characters for security purposes .")
        except ValueError:
            print("enter a valid number.")

    # 2.Ask the user for the preference 


    include_uppercases = input("Include uppercase letters?  ").lower() == "yes"
    include_numbers = input("Include numbers?  ").lower() == "yes"
    include_specials = input("Include special characters/symbols? ").lower() == "yes"

    # 3. build the characters


    characters = string.ascii_lowercase  # Start with lowercase letters as a baseline

    if include_uppercases:
     characters += string.ascii_uppercase
    if include_numbers:
      characters += string.digits
         
    if include_specials:
     characters += string.punctuation


    # 4. Generating a random password 


    passwords_created = random.choices(characters, k=length)
    password = "".join(passwords_created)

    # 5. calculate a score for difficulty of the password  

    score = 0

    # add points for length of password 
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1

    # Add points for character varieties used
    if include_uppercases:
        score += 1
    if include_numbers:
        score += 1
    if include_specials:
        score += 1

    # Converting the password into  a string 
    if score <= 2:
        strength = "🔴 WEAK (<<<<<< Easy password >>>>>>>>>.)"
    elif score == 3 or score == 4:
        strength = "🟡 MODERATE  (<<<<<<<<< Intermediate password >>>>>>>>>>.)"
    else:
        strength = "🟢 STRONG (<<<<<<<<< Hard password >>>>>>>>>. )"

    # 6. Display the password 


    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(f"THE GENERATED PASSWORD BY THE SYSTEM:  {password}")
    print(f"THE STRENGTH OF THE PASSWORD GENERATED IS :  {strength}")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    # 7. ASK THE USER IF THEY WANT TO GENERATE A NEW PASSWORD 

    repeat = input("would you like to try making another one ???? ")
    if repeat.lower() != "yes":
        print("~~~~~~~~~~~    THANK YOU    ~~~~~~~~~~~~~~~~")   



    #  8. ASK IF THE PERSON WILL RATE THE APP

    RATING_APP = input("would you like to rate the app")
    if RATING_APP == "yes":
          Rate =  input( "RATE AS PER YOU CHOICE BETWEEN 1 TO 5") 

    print ("you have rated the app :", Rate) 

    
    break