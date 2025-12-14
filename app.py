def task():
    tasks = []  # empty list
    print("---WELCOME TO THE TASK MANAGEMENT APP---")

    total_task = int(input("Enter how many tasks you want to add = "))

    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"\nToday's tasks are: {tasks}\n")

    while True:
        operation = int(input("Enter:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit\nChoose option = "))

        # ADD TASK
        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added...\n")

        # UPDATE TASK
        elif operation == 2:
            update_val = input("Enter the task name you want to update = ")
            if update_val in tasks:
                new_task = input("Enter new task = ")
                index = tasks.index(update_val)
                tasks[index] = new_task
                print(f"Task updated to '{new_task}'\n")
            else:
                print("Task not found!\n")

        # DELETE TASK
        elif operation == 3:
            del_val = input("Which task do you want to delete = ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' has been deleted...\n")
            else:
                print("Task not found!\n")

        # VIEW TASKS
        elif operation == 4:
            print(f"Total tasks: {tasks}\n")

        # EXIT
        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid Input\n")


# CALL THE FUNCTION
task()
