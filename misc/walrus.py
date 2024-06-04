import time

def count_odds(data):
    time.sleep(1)
    odds = [o for o in data if o%2 == 1]
    return(len(odds))

# sample data
data = [45, 12, 89, 456, 9]

# start time
t1 = time.time()
'''
Below if condition will take atleast 2 seconds

Took 2.0004723072052 seconds
'''
# if count_odds(data) > 1:
#     print(f'{count_odds(data)} odds')   


'''
Below if condition with walrus operator will take 1 second
Took 1.0001862049102783 seconds
'''

if (n:=count_odds(data) > 1):
    print(f'{n} odds')

# end time
t2 = time.time()

print(f'Took {t2-t1} seconds')