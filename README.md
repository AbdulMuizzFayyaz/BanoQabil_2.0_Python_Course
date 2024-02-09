# To-do List

## Problem Statement
A simple To-do list application crafted with python.

## Code Structure
This simple python program make use of “os” library to manipulate the file. First our text file directory is stored in a variable. Then using ”if not  os.path.isfile(TASK_FILE)”  to check if file exists otherwise create it.Then functions like load_task() ,save_task(tasks) ,add_task() ,view_task() ,delete_task() ,mark_task_done() are declared. At last these functions are employed to a while loop to ensure smooth operation. In while loop user enter a choice and calls a function.

## How to Run
1.	First ensure that you have python installed.
2.	Open a terminal or command prompt.
3.	Navigate the directory containing “To_Do_List.py”.
4.	Run the script using “python To_Do_List.py”.

## Example Output
Welcome to To Do List

‘a’ to add new task.

‘v’ to view tasks.

‘d’ to delete task.

‘m’ to mark task as done. 

‘q’ to quit

Enter the choice:
