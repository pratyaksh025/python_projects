import re
import sys

todo_list = []

class todo():

    def __init__(self):
        pass

    def add_task(self, task, date, time, current_status):
        index = len(todo_list) + 1  # dynamic index
        todo_list.append([index, task, date, time, current_status])
        print("Task Added")
        return True

    def view_tasks(self):
        if not todo_list:  # check if list is empty
            print("Todo list is empty")
            return
        print("Index  Task   Date  Time  Status")
        for i in todo_list:
            for item in i:
                print(f"{item}", end=" ")
            print()
        print("All Tasks are displayed Successfully")

    def update_task(self, task, update_item, updated_value):
        found = False
        for i in todo_list:  # i is like [index, task, date, time, status]
            stored_task = i[1]
            if task.lower().strip() == stored_task.lower().strip():
                found = True
                if update_item.lower() == 'task':
                    i[1] = updated_value
                elif update_item.lower() == 'date':
                    i[2] = updated_value
                elif update_item.lower() == 'time':
                    i[3] = updated_value
                elif update_item.lower() == 'status':
                    i[4] = updated_value
                else:
                    print("Cannot Fulfil Requirements!!")
        if not found:
            print(f"{task} not found in todo_list")

    def delete_task(self, task):
        found = False
        for i in todo_list:
            if task.lower().strip() == i[1].lower().strip():
                todo_list.remove(i)
                found = True
                print("--Task Removed--")
                break
        if not found:
            print("Cannot Find Task or List is Empty")

    def main(self):
        print("Welcome this is a todo_list")
        counter = 0
        while counter < 5:
            if (user_Action := input("""Appropriate Actions must be chosen:
Press 1- Adding a task
Press 2- For Viewing All tasks
Press 3- For updating Task
Press 4- For deleting a task
Type 'return' to exit the list. Once exited, all the tasks will be permanently deleted 
""")) and re.match(r"^[1-9\s]*$", user_Action):
                
                if user_Action == '1':
                    if (task := input("Enter Task: ")) and re.match(r"^[0-9A-Za-z._]+$", task):
                        task = task
                    if (date := input("Enter date (DD/MM/YYYY): ")) and re.match(r"^(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/](\d{4})$", date):
                        date = date
                    if (time := input("Enter Time (HH:MM): ")) and re.match(r"^(0[0-9]|1[0-2]):([0-5][0-9])$", time):
                        time = time
                    if (status := input("Enter Status (active/completed/pending): ")) and status in ['active', 'completed', 'pending']:
                        status = status
                    else:
                        print('Retry...')
                        counter += 1
                        continue
                    self.add_task(task, date, time, status)

                elif user_Action == '2':
                    self.view_tasks()

                elif user_Action == '3':
                    if (user_task := input("Enter Task Name: ")) and re.match(r"^[0-9A-Za-z._]+$", user_task):
                        task_to_update = user_task
                    if (user_item := input("Enter Field To Update (task/date/time/status): ")) and (user_item in ['task', 'date', 'time', 'status']):
                        update_item = user_item
                    updated_value = input(f"Value for {user_item} field: ")
                    self.update_task(task_to_update, update_item, updated_value)

                elif user_Action == '4':
                    if (user_task := input("Enter Task Name: ")) and re.match(r"^[0-9A-Za-z._]+$", user_task):
                        task_to_delete = user_task
                    self.delete_task(task_to_delete)

                elif user_Action.lower() == 'return':
                    print("Thanks for using this program")
                    break

                else:
                    counter += 1
                    print("Invalid Choice")

        else:
            sys.exit("Too many invalid attempts")

obj = todo()
obj.main()
