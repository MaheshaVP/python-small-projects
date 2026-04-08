#exception handling

try:
    num = int(input("Enter a number : "))
    print(10 / num)

except ZeroDivisionError:
    print("Cant divide by zero(0)")

except ValueError:
    print("Please enter a value number")

# else :
#     print("Enter correct value")

finally:
    print("Finally code is executed")

    