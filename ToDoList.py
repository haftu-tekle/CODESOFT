
import sys
tasks={}
task_number=1
def save_to_file(filename='task.txt'):
    with open(filename, 'w') as file:
        for number, task in tasks.items():
            file.write(f'{number}:{task}')
            print('The task has been added successfully')
            
def add_task():
    global task_number
    task=input('Enter the task you want to add')
    tasks[task_number]=task
    print(f'Task {task} has been added succesfully with the number {task_number}')
    task_number+=1
def view_task():
    if not tasks:
        print('There is no tasks yet')
    else:
        for number, task in tasks.items():
                print(f'{number}.{task}')
def delete_task():
    if not tasks:
        print('There is no tasks to delete')
        return
    
    view_task()
    try:
        choice=int(input('select the task you want to delete'))
        if choice in tasks:
            del tasks[choice]
            print(f'The task {choice} has been deleted succesfully')
        else:
            print('Invalid task number please try again!!')
    except ValueError:
        print('You have enered invalid input!!')
def stop_app():
    print('Exiting the system......')
    sys.exit(0)

    
if __name__=='__main__':

    print('Welcome to your to do list')
    print('')
    print('Actions')
    

    print('1. Add Task \n2. List Task\n3. Delete Task \n4. Quit task')
  

    while True:
        choice=int(input('Enter an action from above'))
        if choice==1:
            add_task()
        elif choice==2:
             view_task()
        elif choice==3:
            delete_task()
        elif choice==4:
            stop_app()
