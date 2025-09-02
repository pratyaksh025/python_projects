# Console-Based Phone Book

A simple **command-line Phone Book** built in **Python**.  
Easily manage your contacts with add, edit, view, and delete options.

---

## Features
- Add new contacts with **Name, Email, and Phone Number**.  
- Edit existing contacts:
  - Change **Name**, **Email**, or **Phone Number**.  
- View all saved contacts with total count.  
- Delete a contact by name.  
- Input validations for:
  - Email format  
  - 10-digit phone numbers  

---

## Usage Example

```
Console Based Phone-Book

Press:1 to add contact
Press:2 To edit contact
Press:3 To view contact
Press:4 To delete contact
Press:Enter to close phone-book

Enter Name: Pratyaksh Yadav
Enter Email: pratyaksh@example.com

Enter Phone_number: 9876543210

Pratyaksh Yadav Added to contacts successfully

Press:3 To view contact

1- John Doe, pratyaksh@example.com
, 9876543210

Total 1 contacts displayed
```


**Editing a Contact Example:**
```
Enter Name to Edit: Pratyaksh Yadav

Name: Pratyaksh Yadav
Phone_number: 9876543210
Email: Pratyaksh@example.com

Press:1 to change name
Press:2 to change email
Press:3 to change phone_number
Press:Enter to go back to menu

New Mail: Pratyaksh.Yadav@example.com

Changes Saved
```

**Deleting a Contact Example:**

```
Enter Name to Delete Contact: Pratyaksh Yadav

Contact with name 'Pratyaksh Yadav' deleted successfully
```


## How It Works

### Adding a Contact
- User enters **Name, Email, and Phone Number**.  
- Checks if the contact **already exists**.  
- Adds new contact to the **phone dictionary**.

### Editing a Contact
- User can choose to edit **Name, Email, or Phone Number**.  
- Input validation ensures **valid email** and **10-digit phone numbers**.

### Viewing Contacts
- Displays all saved contacts in a **numbered list**.  
- Shows **total number of contacts**.

### Deleting a Contact
- Deletes the contact by **name**.  
- Provides feedback if the contact is not found.

---

## Author
Made with ❤️ by Pratyaksh Yadav