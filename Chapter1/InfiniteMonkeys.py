'''Here’s a self check that really covers everything so far. You may have heard of the infinite monkey theorem?
The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text,
such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function.
How long do you think it would take for a Python function to generate just one sentence of Shakespeare?
The sentence we’ll shoot for is: “methinks it is like a weasel”

You’re not going to want to run this one in the browser, so fire up your favorite Python IDE.
The way we’ll simulate this is to write a function that generates a string that is 28 characters long by choosing random letters from the 26 letters in the alphabet
plus the space. We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.

A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done.
If the letters are not correct then we will generate a whole new string.
To make it easier to follow your program’s progress this third function should print out the best string generated so far and its score every 1000 tries.'''

import string
import random
sentence = 'methinks it is like a weasel'

def generate_string():
    alphabet = list(string.ascii_lowercase + " ")
    gen_string = ''.join(random.choice(alphabet) for i in range(28))
    return gen_string
#use zip function to iterate over both simul
def score_output(string):
    goal = sentence
    score = sum(a==b for a,b in zip(string,goal))
    return score

def execute():
    best_score = 0
    attempt_counter=0
    best_string=str()
    while best_score != 28:
        string = generate_string()
        score=score_output(string)
        attempt_counter += 1
        if score > best_score:
            best_score=score
            best_string=string

        if attempt_counter%1000==0:
            print('Attempt #: ',attempt_counter,' Best String: ',best_string,' Best Score: ', best_score)
    return('Generated the sentence in, ', attempt_counter, ' attempts')

execute()


