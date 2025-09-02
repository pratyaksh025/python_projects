# Word, Character, and Sentence Counter

A simple **Python program** that counts the number of **words, characters, and sentences** in any given text.

---

## Features
- Counts **characters** (ignores spaces and punctuation).  
- Counts **words** (ignores extra spaces and punctuation).  
- Counts **sentences** (splits text by periods).  
- Handles multiple spaces and removes unnecessary punctuation automatically.  
- Easy-to-use command-line interface.

---

## Usage Example

```
Welcome to word,Sentences and character counter
Text: Hello world! This is a test.

Total Number of Characters : 21
Total Number of Words : 6
Total Number of Sentences : 2

Press return key to end this program
```


**Blank Input Example:**
```
Text:
Sorry That Was a blank input exiting program!!!
```
## How It Works

### `count_words(text)`
- Removes punctuation and extra spaces.  
- Splits the text into words.  
- Returns the total number of words.

### `count_char(text)`
- Removes punctuation and spaces.  
- Counts all remaining characters.  
- Returns the total number of characters.

### `count_sentences(text)`
- Cleans the text of extra punctuation and spaces.  
- Splits the text using periods (`.`) as sentence separators.  
- Returns the total number of sentences.

---

## Author
Made with ❤️ by Pratyaksh Yadav