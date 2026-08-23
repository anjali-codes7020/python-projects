# 🔐 Smart Password Generator

A simple yet powerful **Password Generator** built with **Python** and **Tkinter**, developed as a mini project for the **B.Vocational Computer Application** course at Gramin Technical & Management Campus, Nanded, under **Dr. Babasaheb Ambedkar Technological University, Lonere**.

The application generates strong, secure passwords using a combination of letters, digits, and special characters — and includes a real-time **password strength checker**.

---

## 📌 Features

- 🎯 **Custom Password Generation** — Convert any word into a stronger password (e.g., `a → @`, `s → $`, `o → 0`, `i → 1`) with a random number and symbol appended.
- 🎲 **Random Strong Password** — Instantly generate a fully random 12-character password using letters, digits, and symbols.
- 📊 **Password Strength Meter** — Automatically checks and displays password strength as `Weak`, `Medium`, or `Strong` (color-coded: red, orange, green).
- 📋 **Copy to Clipboard** — Copy the generated password with a single click.
- 🧹 **Clear Fields** — Reset input and output fields instantly.
- 🖥️ **Simple GUI** — Built with Tkinter for an easy-to-use desktop interface.

---

## 🖼️ Preview

```
+--------------------------------------+
|        Password Generator             |
|                                        |
|  Enter Word: [ ANJALI            ]    |
|                                        |
|      [ Generate Password ]            |
|      [ Random Strong Password ]       |
|                                        |
|  Generated Password: [ ANJALI8%  ]    |
|                                        |
|         Strength: Medium              |
|                                        |
|      [ Copy Password ]  [ Clear ]     |
+--------------------------------------+
```

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **GUI Library:** Tkinter
- **Modules Used:** `random`, `string`, `tkinter`, `tkinter.messagebox`

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system (Tkinter ships with standard Python installations)

### Installation & Run

1. Clone the repository
   ```bash
   git clone https://github.com/<your-username>/password-generator.git
   cd password-generator
   ```

2. Run the application
   ```bash
   python password_generator.py
   ```

That's it — no external dependencies required!

---

## 🧠 How It Works

1. **Word-based Generation:** Enter a word, and the app substitutes common letters with lookalike symbols/numbers (`a→@`, `s→$`, `o→0`, `i→1`), then appends a random digit and symbol.
2. **Random Generation:** Generates a fully randomized 12-character password using `random.choice()` over a pool of letters, digits, and symbols.
3. **Strength Check:** Evaluates the password based on length (≥8), presence of uppercase, lowercase, digits, and symbols — scoring it to classify as Weak, Medium, or Strong.

---

## 📂 Project Structure

```
password-generator/
│
├── password_generator.py   # Main application file
└── README.md                # Project documentation
```

---

## 🔮 Future Scope

- [ ] Add options to select specific character types (letters, digits, symbols)
- [ ] Add minimum character requirements (at least one symbol, one digit, etc.)
- [ ] Integrate encryption techniques for secure password storage
- [ ] Connect the application with a database for saving passwords
- [ ] Develop a web-based version using Flask or Django
- [ ] Create a mobile application version
- [ ] Add multi-language support
- [ ] Add user authentication (login system)
- [ ] Generate QR codes for passwords
- [ ] Integrate two-factor authentication support
- [ ] Add password expiry reminder feature
- [ ] Convert into a full password manager system

---

## 📚 References

- [Python Official Documentation](https://docs.python.org/3/)
- [Random Module Documentation](https://docs.python.org/3/library/random.html)
- [String Module Documentation](https://docs.python.org/3/library/string.html)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [OWASP Password Security Guidelines](https://owasp.org/)

---

## 👩‍💻 Author

**Anjali Patange**
B.Vocational Computer Application & IT
Gramin Technical & Management Campus, Vishnupuri, Nanded

Guided by **Mr. Devde Sir**

---

## 📄 License

This project is open-source and available for educational use. Feel free to fork and build upon it.
