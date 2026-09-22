tasks =[]

def show_tasks(tasks):
    if tasks:
        print('Tasks:')
        for index, task_in_list in enumerate(tasks, start=1):
            print(f'{index}. {task_in_list}')
    else:
        print('List is empty')

def add_task(tasks):
    task = input(('Enter task:\n'))
    tasks.append(task)
    print('Task added')

def remove_task(tasks):
    try:
        rm = int(input('Write number of task that you want to remove:\n'))
        if 1 <= rm <= len(tasks):
            tasks.pop(rm-1)
        else:
            print('Invalid number')
    except ValueError:
        print('Invalid option')
    except IndexError:
        print('Invalid task number.')

choose = ''
while choose != 4:
    print('==================\n    To-Do List\n==================\n\n')
    print('1. Show tasks\n\n2. Add task\n\n3. Remove task\n\n4. Exit\n\n')
    try:
        choose = int(input('Choose an option:\n'))
        if choose < 1 or choose > 4:
            print('Wrong number')
    except ValueError:
        print('Invalid option')
        continue
    if choose == 1:
        show_tasks(tasks)
    elif choose == 2:
        add_task(tasks)
    elif choose == 3:
        remove_task(tasks)
    