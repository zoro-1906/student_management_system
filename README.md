# 🎓 Student Management System
- Developed a full-featured student record management application using PyQt6 and SQLite.
- Designed a clean and interactive user interface for ease of use.
- Implemented core functionalities including:

- -   Adding new student records

- - Searching existing records

- - Editing student details

- - Deleting records

- Ensured smooth integration between the GUI and database for real-time updates.

- Focused on user experience and efficient data handling.





## 🔍 Overview:
The app offers a user-friendly interface where users can manage student information such as name, course, and mobile number. It’s designed as part of my Python portfolio to demonstrate skills in GUI development, database interaction, and modular coding.

## 📋 Key Features:
✅ CRUD Operations:

- Add new student records

- Search for students by name

- Edit existing student data

- Delete selected student entries

## 🧭 Navigation & UI:

- Menu bar with File, Edit, and Help sections

- Toolbar for quick access to core actions

- Status bar showing contextual actions (Edit/Delete buttons appear on cell click)

## 📐 Table View:

- Interactive QTableWidget to display all student data

- Clickable cells that trigger additional options

## 🧠 Dialog Boxes:

- Custom PyQt dialogs for each operation (Insert, Edit, Delete, Search)

- About dialog explaining the purpose of the app

## 🛠️ Tools & Technologies:
- Python

- PyQt6 for GUI components

- SQLite for lightweight database management

- QTableWidget, QDialog, QMessageBox, QLineEdit, QComboBox for interactivity

- Modular structure with OOP principles

##💡 How It Works:
- Student data is stored in a local SQLite database (database.db)

- The app opens with a data table that auto-loads all student records

- Selecting a row reveals edit/delete actions via the status bar

- Dialogs are used for user inputs and confirmations, ensuring a smooth UX

