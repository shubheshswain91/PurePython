'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190

Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

expenses = [2200, 2350, 2600, 2130, 2190]
month_dict = {
    0: "Jan",
    1: "Feb",
    2: "Mar",
    3: "Apr",
    4: "May",
    5: "Jun",
}

extra_spent_in_feb = expenses[1] - expenses[0]

print(extra_spent_in_feb)

quarter_1_total_expenses = expenses[0] + expenses[1] + expenses[2]

print(quarter_1_total_expenses)
# print(len(expenses))
def if_spent_2000(num):
    for i in range(len(expenses)):
        if num == expenses[i]:
            print("Yes in the month: ", month_dict[i])
            break
        else:
            print("No")
            continue
            
        
input_num = int(input("Enter the number: "))

#print(if_spent_2000(input_num))        
if_spent_2000(input_num)

expenses.append(1980)
print(expenses)

expenses[3] = expenses[3] - 200

print(expenses)
