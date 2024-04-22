import random

def generate_prisoner_num():
    
    prisoner_num_list = [random.randint(1, 100) for _ in range(100)]
    return prisoner_num_list

prisoner_num_list = generate_prisoner_num()
print(prisoner_num_list)

prisoner_pick = [random.randint(1, 100) for _ in range(50)]

print(prisoner_pick)

# 죄수 및 정답 순서

order = 0
answer = prisoner_num_list[order]
print(answer)

for try_num in range(50+1):
    selection = prisoner_pick[try_num]
    print(selection)

    if selection == answer:
        print('정답을 맞혔습니다. 다음 죄수로 넘어갑니다.')
        order += 1
        break






    


# for order in range(0, 99):

#     def choice_by_prisoner(i):
        
#         answer = prisoner_num_list[order]

#         if choose == answer:
#             order += 1