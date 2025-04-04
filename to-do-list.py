# Python To-Do List
tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    for i,task in enumerate(tasks,1):
        print(f'{i}.{task}')

def delete_task(index):
    if index >0 and index<=len(tasks):
        del tasks[index-1]
        print("Enter a valid index")

print('\n To-Do List')
print('1. Add Task')
print('2. View Tasks')
print('3. Delete Task')
print('4. Exit')

while True:

    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Please enter a task: ")
        add_task(task)
    
    elif choice == '2':
        view_tasks()
    
    elif choice == '3':
        index = int(input('Please enter the index of the task: '))
        delete_task(index)
    
    elif choice == '4':
        print("Thanks! have a good day.")
        break    
    
    else:
        print("Enter a valid choice!")

