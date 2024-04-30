lst = [1,2,3,4,5,6]

print(lst)
print(*lst)  # unpacking the list


def order_pizza(size, *toppings, **details):
    print(f"Ordered a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    print("\n Details of the order are:")
    for key, value in details.items():
        print(f"- {key}: {value}")

order_pizza("large", "pepperoni", "sausage", "veggies", delivery=True, tip=5)