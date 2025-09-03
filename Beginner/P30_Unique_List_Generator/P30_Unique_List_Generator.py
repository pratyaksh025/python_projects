def unique_list(a):
    b = set()
    result = []

    for i in a:
        if i not in b:
            result.append(i)
            b.add(i)
    return result


print("Duplicate Remover")
items=input("Enter Values in []: ").strip("[").strip("]").strip("")
if not items:
    print("Nothing Was Inserted")
else:   
    uploaded = [int(item) if item.strip().isdigit() else item.strip() for item in items.split(",")]
    print(unique_list(uploaded))
