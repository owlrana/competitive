# creating a multiple choice quiz in python

# class available in MCQclass.py
from MCQclass import Question

# list of all my questions prompt
question_prompts = [
    "What colour are apples?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
    "What colour are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What colour are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

Questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(Questions):
    score = 0
    for question in Questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(Questions)) + " correct")
 
run_test(Questions)