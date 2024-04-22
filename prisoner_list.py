import random


def prisoner_trial(prisoners_num):
    prisoner_list = list(range(1,pisoners_num+1))
    random.shuffle(prisoner_list)

    for prisoner in range(prisoners_num):
        current_drawer=prisoner_list[prisoner]
        for attempt in range(50):
            if current_drawer == prisoner+1:
                break
            else:
                current_drawer = prisoner_list[current_drawer-1]
        else:
            return False
    return True



