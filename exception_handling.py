#This is the code to demonstrate the working of Exception Handling in Python....

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a/b)
except ValueError as e:
    print("Cannot convert string to Integer..." , e)
except ZeroDivisionError as e:
    print("Can't divide a number by 0..." , e)
except Exception as e:
    print("Something went wrong...." , e)
finally:
    print("Thanks for your time...")