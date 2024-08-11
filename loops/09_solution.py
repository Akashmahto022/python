items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("duplicate", item)
        break
    else:
        unique_item.add(item)
        print(item, "is not")