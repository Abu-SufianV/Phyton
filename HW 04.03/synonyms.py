SYNONYMS = dict()


def add(new_1, new_2):
    if new_1 not in SYNONYMS.keys():
        SYNONYMS[new_1] = set()
    if new_2 not in SYNONYMS.keys():
        SYNONYMS[new_2] = set()
    SYNONYMS[new_1].add(new_2)
    SYNONYMS[new_2].add(new_1)


def count(word):
    if word in SYNONYMS.keys():
        print(len(SYNONYMS[word]))
    else:
        print(0)


def check(new_1, new_2):
    if new_1 in SYNONYMS[new_2]:
        print('Yes')
    else:
        print('No')


AMOUNT = int(input('Enter number of lines: '))

while AMOUNT > 0:
    COMMAND = str(input())
    COMMAND = COMMAND.lower()
    COMMAND = COMMAND.split()
    if COMMAND[0] == "add":
        add(COMMAND[1], COMMAND[2])
    elif COMMAND[0] == "count":
        count(COMMAND[1])
    elif COMMAND[0] == "check":
        check(COMMAND[1], COMMAND[2])
    else:
        print("Error")
    AMOUNT -= 1
