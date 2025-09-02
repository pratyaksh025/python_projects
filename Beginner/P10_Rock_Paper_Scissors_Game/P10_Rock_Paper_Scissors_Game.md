# Rock-Paper-Scissors Game

A simple **command-line Rock-Paper-Scissors game** built in **Python**.  
Play against the computer and see if you can win!

---

## Features
- Play up to **10 rounds** per session.  
- Choose either **Rock, Paper, or Scissors**.  
- Computer makes a **random choice** every round.  
- Keeps track of **score** for both player and computer.  
- Displays **final winner** or draw after all rounds.  
- Simple, interactive, and fun!

---

## Usage Example

``` 
Choose:
1 or Rock
2 or Paper
3 or Scissors

1
Computer chose: Paper
Computer Won

Choose:
1 or Rock
2 or Paper
3 or Scissors

Rock
Computer chose: Scissors
You Won
```

**Final Result Example:**
```
Final Result:
You Won The Game
```

**Draw Example:**
```
Final Result:
The Session Was a Draw!
```


## How It Works

### Choices
- User can input **1, 2, 3** or type **Rock, Paper, Scissors**.  
- Computer randomly selects one choice each round using **secrets.choice**.  

### Scoring Logic
- Rock beats Scissors  
- Paper beats Rock  
- Scissors beats Paper  
- If both choose the same, it’s a **Draw**.  

Scores are tracked through the session, and the **final winner** is announced at the end.

---

## Author
Made with ❤️ by Pratyaksh Yadav