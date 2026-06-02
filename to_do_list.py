# Display the title of the To-Do List application
print("--- To-Do List ---")

# Display a separator line
print("-----------------------------------")

# Display the menu options
print("""1. Add Task
2. View Tasks
3. Remove Task
4. Exit""")

# Display another separator line
print("-----------------------------------")

# Create an empty list to store tasks
list = []

# Run the program continuously until the user chooses to exit
while True:

    try:
        # Get the user's menu choice and convert it to an integer
        user_choice = int(input("Enter the Number : "))
    
        # Exit the program if the user selects option 4
        if user_choice == 4:
            break

        # Add tasks if the user selects option 1
        elif user_choice == 1:

            while True:
                # Display a separator line
                print("-----------------------------------")

                # Ask the user to enter a task
                task = input("Enter the task (Type 'done' to exit) : ")

                # Stop adding tasks if the user types 'done'
                if task == "done":
                    break

                # Add the entered task to the list
                else:
                    list.append(task)  

        # Remove a task if the user selects option 3
        elif user_choice == 3:
            
            # Display a separator line
            print("-----------------------------------")

            # Show the current list of tasks
            print(list)

            # Ask the user for the task name to remove
            task = input("Enter the task name for remove : ")

            # Remove the task if it exists in the list
            if task in list:
            
                list.remove(task)

            # Display an error message if the task is not found
            else:
                print("Task not found")
                print("-----------------------------------")

        # View all tasks if the user selects option 2
        elif user_choice == 2:
            print("-----------------------------------")
            print(list)

    # Handle invalid input or unexpected errors
    except:
        print("You enter a invalid option")
        continue
