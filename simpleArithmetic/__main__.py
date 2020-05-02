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
    hex_in_dec = random.randint(10, 16)
    binary_in_dec = random.randint(1, 8)
    
    hint: "..."

    hex = "{0:x}".format(hex_in_dec)
    binary = "{0:b}".format(binary_in_dec)

    operation = random.choice([0, 1, 2, 3])
    if operation == 0:
        answer = hex_in_dec + binary_in_dec
        sign = "+"
    elif operation == 1:
        answer = hex_in_dec - binary_in_dec
        sign = "-"
    elif operation == 2:
        answer = hex_in_dec * binary_in_dec
        sign = "x"
    else:
        answer = hex_in_dec // binary_in_dec
        sign = "÷"

    prompt = "<b>What is " + str(hex) + "<sub>16<sub> " + str(sign) + " " + str(binary) + "<sub>2<sub> ?<b>"

    choices = []
    position = random.randint(0, 9)
    ans_index = 0
    for i in range(10):
        c_text = str(answer + position) + "<sub>10<sub>"
        if answer + position == answer:
            ans_index = i
        choices.append(c_text)
        position -= 1

    return {"prompt":prompt, "choices":choices, "answers":ans_index, "hint": hint}



if __name__ == "__main__":
    main()
