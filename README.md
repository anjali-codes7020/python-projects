# 🔐 Smart Password Generator

A simple and interactive **Password Generator** built with **Python**
and **Tkinter**. This mini project was developed as part of my
B.Vocational Computer Application course.

The application can generate stronger passwords, check password
strength, copy passwords to the clipboard, and clear the input/output
fields.

## ✨ Features

-   🎯 **Custom Password Generation** --- Enter a word and convert
    common letters into stronger alternatives such as `a → @`, `s → $`,
    `o → 0`, and `i → 1`, with a random number and symbol added.
-   🎲 **Random Strong Password** --- Generate a random 12-character
    password containing letters, digits, and special characters.
-   📊 **Password Strength Meter** --- Checks the generated password and
    displays its strength as **Weak**, **Medium**, or **Strong**.
-   📋 **Copy Password** --- Copy the generated password to the
    clipboard with one click.
-   🧹 **Clear Button** --- Quickly reset the input and generated
    password fields.
-   🖥️ **GUI Application** --- Simple desktop interface built using
    Tkinter.

## 🖼️ Application Preview

![Smart Password Generator](Screenshot%202026-08-23%20115324.png)


## 🛠️ Tech Stack

-   **Programming Language:** Python 3
-   **GUI:** Tkinter
-   **Modules:** `random`, `string`, `tkinter`, `tkinter.messagebox`

## 🚀 Getting Started

### Prerequisites

-   Python 3.x
-   Tkinter (usually included with standard Python installations)

### Installation

1.  Clone this repository:

``` bash
git clone https://github.com/<your-username>/smart-password-generator.git
```

2.  Open the project folder:

``` bash
cd smart-password-generator
```

3.  Run the application:

``` bash
python password_generator.py
```

No external Python packages are required.

## 🧠 How It Works

### 1. Custom Password Generation

The user enters a word. The program replaces selected characters with
common symbols or numbers and adds a random digit and special character.

Example:

``` text
Anjali → Anj@l1 + random digit + symbol
```

### 2. Random Password Generation

The application creates a random password using a combination of:

-   Uppercase letters
-   Lowercase letters
-   Numbers
-   Special characters

### 3. Password Strength Checking

The program checks factors such as:

-   Password length
-   Uppercase letters
-   Lowercase letters
-   Digits
-   Special characters

It then classifies the password as **Weak**, **Medium**, or **Strong**.

## 📂 Project Structure

``` text
smart-password-generator/
│
├── password_generator.py
├── README.md
└── screenshots/
    └── password-generator.png
```

## 🎯 Learning Outcomes

This project helped me practice:

-   Python programming fundamentals
-   Functions and conditional statements
-   Random password generation
-   String manipulation
-   GUI development with Tkinter
-   Clipboard functionality
-   Basic password-strength evaluation
-   Organizing and documenting a GitHub project

## 🔮 Future Improvements

-   [ ] Add password length selection
-   [ ] Allow users to choose letters, numbers, and symbols
-   [ ] Add minimum character requirements
-   [ ] Improve password-strength rules
-   [ ] Add a password history feature
-   [ ] Add a web version using Flask or Django
-   [ ] Develop a complete password-manager version
-   [ ] Add secure password storage and encryption

## 📚 References

-   [Python Documentation](https://docs.python.org/3/)
-   [Python Random
    Module](https://docs.python.org/3/library/random.html)
-   [Python String
    Module](https://docs.python.org/3/library/string.html)
-   [OWASP Password Security Guidelines](https://owasp.org/)

## 👩‍💻 Author

**Anjali Patange**

B.Vocational Computer Application & IT\
Gramin Technical & Management Campus, Vishnupuri, Nanded

Guided by **Mr. Devde Sir**

## 📄 License

This project is created for educational purposes and is open for further
improvement.
