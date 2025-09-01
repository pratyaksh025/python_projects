import string
import re

punc= string.punctuation.replace(".","").replace(",","")

def count_words(text):
    clean_list = re.sub(f"[{re.escape(punc)}]","",text)
    space_removed = re.sub(r"\s{2,}"," ",clean_list)
    word_list = [word for word in space_removed.split(" ") if word not in punc and word!="." and word != ","]
    return len(word_list)

def count_char(text):
    clean_list = re.sub(f"[{re.escape(punc)}]","",text)
    space_removed = re.sub(r"\s{2,}"," ",clean_list)
    char_list = [char for char in space_removed if char!=" " and char not in punc and char!="." and char != ","]
    return len(char_list)

def count_sentences(text):
    clean_list = re.sub(f"[{re.escape(punc)}]","",text)
    space_removed = re.sub(r"\s{2,}"," ",clean_list)
    sen_list =[sen for sen in space_removed.split('.')]
    return len(sen_list)



def main():
    print("Welcome to word,Sentences and character counter")

    while True:
        user_text= input("Text: ")

        if user_text:
            print(f"Total Number of Characters : {count_char(user_text)} ")
            print(f"Total Number of Words : {count_words(user_text)} ")
            print(f"Total Number of Sentences : {count_sentences(user_text)} ")
            print(f"\nPress return key to end this program")
        
        else: 
            print("Sorry That Was a blank input exiting program!!!")
            break

if __name__ == "__main__":
    main()