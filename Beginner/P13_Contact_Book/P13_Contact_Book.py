import re
class phone():
    global phone_dict
    phone_dict ={}
    def __init__(self) -> None:
        self.main()

    def add_contact(self,name,email,phone_number):
        phone_dict[name]=[email,phone_number]
    
    def edit_contact(self,name=None):
        if name!= None:
            details=phone_dict.get(name)
            if not details:
                print(f"\nCannot find contact with name '{name}'\n")
            else:
                email,phone_number=details
                print(f"\nName: {name}\nPhone_number: {phone_number}\nEmail: {email}\n")
                to_edit=input("Press:1 to change name\nPress:2 to change email\nPress:3 to change phone_number\nPress:Enter to go back to menu\n")
                if to_edit=="1":
                    new_name=input("New Name: ")
                    del(phone_dict[name])       
                    phone_dict[new_name]=[email,phone_number]
                    print(f"\nChanges saved for {new_name}\n")
                elif to_edit == "2":
                    if (new_mail:=input("New Mail: ")) and (re.match(r"^[a-zA-Z0-9._%+-]{5,}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",new_mail)):
                        phone_dict[name]=[new_mail,phone_number]
                        print("\nChanges Saved\n")
                    else:
                        print("\nInvalid Email\n")
                elif to_edit == "3":
                    if (new_phone:= input("New Phone: ")) and (re.match(r"^[0-9]{10}$",new_phone)):
                        phone_dict[name]= [email,new_phone]
                        print("\nChanges Saved\n")
                    else:
                        print("\nInvalid number\n")
                elif to_edit == "":
                    print("\nNo changes applied\n")
                else:
                    print("\nInvalid Choice\n")

    def view_contacts(self):
        names=phone_dict.keys()
        if not names:
            print("\nSorry Currently Phone book is empty try adding some\n")
            return [],[],[],[],0
        else:
            indexes=[]
            names_str=[]
            email=[]
            phone_number=[]
            for index, name in enumerate(names):
                indexes.append(index+1)
                names_str.append(name)
                email.append(phone_dict[name][0])
                phone_number.append(phone_dict[name][1])
            count=len(names_str)
            return indexes,names_str,email,phone_number,count

    def delete(self,name):
        if name in phone_dict:
            del(phone_dict[name])
            print(f"\nContact with name '{name}' deleted successfully\n")
        else:
            print(f"\nNo contact with name '{name}' please retry\n")
        
    def main(self):
        print("\nConsole Based Phone-Book\n")
        while True:
            choice=input("""Press:1 to add contact
Press:2 To edit contact
Press:3 To view contact
Press:4 To delete contact
Press:Enter to close phone-book
""")
            if choice =="":
                print("\nThank You for using Pratyaksh's phone-book\n")
                break
            elif choice == "1":
                phone_list=[]
                name=input("\nEnter Name: ")
                email=input("Enter Email: ")
                phone=input("Enter Phone_number: ")
                temp_val=phone_dict.get(name)
                if temp_val:
                    print(f"\nContact with {name} already exists\n")
                    data=self.view_contacts()
                    _,_,_,phone_number,_=data
                    if phone in phone_number:
                        print("\nNumber Already Exists\n")
                else:
                    self.add_contact(name,email,phone)
                    print(f"\n{name} Added to contacts successfully\n")
            elif choice =="2":
                name=input("\nEnter Name to Edit: ")
                self.edit_contact(name)
            elif choice == "3":
                index,names,emails,phones,count=self.view_contacts()
                if not index :
                    print("\nNo Contacts to Display\n")
                else:
                    print()
                    for i,n,e,p in zip(index,names,emails,phones):
                        print(f"{i}- {n}, {e}, {p}") 
                    print(f"\nTotal {count} contacts displayed\n")
            elif choice == "4":
                name=input("\nEnter Name to Delete Contact: ")
                self.delete(name)

obj=phone()
