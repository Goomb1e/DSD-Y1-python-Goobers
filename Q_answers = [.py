Q_answers = [
{
    "Question":"How many teeth does an Aardvark have?",
    "Answer":"None"

},
{
    "Question":"What is the snake called in rango?",
    "Answer":"Rattlesnake jake"
},
{
    "Question":"What the theme of the current fortnite season?",
    "Answer":"Simpsons"
},
{
    "Question":"What species is a Hellbender?",
    "Answer":"Salamander"
}
]
for qa in Q_answers:
    user_input = input(qa["Question"]+" ").strip()
    if user_input.lower() == qa["Answer"].lower():
        print("Correct")
    else:
        print("Incorrect")