import json
import os
from datetime import datetime


def askPriority():
    #This function will ask the user for the priority of its task

    while(True):
        valid_priorities = ["high", "medium", "low"]
        priority = input("Enter your task's priority (high/medium/low): ").lower().strip()

        if priority in valid_priorities:
            return priority
        else:
            print("Enter valid priority. (high/medium/low)")    


def user_input():
    #This function takes task name as user input
    
    task_name = input("\nEnter Task name: ").strip()
    return task_name


def isTaskPresent():

    #The refactored code of searching a task in the list.
    task_name = user_input()
    for index, task in enumerate(tasks_list):
        if (task["task_name"] == task_name):
            return index, True
           
    return None, False
   

def setDueDate():
    while(True):
        dueDate = input("Enter Due Date (DD-MM-YYYY) leave blank if no due date: ")

        if(dueDate == ""):
            return None
    
        if(len(dueDate) == 10):
            return dueDate
    
        else:
            print("Re-Enter the due date in a proper format (DD-MM-YYYY)")


def add_task(): 

    #This function adds a new task to the tasksList using append. 

    task = {"task_name": user_input(), "status": "incomplete", "priority": askPriority(), "due date": setDueDate()}
    tasks_list.append(task)
    print("\nThe task is added Successfully...🤩")


def view_tasks():

    #This function displays all the tasks from  the tasksList using .get("task_name")

    print("\nThe total number of tasks are: ",len(tasks_list))
    for task in tasks_list:
        print("Task Name: ", task.get("task_name"), "\nTask Status: ", task.get("status"), "\nTask Priority: ", task.get("priority"), "\nTask Due Date: ", task.get("due date"), "\n")
 

def complete_task():

    #This function searches for the task in a tasksList and updates the satus of task if is incomplete otherwise displays that the
    #task is completed, and tells wheteher if the task is present in the list or not.

    index, isPresent = isTaskPresent()

    if(isPresent):
        if (tasks_list[index]["status"] == "incomplete"):
            tasks_list[index]["status"] = "completed"
            print("\nThe status is updated. The new status is: \n")
            print("Task Name: ", tasks_list[index]["task_name"], "\nTask Status: ", tasks_list[index]["status"])

        else:
            print("The status is already updated.")
    else:
        print("\nThe task does not exist in your To-Do List.")


def delete_task(): 

    #This function enumerates through taskList and delete the task with specific name using its index.

    
    index, isPresent = isTaskPresent()

    if(isPresent):
        del tasks_list[index]
        print("The task is deleted Successfully. ")

    else:
        print("\nThe task does not exist in your To-Do List.")


def save_tasks(filename, tasks_list):

    #It will save data to the file
    #json.dump() is used to covert python Data Structures to the JSON format and write directly to the file. 
    with open(filename, "w") as file:
        json.dump(tasks_list, file, indent = 4)
        print("Tasks have been saved successfully.")


def load_tasks(filename):

     #It will load data from the file
     ##json.load() is used to read from the file and covert JSON format to the python Data Structures . 
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    else:
        return []


def filter_tasks():
    while True:
        filter_choice = input("Enter filter choice: \n1 for Status. \n2 for Priority: ")
        if (filter_choice == "1"):
            status_filter()
            break
    
        elif(filter_choice == "2"):
            priority_filter()
            break

        else:
            print("\nEnter valid choice \n1 for Status. \n2 for Priority: ")


def status_filter():
    filtered_tasks_list = []
    while True:
        status_choice = input("\nEnter status (completed/incomplete): ").lower().strip()
        if status_choice in ["completed", "incomplete"]:
            break
        else:
            print("\nEnter valid choice")
    
    for task in tasks_list:
        if (task["status"] == status_choice):
            filtered_tasks_list.append(task)

    if not filtered_tasks_list:
        print("No such tasks exist with ", status_choice, " status.")
    else:
        view_filtered_tasks(filtered_tasks_list)


def priority_filter():
    filtered_tasks_list = []
    while True:
        priority_choice = input("\nEnter status (high/medium/low): ").lower().strip()
        if priority_choice in ["high", "medium", "low"]:
            break
        else:
            print("\nEnter valid choice")
    
    for task in tasks_list:
       if (task["priority"] == priority_choice):
           filtered_tasks_list.append(task)

    if not filtered_tasks_list:
        print("No such tasks exist with ", priority_choice, " status.")
    else:
        view_filtered_tasks(filtered_tasks_list)
       

def view_filtered_tasks(filtered_tasks_list):

    print("\nThe total number of filtered tasks are: ",len(filtered_tasks_list), "\n")
    for task in filtered_tasks_list:
        print("Task Name: ", task.get("task_name"), "\nTask Status: ", task.get("status"), "\nTask Priority: ", task.get("priority"), "\nTask Due Date: ", task.get("due date"), "\n")
 
 
def sort_tasks():
    while True:
        sort_choice = input("Enter filter choice: \n1 By Priority . \n2 By Due Date: ")
        if (sort_choice == "1"):
            priority_sort(tasks_list)
            break
    
        elif(sort_choice == "2"):
            dueDate_sort(tasks_list)
            break

        else:
            print("\nEnter valid choice \n1 By Priority . \n2 By Due Date: ")


def priority_sort(tasks):
    priority_order = {"high": 1, "medium": 2, "low": 3}
    
    tasks.sort(key = lambda x: priority_order[x["priority"].lower()] )

    view_filtered_tasks(tasks)


def dueDate_sort(tasks):

    tasks.sort(key= lambda t: datetime.strptime(t["due date"], "%d-%m-%Y") if t.get("due date") else datetime.max)

    view_filtered_tasks(tasks)


filename = "tasks.json"
tasks_list = load_tasks(filename)

while (True):

    print("\n\n---------Main Menu-------------")
    print("\nEnter 1 to add a task. \nEnter 2 to view tasks. \nEnter 3 to complete task. \nEnter 4 to delete a task. \nEnter 5 to Filter Tasks. \nEnter 6 to Sort Tasks. \nEnter 7 to Exit.\n")
    try:
        choice = int(input("Enter your choice:  "))
        if(choice == 1):
            add_task()
    
        elif(choice == 2):
            view_tasks()

        elif(choice == 3):
            complete_task()

        elif(choice == 4):
            delete_task()

        elif (choice == 5):
            filter_tasks()

        elif (choice == 6):
            sort_tasks()

        elif (choice == 7):
            save_tasks(filename, tasks_list)
            print("You have opted to Exit. Ba-Bye 👋")
            break

        else:
            print("Enter appropriate choice.")

    except ValueError:
        print("The input should be Integer in the valid range.")