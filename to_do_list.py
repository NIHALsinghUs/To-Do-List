print("--- To-Do List ---")

print("-----------------------------------")

print("""1. Add Task
2. View Tasks
3. Remove Task
4. Exit""")

print("-----------------------------------")

list = []

while True:

    try:
        user_choice = int(input("Enter the Number : "))
    
        if user_choice == 4:
            break

        elif user_choice == 1:

            while True:
                print("-----------------------------------")
                task = input("Enter the task (Type 'done' to exit) : ")

                if task == "done":
                    break

                else:
                    list.append(task)  

        elif user_choice == 3:
            
            print("-----------------------------------")
            print(list)
            task = input("Enter the task name for remove : ")

            if task in list:
            
                list.remove(task)
            
            else:
                print("Task not found")
                print("-----------------------------------")

        elif user_choice == 2:
            print("-----------------------------------")
            print(list)

    except:
        print("You enter a invalid option")
        continue