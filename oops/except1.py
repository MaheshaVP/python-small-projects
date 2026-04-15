#Exception handling

def divide_no():
    try:
        num1 = int(input("Enter a number : "))
        num2 = int(input("Enter a number : "))
        result = num1/num2

    except ZeroDivisionError:
        print("No can't divide by zero")
    
    except ValueError:
        print("Only enter the numbers")
    
    else:
        print("Division successful")
        print(f"result = {result}")

    finally:
        print("Program execution completed")

divide_no()

