import random

def generate_prisoner_num():
    
    prisoner_num_list = [random.randint(1, 100) for _ in range(100)]
    return prisoner_num_list

prisoner_num_list = generate_prisoner_num()
print(prisoner_num_list)
