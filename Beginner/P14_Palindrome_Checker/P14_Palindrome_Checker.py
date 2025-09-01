import re
user_input=re.sub(r"\s{2,}"," " ,input("Word or phrase: "))
user_input = re.sub(r"[^a-zA-Z0-9 ]", "", user_input)
user_input= user_input.lower()
print(user_input)
if user_input:

    phrase=[word for word in user_input.split(" ") ]
    if len(phrase)>1:
        joined="".join(phrase)

        if phrase == list(reversed(phrase)) and joined == joined[::-1]:
            print(f"'{' '.join(phrase)}' is a palindrome at word and character level")
        
        elif phrase == list(reversed(phrase)):
            print(f"'{' '.join(phrase)}' is palindrome at word level only")
        
        elif joined == joined[::-1]:
            print(f"'{' '.join(phrase)}' is palindrome at Character level only")
            
        else:
            print("Neither a palindrome at word nor at character level")
    else:
        word=phrase[0]
        if word == word[::-1]:
            print(f"'{word}' is palindrome")

        else:
            print("Not a palindrome")
