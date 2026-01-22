def shutdown(choice1):
    choice = choice1.lower()
    if choice == "yes":
        print("Shutting down")
    elif choice == "no":
        print("Abort shutdown")
    else:
        print("Sorry")


user_input = input("Do you want to shutdown the system? (Yes/No): ")
shutdown(user_input)
print("Program has been shutdown.")
