import random

def prisoner_list(prisoners_num):
    prisoner_list = list(range(1, prisoners_num + 1))
    random.shuffle(prisoner_list)
    return prisoner_list

print(prisoner_list(100))
