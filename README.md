# README.md

## *AirBnB Clone Project*

This project is part of the ALX curriculum, aiming to build a simple clone of the AirBnB platform. The project involves creating a command-line interpreter to manage the backend operations of the application.

### **Description**

The AirBnB clone project is designed to:

* Store and manage user data, places, amenities, and more.
* Perform CRUD (Create, Read, Update, Delete) operations through a custom-built console.
* Prepare for web-based interactions in future phases.

The project is divided into several key components:

1. **Command Interpreter**: This allows users to interact with the application from the terminal.
2. **Storage System**: A custom engine to persist and manage data.
3. **Unit Testing**: Comprehensive tests to ensure code quality and reliability.

---

### **Command Interpreter**

#### **How to Start It**

Run the command below in your terminal to start the command interpreter:

```bash
$ ./console.py
```

#### **How to Use It**

Once the console is running, you can use various commands:

* `help`: Displays all available commands.
* `quit`: Exits the console.
* `EOF`: Exits the console using EOF (Ctrl+D).

#### **Examples**

**Interactive Mode:**

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$
```

**Non-Interactive Mode:**

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

---

### **Project Structure**

* **`models/`**: Contains the data models of the project.
* **`tests/`**: Unit test modules.
* **`console.py`**: The main entry point for the command interpreter.

---

### **Requirements**

* **Python Version**: 3.8.5
* **Operating System**: Ubuntu 20.04 LTS
* **Code Style**: Pycodestyle 2.7.*

---

### **Authors**

A list of all contributors to this project is provided in the AUTHORS file.

---

# AUTHORS

* Kelvin Tawe [k.tawe@alustudent.com]
* Payang Richard .
    * Repository Url: https://github.com/Sougnabe/alu-AirBnB_clone
