import time

def tictoc(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()-start
        print(f"{func.__name__} ran in "\
              f"{end} seconds")
    return wrapper

@tictoc
def do_this():
    time.sleep(1.3)


@tictoc
def do_that():
    time.sleep(.4)

do_this()
do_that()
print("Done")    