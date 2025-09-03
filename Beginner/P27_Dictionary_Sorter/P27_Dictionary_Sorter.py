
my_dict = {}

while True:
    items=input("Enter Key: Value - ").strip()
    if not items:
        break
    else:
        key,value=items.split(":")
        my_dict[key.capitalize()]=int(value)

print("\n")
for key,value in my_dict.items():
    print(f"{key}: {value}")



choice = input("Sort by (key/value): ").strip().lower()

if choice == "key":
    choice_r=input("Enter to continue R to reverse: ").strip().lower()
    if choice_r!='r':
        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[0]))
    else:
        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[0],reverse=True))
        
elif choice == "value":
    choice_r=input("Enter to continue R to reverse: ").strip().lower()
    if choice_r!='r':
        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
    else:
        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1],reverse=True))
else:
    print("Invalid choice!")
    sorted_dict = my_dict

print("Sorted Dictionary:")
print(sorted_dict)
