import re
import sys
todo_list=[]
class todo():

    def __init__(self):
        pass

    def add_task(self,task,date,time,current_status):
        index=1
        if todo_list == '':
            todo_list.append([index,task,date,time,current_status])
            index+=1
            print("Task Added")
        
        else:
            todo_list.append([index,task,date,time,current_status])
            print("Task Added")

        return True
    
    def view_tasks(self):
        print("Index  Task   Date  Time  Status")
        for i in todo_list:
            for item in i:      
                print(f"{item}",end=" ")
            print()

        if todo_list=="":
            print(f"{todo_list} is empty")
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

    
    def delete_task(self,task):
        for i in todo_list:
            for index,stored_task,date,time,status in i:
                if task.lower().strip() == stored_task.lower().strip():
                    todo_list.remove(i)

        else:
            print("Cannot Find Task or List is Empty")
        print("--Task Removed--")

    def main(self):
        print("Welcome this is an todo_list")
        counter=0
        while counter<5:
            if (user_Action:=input("""Approprite Actions must be choosen:
Press 1- Adding a task
Press 2- For Viewing All task
Press 3- For updating Task
Press 4- for deleting a task
return to exit the list once exited all the tasks will be permanently deleted 
""")) and re.match(r"^[1-9\s]*$",user_Action):
                if user_Action=='1':
                    if (task:=input("Enter Task: ")) and re.match(r"^[0-9A-Za-z._]+$",task):
                        task=task
                    if (date:=input("Enter date: ")) and re.match(r"^(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/](\d{4})$",date):
                        date=date
                    if (time:=input("Enter Time: ")) and re.match(r"^(0[1-9]|1[0-2]):([0-5][0-9])$",time):
                        time=time
                    if (status:=input("Enter Status: ")) and  status in ['active','completed','pending']:
                        status=status
                    else:
                        print('Retry...')
                        counter+=1 
                    self.add_task(task,date,time,status)

                elif user_Action == '2':
                    self.view_tasks()

                elif user_Action == '3':
                    if (user_task := input("Enter Task Name: ")) and re.match(r"^[0-9A-Za-z._]+$",user_task):
                        task_to_update=user_task
                    if (user_item := input("Enter Field To Update: ")) and (user_item in ['task','date','time','status']):
                        update_item = user_item
                    updated_value= input(f"Value for {user_item} field: ")
                    self.update_task(task_to_update,update_item,updated_value)

                elif user_Action == '4':
                    if (user_task := input("Enter Task Name: ")) and re.match(r"^[0-9A-Za-z._]+$",user_task):
                        task_to_delete=user_task

                    self.delete_task(task_to_delete)

                elif user_Action ==' ':
                    print("Thanks for using this program")
                    break

                else:
                    counter+=1
                    print("Invalid Choice")

        else:
            sys.exit("To Many invalid attempts")


obj=todo()
obj.main()

        
        
