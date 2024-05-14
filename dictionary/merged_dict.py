def merge_dictionaries(d1: dict, d2: dict) -> dict:
    result = {}
    
    # Merge values from d1
    for key, value in d1.items():
        if key in d2 and d2[key] != value:
            # If key exists in both dictionaries and values are different, use a list for the value
            result[key] = [value, d2[key]]
        else:
            # Otherwise, just use the value from d1
            result[key] = value
    
    # Merge values from d2
    for key, value in d2.items():
        if key not in d1:
            # If key is only in d2 and not in d1, add the value directly
            result[key] = value
    
    return result

# Test the function
d1 = {"Temperature": "Celsius", "Wind": "South"}
d2 = {"Wind": "North"}

expected = {"Temperature": "Celsius", "Wind": ["South", "North"]}
output = merge_dictionaries(d1, d2)
assert output == expected

print(output)  # Output: {'Temperature': 'Celsius', 'Wind': ['South', 'North']}
