import random

def generate_prisoner_num():
    
    prisoner_num_list = [random.randint(1, 100) for _ in range(100)]
    return prisoner_num_list

prisoner_num_list = generate_prisoner_num()
print(prisoner_num_list)

prisoner_pick = [random.randint(1, 100) for _ in range(50)]

print(prisoner_pick)

# 죄수 및 정답 순서

def simulation_pick(answer, prisoner_pick):
    for selection in prisoner_pick:
        if selection == answer:
            return True
    return False

def calculate_success_probability(n):
    success_count = 0
    for _ in range(n):
        prisoner_num_list = generate_prisoner_num()
        prisoner_pick = [random.randint(1, 100) for _ in range(50)]
        success = True
        for answer in prisoner_num_list:
            if not simulation_pick(answer, prisoner_pick):
                success = False
                break
        if success:
            success_count += 1
    success_probability = success_count / n * 100
    return success_probability

n = int(input('몇 회 시도하시겠습니까?: '))
success_probability = calculate_success_probability(n)
print(f"{n}회 시도 후 성공 확률은 {success_probability:.2f}%입니다.")




# for order in range(0, 99):

#     def choice_by_prisoner(i):
        
#         answer = prisoner_num_list[order]

#         if choose == answer:
#             order += 1