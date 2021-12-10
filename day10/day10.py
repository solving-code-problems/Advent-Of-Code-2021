
def syntax_scoring_p1():

    closing_pair = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }

    score = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    illegal_characters = []
    with open('input', 'r') as  f:
        lines = [x.strip() for x in f.readlines()]
        for line in lines:

            stack = []
            for char in line:
                if char in ["(","{","<","["]:
                    stack.append(char)
                else:
                    last_opening = stack.pop()
                    if closing_pair[char] != last_opening:
                        illegal_characters.append(char)
                        break

    sum = 0
    for char in illegal_characters:
        sum += score[char]
    return sum

def syntax_scoring_p2():

    closing_pair = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }

    opening_pair = {
       "(":  ")" ,
       "[":  "]" ,
       "{":  "}" ,
       "<":  ">"
    }

    score = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    uncompleted_chars = []
    with open('input', 'r') as  f:
        lines = [x.strip() for x in f.readlines()]
        for line in lines:

            stack = []
            legal = True
            for char in line:
                if char in ["(","{","<","["]:
                    stack.append(char)
                else:
                    last_opening = stack.pop()
                    if closing_pair[char] != last_opening:
                        legal = False
                        break
            if legal:
                if len(stack) > 0:
                    uncompleted_chars.append(stack)

    scores = []
    for chars in uncompleted_chars:
        sum = 0
        processed = list(reversed([opening_pair[c] for c in chars]))
        for c in processed:
            sum *=5
            sum += score[c]
        scores.append(sum)
    scores = sorted(scores)
    return scores[len(scores)//2]



print(f'Part one: {syntax_scoring_p1()}')
print(f'Part two: {syntax_scoring_p2()}')