# Write a Python program to create a decorator that logs the arguments and return value of a function

def decorator(func):
    def wrap(*args, **kwargs):
        # Log the function name and arguments
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")

        # Call the original function
        result = func(*args, **kwargs)

        # Log the return value
        print(f"{func.__name__} returned: {result}")

        # return the result
        return result
    return wrap

@decorator
def multiply_numbers(x,y):
    return x*y
# Call the decoarted function
result = multiply_numbers(10,20)
print("Result: ", result)

