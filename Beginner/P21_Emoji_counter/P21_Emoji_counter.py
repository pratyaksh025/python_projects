import emoji
from collections import Counter

def count_emoji(text):
    emojis= [ch for ch in text if ch in emoji.EMOJI_DATA]
    return Counter(emojis)

text= input("Enter Text: ")

counts=count_emoji(text)

for emj,count in counts.items():
    print(f"{emj}: {count}")