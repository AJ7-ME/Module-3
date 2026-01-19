while True:    
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        result = num1 / num2
        print("Result is : ", result)
    except ValueError:
        print("Value Error: Please enter valid integers.")
    except ZeroDivisionError:
        print("Zero Division Error: Cannot divide by zero.")
    except NameError:
        print("Name Error: Variable not defined.")
    except:
        print("An unexpected error occurred.")
    finally:
        print("Execution completed.")