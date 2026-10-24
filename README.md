# 🎓 Student Management System

> A lightweight Python CLI application for managing student records with CSV-based storage and essential record management operations.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=white)
![Storage](https://img.shields.io/badge/Storage-CSV-green)
![Interface](https://img.shields.io/badge/Interface-CLI-lightgrey)
![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library-success)
![License](https://img.shields.io/badge/License-Not%20Specified-lightgrey)

## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Scope and Objectives](#-scope-and-objectives)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation and Setup](#-installation-and-setup)
- [Usage](#-usage)
- [Data Storage](#-data-storage)
- [Limitations and Future Enhancements](#-limitations-and-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

## 🚀 Overview

### Why

Maintaining student information manually can make it difficult to organize records, locate specific students, and keep information up to date. This project provides a straightforward way to manage student records through a command-line interface without requiring a database server or third-party packages.

### What

The Student Management System is a Python application that stores student information in a CSV file and provides basic record management functionality.

### How

The application follows a simple file-based workflow:

1. Users select an operation from the interactive command-line menu.
2. Python collects the required student information or search criteria.
3. The application reads or updates records in `students.csv`.
4. Changes are written to the CSV file when records are added, updated, or deleted.
5. Users receive a message indicating the result of the operation.

### To Whom

This project is suitable for:

- Students learning Python programming.
- Beginners practicing file handling and CSV operations.
- Developers exploring command-line application design.
- Small-scale demonstrations of basic student record management.

## ✨ Features

- **Add Student:** Enter and save a new student record.
- **View Students:** Display saved records in a column-aligned terminal output.
- **Search Student:** Find a student by ID.
- **Update Student:** Modify an existing student's information while retaining current values for fields left blank.
- **Delete Student:** Remove a record using its ID.
- **Interactive Menu:** Navigate the available operations through numbered choices.
- **Persistent Storage:** Save records in a CSV file so changes remain available between application runs.

## 🏗️ Architecture

The application uses a monolithic, single-script architecture with local file storage.

```text
             User
              |
              v
       Command-Line Menu
              |
              v
          student.py
              |
       +------+------+------+------+
       |      |      |      |      |
       v      v      v      v      v
      Add    View  Search Update Delete
       |      |      |      |      |
       +------+------+------+------+
                     |
                     v
                 students.csv
                     |
                     v
             Persistent Records
```

### Core Components

| Component | Responsibility |
|---|---|
| `display_menu()` | Displays available operations |
| `add_student()` | Collects student information and appends a CSV row |
| `view_students()` | Reads and displays stored student records |
| `search_student()` | Searches records by student ID |
| `update_student()` | Updates a matching record and rewrites the CSV file |
| `delete_student()` | Removes a matching record and rewrites the CSV file |
| Main menu loop | Dispatches user selections and exits when requested |

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![CSV](https://img.shields.io/badge/Data%20Format-CSV-217346?style=flat)
![Terminal](https://img.shields.io/badge/Interface-Command%20Line-black?style=flat)

| Technology | Purpose |
|---|---|
| Python | Application logic and user interaction |
| `csv` module | Reading and writing structured records |
| File I/O | Persistent local data storage |
| Command-line interface | Menu navigation and input collection |

The application uses Python's standard library and does not require an external package installation.

## 🎯 Scope and Objectives

### Objectives

- Implement basic student record management operations.
- Demonstrate Python functions, loops, conditionals, and user input.
- Practice reading and writing CSV files.
- Provide a persistent storage mechanism without a database server.
- Keep the application simple to run and understand.

### In Scope

- Adding, viewing, searching, updating, and deleting student records.
- Searching by student ID.
- Storing student information in a local CSV file.
- Interactive terminal-based operation.

### Out of Scope

- Web-based or graphical user interfaces.
- User authentication and role-based access.
- Cloud storage and multi-user collaboration.
- Database-backed transactions.
- Automated report generation.
- Advanced search, filtering, and pagination.

## 📂 Project Structure

```text
STUDENT-MANAGEMENT-SYSTEM/
├── student.py       # Main application and CRUD operations
├── students.csv     # Student record storage
└── .gitattributes   # Git file handling configuration
```

### File Responsibilities

- **`student.py`** — Defines the student fields, displays the menu, and implements record operations.
- **`students.csv`** — Stores student records in comma-separated format.
- **`.gitattributes`** — Configures Git handling for repository files.

## 💻 Prerequisites

- Python 3.6 or later.
- Git, if cloning the repository.
- A terminal or command prompt.

No database, web server, virtual environment, or third-party Python package is required.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/pratikabhang/STUDENT-MANAGEMENT-SYSTEM.git
```

### 2. Navigate to the Project Directory

```bash
cd STUDENT-MANAGEMENT-SYSTEM
```

### 3. Verify Python Installation

```bash
python --version
```

If your system uses `python3`, run:

```bash
python3 --version
```

### 4. Run the Application

On Windows:

```bash
python student.py
```

On macOS or Linux:

```bash
python3 student.py
```

The application displays the interactive menu in the terminal.

**No build step or dependency installation is necessary.**

## ▶️ Usage

After starting the program, the following menu is displayed:

```text
--------------------------------------
 Welcome to Student Management System
--------------------------------------
1. Add New Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Quit
```

Enter the number corresponding to the operation you want to perform.

### 1. Add a Student

Select option `1` and provide the requested fields:

- ID
- Name
- Age
- Email
- Phone
- City

The application appends the entered record to `students.csv`.

### 2. View Students

Select option `2` to display the records currently stored in the CSV file.

### 3. Search for a Student

Select option `3` and enter the student's ID.

The application searches the CSV records and displays the matching student's details, if found.

### 4. Update a Student

Select option `4` and enter the ID of the student to update.

For each field, enter a new value or press Enter to retain the existing value.

### 5. Delete a Student

Select option `5` and enter the ID of the student to remove.

The application rewrites the CSV file without the matching record.

### 6. Quit

Select option `6` to exit the application.

## 💾 Data Storage

Student records are stored locally in `students.csv`.

### Expected Record Structure

The application defines six fields:

| Field | Description |
|---|---|
| `ID` | Student identifier |
| `Name` | Student's name |
| `Age` | Student's age |
| `Email` | Student's email address |
| `Phone` | Student's phone number |
| `City` | Student's city |

### Example CSV Format

```csv
ID,Name,Age,Email,Phone,City
1001,Alex,20,alex@example.com,9876543210,Pune
1002,Jordan,21,jordan@example.com,9876543211,Mumbai
```

The entries above are illustrative examples, not actual repository records.

### Persistence Behavior

- New records are appended to the CSV file.
- Existing records are read from the file for viewing and searching.
- Updates and deletions rewrite the file with the remaining or modified records.
- Data remains on the local filesystem between application runs.

**Important:** Keep the CSV structure consistent with the six fields defined in `student.py`. Existing data with extra columns may cause issues in operations such as updating records.

## 🔮 Limitations and Future Enhancements

Potential improvements include:

- Validate student IDs and prevent duplicate entries.
- Validate age, email, and phone number formats.
- Handle missing, empty, or malformed CSV files safely.
- Ensure CSV records consistently match the expected field count.
- Add confirmation before deleting a student.
- Add unit tests for record operations.
- Separate business logic, storage, and user interface into modules.
- Introduce SQLite or another database for more robust persistence.
- Add sorting, filtering, and export functionality.
- Develop a web interface for broader accessibility.

These are proposed enhancements and are not part of the current feature set.

## 🤝 Contributing

Contributions, bug reports, and improvement suggestions are welcome.

### Contribution Workflow

1. Fork the repository.
2. Clone your fork.
3. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. Implement your changes.
5. Test the affected operations manually.
6. Commit your changes:

   ```bash
   git add student.py
   git commit -m "Improve student record handling"
   ```

7. Push your branch:

   ```bash
   git push origin feature/your-feature-name
   ```

8. Open a pull request against the original repository.

### Guidelines

- Follow standard Python naming conventions.
- Keep functions focused and readable.
- Handle invalid input and file errors appropriately.
- Test add, view, search, update, and delete operations.
- Avoid committing private student information or other sensitive data.

## 📄 License

No `LICENSE` file is listed in the current repository. The project's license is therefore **not specified**.

Before distributing or reusing the code, add an appropriate license file and update this section with the correct license terms.

## 👨‍💻 Author

**Pratik Abhang**

- GitHub: [@pratikabhang](https://github.com/pratikabhang)
- Repository: [STUDENT-MANAGEMENT-SYSTEM](https://github.com/pratikabhang/STUDENT-MANAGEMENT-SYSTEM)

---

⭐ If you find this project useful, consider starring the repository.

*Built with Python and CSV file handling.*
