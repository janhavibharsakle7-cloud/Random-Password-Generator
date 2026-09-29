# Random-Password-Generator
 This project demonstrates the use of Python concepts such as **strings, lists, loops, user input, and the random module**. It helps users create secure passwords without having to think of them manually.
The Random Password Generator is a Python-based application developed to generate secure and customizable passwords. The program allows users to specify the password length and select different character types, including uppercase letters, numbers, and special symbols. It also evaluates the strength of the generated password and provides feedback to the user.

This project demonstrates the practical implementation of core Python programming concepts such as loops, conditional statements, exception handling, strings, modules, and randomization techniques.

Objectives:


To generate random and secure passwords.
To allow users to customize password composition.
To evaluate password strength based on length and character diversity.
To apply fundamental Python concepts in a real-world application.


Features:


User-defined password length.
Minimum password length validation.
Optional inclusion of:
Uppercase letters
Numbers
Special characters
Random password generation.
Password strength analysis.
Interactive command-line interface.
Application rating feature.
Technologies Used
Programming Language: Python 3
Libraries Used:
random
string
Methodology

The application follows these steps:

Display a welcome message.
Accept password length from the user.
Validate the input using exception handling.
Ask the user for character preferences.
Create a character pool based on selected options.
Generate a random password.
Calculate password strength.
Display the generated password and its strength.
Provide an option to generate another password.
Collect user feedback through a rating system.
Password Strength Criteria


The strength of the password is determined using the following parameters:

Criteria	Score

Password length ≥ 8	+1
Password length ≥ 12	+2
Includes uppercase letters	+1
Includes numbers	+1
Includes special characters	+1
Strength Levels
Total Score	Strength
0 – 2	Weak
3 – 4	Moderate
5 or more	Strong


Sample Output:


---------WELCOME TO THE PASSWORD GENERATOR APP--------

....SETTINGS FOR PASSWORD GENERATOR.....

Enter length of the password (minimum limit is 6): 12

Include uppercase letters? yes
Include numbers? yes
Include special characters/symbols? yes

THE GENERATED PASSWORD BY THE SYSTEM: A7@kLm#9Pq2!
THE STRENGTH OF THE PASSWORD GENERATED IS: STRONG 


Applications:

Creating secure passwords for online accounts.
Improving awareness of password security.
Learning Python programming concepts through practical implementation.
