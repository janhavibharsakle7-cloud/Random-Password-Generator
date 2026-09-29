# 🔐 Random Password Generator

A Python-based **Random Password Generator** that creates customizable passwords based on the user's selected length and character preferences. The application also provides a basic password-strength evaluation based on password length and character variety.

---

## 📌 Project Overview

Creating strong and unique passwords is an important part of maintaining online security. Remembering and creating different passwords manually can be difficult, especially when a password needs to contain a combination of letters, numbers, and special characters.

This project provides a simple command-line solution for generating random passwords. The user can specify the required password length and choose whether to include **uppercase letters, numbers, and special characters**.

After generating the password, the application calculates a score and classifies the password as **Weak, Moderate, or Strong**.

The project was developed using Python's built-in `random` and `string` modules and does not require any external packages.

---

## 🎯 Objectives

The main objectives of this project are:

* Generate random passwords automatically.
* Allow users to customize the password according to their requirements.
* Provide options for uppercase letters, numbers, and special characters.
* Validate the password length entered by the user.
* Evaluate the basic strength of the generated password.
* Demonstrate fundamental Python programming concepts through a practical project.
* Create an interactive command-line application.

---

## ✨ Features

### 🔢 Custom Password Length

The user can specify the desired password length.

The program requires a minimum length of **6 characters**.

### 🔤 Uppercase Letters

Users can choose whether uppercase letters should be included in the generated password.

Example:

```text
A B C D E F
```

### 🔢 Numbers

Users can choose to include numbers.

Example:

```text
0 1 2 3 4 5 6 7 8 9
```

### 🔣 Special Characters

Users can choose to include special characters and symbols.

Example:

```text
! @ # $ % & *
```

### 🎲 Random Password Generation

The application randomly selects characters from the available character set to create the password.

### 🛡️ Password Strength Evaluation

The generated password receives a score based on:

* Password length
* Uppercase letter selection
* Number selection
* Special-character selection

The application then displays the strength as:

* 🔴 **Weak**
* 🟡 **Moderate**
* 🟢 **Strong**

### ⭐ User Rating

The application also provides an optional feature that allows the user to rate the application from **1 to 5**.

---

## 🛠️ Technologies Used

| Technology   | Purpose                    |
| ------------ | -------------------------- |
| Python       | Main programming language  |
| `random`     | Random character selection |
| `string`     | Predefined character sets  |
| Command Line | User interface             |

---

## 📚 Python Concepts Used

This project demonstrates several fundamental Python concepts:

### Variables

Variables are used to store values such as password length, character sets, user preferences, and password strength score.

### Conditional Statements

`if`, `elif`, and `else` are used to make decisions throughout the program.

### While Loops

`while` loops are used for input validation and controlling program execution.

### Exception Handling

The `try-except` statement handles invalid numerical input.

For example:

```python
try:
    length = int(input("Enter length of the password: "))
except ValueError:
    print("Enter a valid number.")
```

### Strings

Strings are used to store and combine the different character sets used for password generation.

### Modules

The project uses Python's built-in modules:

```python
import random
import string
```

### Boolean Expressions

User responses are converted into Boolean values to determine which character types should be included.

---

## ⚙️ How the Program Works

The application follows these main steps:

### 1. Start the Application

The program displays a welcome message.

### 2. Enter Password Length

The user enters the desired password length.

The program checks whether the entered value is valid and whether it meets the minimum length requirement of 6 characters.

### 3. Select Character Preferences

The user is asked three questions:

```text
Include uppercase letters?
Include numbers?
Include special characters/symbols?
```

The user can answer with `yes` or another response.

### 4. Build the Character Set

The program starts with lowercase letters:

```python
characters = string.ascii_lowercase
```

Depending on the user's choices, it adds:

```python
string.ascii_uppercase
string.digits
string.punctuation
```

### 5. Generate the Password

The program randomly selects characters using:

```python
random.choices(characters, k=length)
```

The selected characters are then joined together to create the final password.

### 6. Calculate Password Strength

The program calculates a score using password length and the selected character types.

### 7. Display the Result

The generated password and its strength are displayed to the user.

### 8. Collect Feedback

The user can optionally rate the application from 1 to 5.

---

## 🔐 Password Strength System

The application uses a simple scoring system.

### Password Length

| Condition             | Score |
| --------------------- | ----: |
| 8 or more characters  |    +1 |
| 12 or more characters |    +2 |

### Character Variety

| Character Type     | Score |
| ------------------ | ----: |
| Uppercase letters  |    +1 |
| Numbers            |    +1 |
| Special characters |    +1 |

### Strength Classification

| Score | Classification |
| ----: | -------------- |
|   0–2 | 🔴 Weak        |
|   3–4 | 🟡 Moderate    |
|    5+ | 🟢 Strong      |

> **Note:** This is a basic educational strength-scoring system. It is not intended to replace professional password-security analysis.

---

## ▶️ How to Run the Project

### Step 1: Install Python

Install **Python 3** on your computer.

### Step 2: Download or Clone the Project

Clone the repository:

```bash
git clone <your-repository-link>
```

Or download the project files manually.

### Step 3: Open the Project Folder

Open the folder in an IDE or code editor such as:

* Visual Studio Code
* PyCharm
* IDLE

### Step 4: Run the Program

If your Python file is named:

```text
password_generator.py
```

run:

```bash
python password_generator.py
```

No additional packages need to be installed.

---

## 💻 Example

### User Input

```text
---------WELCOME TO THE PASSWORD GENERATOR APP--------

....SETTINGS FOR PASSWORD GENERATOR.....

enter length of the password(minimum limit is 6): 12

Include uppercase letters? yes
Include numbers? yes
Include special characters/symbols? yes
```

### Generated Output

```text
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

THE GENERATED PASSWORD BY THE SYSTEM:
aP7@kLm2#Xq9

THE STRENGTH OF THE PASSWORD GENERATED IS:
🟢 STRONG

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
```

**Note:** The generated password will be different each time because the characters are selected randomly.

---

## 📁 Project Structure

A simple project structure can be:

```text
Random-Password-Generator/
│
├── password_generator.py
│
└── README.md
```

### `password_generator.py`

Contains the complete Python source code for the password generator.

### `README.md`

Contains the project documentation, features, usage instructions, and other information about the project.

---

## 🧪 Testing

The application can be tested using different inputs.

| Test | Input             | Expected Result                        |
| ---- | ----------------- | -------------------------------------- |
| 1    | Length = 5        | Minimum-length warning                 |
| 2    | Length = 6        | Password is generated                  |
| 3    | Length = 12       | Longer password is generated           |
| 4    | Length = `abc`    | Invalid number message                 |
| 5    | Uppercase = Yes   | Uppercase characters added             |
| 6    | Numbers = Yes     | Digits added                           |
| 7    | Special = Yes     | Special characters added               |
| 8    | All options = Yes | All selected character types available |

---

## ✅ Advantages

* Simple and easy to use.
* Generates passwords quickly.
* Allows password customization.
* Requires no external Python packages.
* Uses Python's built-in modules.
* Includes input validation.
* Provides basic password-strength feedback.
* Demonstrates practical use of Python programming concepts.

---

## ⚠️ Limitations

The current version has some limitations:

* It is a command-line application.
* Password strength is evaluated using a basic scoring system.
* The program does not guarantee that every selected character category will appear in the generated password.
* Generated passwords are not saved or stored.
* There is no graphical user interface.
* The current version does not include a clipboard-copy feature.

---

## 🚀 Future Improvements

The project can be improved in the future by adding:

* 🖥️ **Graphical User Interface (GUI)** using Tkinter.
* 📋 **Copy-to-clipboard** functionality.
* 🔐 More advanced password-strength analysis.
* 🎯 Guaranteed inclusion of selected character types.
* ⚙️ More password customization options.
* 📜 Password generation history.
* 👁️ Show/hide password functionality.
* 📊 A visual password-strength indicator.

---

## 🎓 Learning Outcomes

By developing this project, the following concepts and skills were practiced:

* Python programming fundamentals.
* Working with built-in modules.
* String manipulation.
* Conditional statements.
* Loops.
* Exception handling.
* User input validation.
* Boolean expressions.
* Random character generation.
* Problem-solving and application development.

---

## 🔒 Security Note

This project is intended primarily as a **Python programming and educational project**.

The generated passwords are displayed directly in the terminal and are not stored by the application. Users should avoid sharing generated passwords and should use appropriate password-management and security practices for real accounts.

---

## 🔮 Future Scope

The project can be expanded into a complete password-management utility by adding secure password storage, stronger password analysis, a graphical interface, clipboard integration, and additional customization features.

---

## 👩‍💻 Author

**Janhavi**

**Project:** Random Password Generator
**Language:** Python
**Academic Year:** 2026–2027

---

## 📄 License

This project was created for **educational and academic purposes**.
