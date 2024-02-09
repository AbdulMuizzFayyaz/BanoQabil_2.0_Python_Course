# Abdul_Muizz
# 0321-2266448
# www.legendgamerz@gmail.com

# Project No. 2:
# To do list: A simple program which will store task and display menu with options.

#First we import "os" library.
import os

#Define the filename for storing the tasks
TASK_FILE = "tasks.txt"

#Check if the task file exists. If not, create it.
if not os.path.isfile(TASK_FILE):       #It is checking the file path.
    with open(TASK_FILE, "w") as f:     #It opens the file if present,otherwise creates one.
        f.write("")

#Function to load the tasks from the file into the tasks list.
def load_tasks():
    with open(TASK_FILE, "r") as f:     #Opens the file as readable only.
        tasks = f.readlines()
    #Remove the newline characters from each task.
    tasks = [task.strip() for task in tasks]
    return tasks

#Save the tasks from the list to the file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:     #Opens the file in editable to save the changes made.
        for task in tasks:
            f.write(task + "\n")

#Print a welcome message
print("Welcome to To Do List")

#Load the tasks from the file
tasks = load_tasks()

#Define the functions to add, view, delete, and mark tasks as done.
#Function to add a new task.
def add_task():
    new_task = input("Enter the new task :")        #Takes the input of new task.
    tasks.append(new_task)                          #Append the new task.
    save_tasks(tasks)                               #Save the changes made.
    print(f"Task '{new_task}' added successfully!") #Print an appropiate statment regarding task being added.
#Function to view task.
def view_task():
    if not tasks:                           #Checking if there is any task to view.
        print("No Task to display yet")     #Print an appropiate statement.
    else:
        print("Here is your tasks!")        #Otherwise displays the task.
        for i in range(len(tasks)):         #Using for loop to view range of task by len(tasks).
            print(f"{i+1}.{tasks[i]}")      #{i+1} is for numbering tasks , {task[i]} prints the task from the list.
#Function to delete task.
def delete_task():
    try:                                    #Using error handling to avoid errors.
        if not tasks:                       #Checking if there is any task to delete.
            print("No tasks to delete!")    #Print the appropiate statement.
            return
        task_index = int(input("Enter the index of the task you want to delete( index starts from 0):"))    #Otherwise take the task index.
        if task_index<0 or task_index>=len(tasks):                                                          #Checking if user input is valid.
            print("Invalid task input! PLease enter a valid task index(index starts from 0).")              #If not valid,prints a statement.
            return
        del tasks[task_index]                   #If index is valid, then delete the task.
        save_tasks(tasks)                       #Save the changes made.
        print("Task deleted successfully!")     #Print an appropiate statement.
    except ValueError:                          #If their is value error then execute the except block, and print an appropiate statement.
        print("Invalid Input!Please enter a correct integer index.")
#Function to mark task as done.
def mark_task_done():
    try:                                        #Using error handling to avoid errors.
        if not tasks:                           #Checking if there is any task to delete.
            print("No task to mark as done.")   #Print an appropiate statement.
            return
        task_index = int(input("Enter the index of the task you want to mark as done(index starts from 0):"))   #Otherwise take the task index.
        if task_index<0 or task_index>=len(tasks):                                                              #Checking if user input is valid.
            print("Invalid task input!Please enter a valid task index(index starts from 0).")                   #If not valid,print a statement.
        tasks[task_index] = f"[Done]{tasks[task_index]}"    #If index is valid,then mark task as done.
        save_tasks(tasks)                                   #Save the change made.
    except ValueError:                                      #If there is value error then execute except block,and print a appropiate statement.
        print("Invalid input!Please enter a correct integr index.")

# Implement the main program loop
while True:         #A while loop which is always true so the program keep running until the loop breaks.
    choice = input("\n 'a' to add new task. \n 'v' to view tasks. \n 'd' to delete task. \n 'm' to mark task as done. \n 'q' to quit  \n Enter your choice :").lower()
    if choice == 'a':       #Take the input of choice from user, and then use conditions to call the function we defined.
        add_task()
    elif choice == 'v':
        view_task()
    elif choice == 'd':
        delete_task()
    elif choice == 'm':
        mark_task_done()
    elif choice == 'q':
        break
    else:                  #If user input is not in the if block then execute else block ,and print an appropiate statement.
        print("Invalid input!Please try again :)")
#Printing a bye message.
print("Bye👋👋")