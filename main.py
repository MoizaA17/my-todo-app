import json
import os

tasks_list = []

def user_input():
    #This function takes task name as user input
    
    task_name = input("\nEnter Task name: ")
    return task_name

def isTaskPresent():

    #The refactored code of searching a task in the list.
    task_name = user_input()
    for index, task in enumerate(tasks_list):
        if (task["task_name"] == task_name):
            return index, True
           
    return None, False


def add_task(): 

    #This function adds a new task to the tasksList using append. 

    task = {"task_name": user_input(), "status": "incomplete"}
    tasks_list.append(task)
    print("The task is added Successfully...🤩")


def view_tasks():

    #This function displays all the tasks from  the tasksList using .get("task_name")

    print("\nThe total number of tasks are: ",len(tasks_list))
    for task in tasks_list:
        print("Task Name: ", task.get("task_name"), "\nTask Status: ", task.get("status"))


def complete_task():

    #This function searches for the task in a tasksList and updates the satus of task if is incomplete otherwise displays that the
    #task is completed, and tells wheteher if the task is present in the list or not.

    index, isPresent = isTaskPresent()

    if(isPresent):
        if (tasks_list[index]["status"] == "incomplete"):
            tasks_list[index]["status"] = "completed ✔"
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
    with open(filename, "w") as file:
        json.dump(tasks_list, file, indent = 4)

def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    else:
        return []



while (True):
    print("\n\n---------Main Menu-------------")
    print("\nEnter 1 to add a task. \nEnter 2 to view tasks. \nEnter 3 to complete task. \nEnter 4 to delete a task. \nEnter 5 to Exit.\n")
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
            print("You have opted to Exit. Ba-Bye 👋")
            exit()

        else:
            print("Enter appropriate choice.")

    except ValueError:
        print("The input should be Integer in the valid range.")