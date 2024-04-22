import random


def prisoner_trial(prisoners_num):
    prisoner_list = list(range(1,prisoners_num+1))
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

def calculate_probability(prisoners_num, num_trials):
    success_count = 0

    for _ in range(num_trials):
        if prisoner_trial(prisoners_num):
            success_count += 1

    success_probability = success_count / num_trials
    return success_probability

num_trials = 1000
prisoners_num = 100

print(num_trials, "회 시행 시 성공확륙은: ", calculate_probability(prisoners_num, num_trials))

