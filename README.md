# Python Project: Console To-Do List Manager 🚀

## Project Overview

Welcome to my Python project, a simple yet powerful console-based To-Do List Manager! 👋

As a beginner in Python, this project was a fantastic journey into understanding core programming concepts and building a practical application from scratch. It's designed to help users efficiently manage their daily tasks, ensuring nothing gets missed. This application runs entirely in your terminal, providing a straightforward and intuitive experience.

Through this project, I've focused on solidifying my Python fundamentals and embracing best practices like code modularity and robust error handling.

## Key Features ✨

This To-Do List application comes packed with essential functionalities to keep you organized:

* **Add New Tasks:** Easily add new tasks to your list. Each task is by default marked as `incomplete`.
* **View All Tasks:** Get a clear overview of all your tasks, neatly numbered with their current status (`completed`/`incomplete`)
* **Mark Tasks Complete:** Mark any task as `complete` by simply entering its name.
* **Delete Tasks:** Remove unwanted tasks from your list with a quick command.
* **Intuitive Menu System:** A clear, interactive menu guides you through all available options.
* **Robust Input Handling:** Designed to handle invalid user inputs gracefully, ensuring the application remains stable and user-friendly.

### What I Learned & Refactored 🧠

This project was a huge learning curve, and I'm particularly proud of the following improvements I implemented:

* **Reusable Input Function:** Instead of repeating `input()` calls and their associated validation logic everywhere, I created a dedicated function. This significantly reduces code duplication and makes the code cleaner.
* **Modular Task Existence Check (`isTaskPresent`):** I abstracted the logic for checking if a task exists in the list into its own function. This makes the `complete_task()` and `delete_task()` functions much more readable and focused on their primary responsibilities.
* **Enhanced Error Handling:** Implemented `try-except` blocks, especially for user choices, to catch `ValueError` if a non-integer input is provided, guiding the user with helpful messages instead of crashing.

## Technologies Used 🛠️

* **Python 3 or above**

## How to Run the Application 🏃‍♀️

Getting started with the To-Do List Manager is easy!

1.  **Prerequisites:** Ensure you have Python 3 or above installed on your system. If not, you can download it from the [official Python website](https://www.python.org/downloads/).
2.  **Download the Code:**
    * Clone this repository: `git clone https://github.com/MoizaA17/my-todo-app.git`
    * Or, download the ZIP file directly from GitHub.
3.  **Navigate to the Project Directory:** Open your terminal or command prompt and navigate to the folder where you've saved the `todo_app.py` file.
    ```bash
    cd path/to/your/project_folder
    ```
4.  **Execute the Application:** Run the application using the Python interpreter:
    ```bash
    python main.py
    ```
5.  Follow the on-screen menu to manage your tasks!

## Future Enhancements (Coming Soon!) 💡

I'm excited to continue improving this project! Here are some features I plan to implement next:

* **Persistent Storage:** Save tasks to a file (e.g., JSON) so they are not lost when the application closes. ✔
* **Task Priorities:** Allow users to assign priorities (High, Medium, Low) to their tasks. ✔
* **Due Dates:** Add functionality to set and track due dates for tasks. ✔
* **Filtering Options:** Enable users to filter tasks by status (complete/incomplete) or priority. ✔

## Author 👩‍💻

* **MoizaA17** - Connect with me on [GitHub](https://github.com/MoizaA17)!

---
