# Python Quiz Game

A simple **command-line Quiz Game** built in **Python**.  
Test your general knowledge and see how many questions you can answer correctly!

---

## Features
- Randomly selects questions from a pre-defined list.  
- Multiple choice answers are **shuffled** each time.  
- Input answers using the **number of the option**.  
- Keeps track of your **points** for correct answers.  
- Ends the game if you answer incorrectly.  
- Congratulates you if all questions are answered correctly.  

---

## Usage Example

```
Welcome to quiz

Q- What is the capital of India?

1- Mumbai
2- Delhi
3- Uttar Pradesh
4- Kashmir

Your answer: 2
Correct answer

Q- Who is the Prime Minister of India?

1- Draupadi Murmu
2- Akhilesh Yadav
3- Narendra Modi
4- Rahul Gandhi

Your answer: 3
Correct answer

Congratulations game is finished you answered all questions
total points: 2
```


**Wrong Answer Example:**
```
Your answer: 1
Wrong Answer Game Over
Total Points: 1
```


## How It Works

### Questions & Options
- Questions are stored in a dictionary with **options and correct answer**.  
- Each round, a question is randomly selected using `secrets.choice`.  
- The answer options are **shuffled** randomly so the correct answer is not always in the same position.

### User Input
- Players answer by typing the **number corresponding to their choice**.  
- The game checks if the selected option matches the correct answer.  

### Scoring
- **Points are incremented** for each correct answer.  
- The game ends immediately on a **wrong answer**.  
- If all questions are answered correctly, the game **congratulates the player**.

---

## Author
Made with ❤️ by Pratyaksh Yadav


