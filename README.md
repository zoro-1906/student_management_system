# 🎓 Student Management System
This project is a full-featured student record management application developed using PyQt6 and SQLite. It provides a clean and interactive interface to manage student data, including adding, searching, editing, and deleting records.

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

Clickable cells that trigger additional options

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

Selecting a row reveals edit/delete actions via the status bar

Dialogs are used for user inputs and confirmations, ensuring a smooth UX

