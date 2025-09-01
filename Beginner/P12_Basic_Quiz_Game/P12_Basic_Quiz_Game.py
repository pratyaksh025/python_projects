import secrets
import random


questions={
    "Q- What is the capital of India?":[["Delhi","Mumbai","Kashmir","Uttar Pradesh"],["Delhi"]],
    "Q- Who is the Prime Minister of India":[["Narendra Modi","Rahul Gandhi","Akhilesh Yadav","Draupadi Murmun"],["Narendra Modi"]]
}
lis_of_q=[]
for q in questions.keys():
    lis_of_q.append(q)
points=0
qno=1
ans_dic={}
print("Welcome to quiz")
while True:
    
    ques= secrets.choice(lis_of_q)

    print(f"{"-"*len(ques)}\n{ques}\n")
    values=questions[ques][0]
    random.shuffle(values)
    for index,option in enumerate(values):
        print(f"{index+1}-{option}\n",end="")
        ans_dic[index+1]=[option]

    print(f"{"-"*len(ques)}")
    user_choice= input("Your answer: ")
    print()
    if len(user_choice)>1:
        print("Answer Correctly with number")
    else:
        # print(ans_dic)
        user_ans=ans_dic[int(user_choice)]
        if user_ans == questions[ques][1]:
            print("Correct answer")
            points+=1
            
        
        else:
            print(f"Wrong Answer Game Over\nTotal Points:{points}")
            break

    lis_of_q.remove(ques)
    if not lis_of_q:
        print(f"Congratulations game is finished you answered all questions \ntotal points: {points}")
        break
    



