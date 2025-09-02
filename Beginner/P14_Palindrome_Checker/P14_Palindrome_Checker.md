# Palindrome Checker

A simple **command-line Palindrome Checker** built in **Python**.  
It checks whether a given **word or phrase** is a palindrome at both **word** and **character** levels.

---

## Features
- Checks **single words** for palindrome.  
- Checks **phrases** for palindrome at:
  - **Word level** (e.g., "step on no pets")  
  - **Character level** (ignores spaces and punctuation)  
- Handles **case-insensitive input**.  
- Ignores **punctuation** automatically.  

---

## Usage Example

```
Word or phrase: Madam
madam
'madam' is palindrome

Word or phrase: Step on no pets
step on no pets
'step on no pets' is a palindrome at word and character level

Word or phrase: Hello World
hello world
Neither a palindrome at word nor at character level


```
## How It Works

1. **Input Processing**:
   - Removes extra spaces.  
   - Removes punctuation.  
   - Converts input to lowercase for uniform checking.

2. **Palindrome Checking**:
   - **Single Word**: Checks if the word reads the same forwards and backwards.  
   - **Multiple Words (Phrase)**:
     - **Word-level**: Checks if the words in the phrase are the same when reversed.  
     - **Character-level**: Joins the words and checks if the resulting string reads the same forwards and backwards.

3. **Output**:
   - Prints if the input is palindrome at **word**, **character**, **both**, or **neither**.

---

## Author
Made with ❤️ by Pratyaksh Yadav
