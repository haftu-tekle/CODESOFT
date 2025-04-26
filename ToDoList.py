
import sys
task={}
task_number=1
def save_to_file(filename='task.txt'):
    with 
def load_from_file(filename='task.txt'):
    tasks.clear()
    global task_number
    try:
        with open (filename, 'r') as file:
            for line in file:
                number_str, task=line.strip().split(':',1)
                try:
                    number=int(number_str)
                    tasks[number]=task
                    if number>=task_number:
                        task_number=1+number
                except ValueError:

                    print(f'Warning: skipping values in file{line.strip()}')
    except FileNotFoundError:
        print(f'file named{filename} not found')
def delete_from_file(task_number_to_be_deleted, filename='task.txt'):
    update_tasks={}
    global task_number
    tasks.clear()
    task_deleted=False
    try:
        with open(filename, 'r') as file:
            for line in file:
                numbr_str, task=line.strip().split(':',1)
                number=int(numbr_str)
                if number!=task_number_to_be_deleted:
                    update_tasks[number]=task
                else:
                    task_deleted=True
        with open(filename, 'r') as file:
            for number, task in sorted(update_tasks.items()):
                file.write(f'{number}:{task}')
            task_number=len(update_tasks) if update_tasks else 0
            if task_deleted:
                print(f'{task_number_to_be_deleted} is deleted successfully')
            else:
                print(f'{task_number_to_be_deleted} doesnot exist')


    except ValueError:
        print(f'Warning!: Skipping invalid values in line{line.strip()}')
    except FileNotFoundError:
        print(f'File name {filename} not found')


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
            save_to_file(add_task)
        elif choice==2:
             load_from_file()
             view_task()
        elif choice==3:
            delete_task()
        elif choice==4:
            stop_app()
