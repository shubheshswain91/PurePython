def do_this():
    print("do this")

def do_that():
    print("do that") 

match input("Do this or do that? "):
    case 'this':
        do_this()
    case 'that':
        do_that()
    case _:
        print("Invalid input!")               