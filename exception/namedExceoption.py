try:
    x = int(input("Enter a number: "))
    y = 1/x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Please enter an integer.")
except:
    print("Something went wrong.")

print("All done!")            
