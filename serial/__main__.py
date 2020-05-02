import json
import random

def main():

    questions = [generate_ques() for i in range(5)]
    to_save = {"multiple_choice": questions}
    print(json.dumps(to_save))

    with open('output.txt', 'w') as outfile:
        json.dump(to_save, outfile)




#Generate 1 question
def generate_ques():
    n = random.randint(1, 10)
    answer = str(round((1/n)*100)) + '%'
    
    hint = "1/SerialFraction"

    prompt = "<b>If the max speedup with ∞ cores is " + str(n) + "x, what percentage of code is serial?"

    choices = ["100%", "50%", "33%", "25%", "20%", "17%", "14%", "11%", "10%"]
    
    ans_index = 0
    for i in range(9):
        if choices[i] == answer:
            ans_index = i

    print(answer)

    return {"prompt":prompt, "choices":choices, "answers":ans_index, "hint": hint}



if __name__ == "__main__":
    main()
