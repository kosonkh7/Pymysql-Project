# 1) 랜덤 넘버(1~100)를 추출하여 10회안에 맞추는 게임
# 2) 3회 안에 맞추면 점수 1 증가
# 3) 맞추지 못한 경우 힌트 제공 (‘up’, ‘down’)
# 3) 게임이 끝나면 계속할지 여부를 묻고
# ‘y’를 입력하는 경우 게임 반복,
# ‘n’를 입력하는 경우 점수 출력 후 종료

import random
ran_num = random.randint(1, 100)
score = 0
retry: ""
i = 1

while i <= 10 :
    my_num = int(input("숫자를 입력하세요 : "))
    if i <= 3:
        if ran_num == my_num:
            score += 1
            print("3회 안에 맞추셨습니다.")
            break

    if ran_num != my_num:
        if ran_num > my_num:
            print("Hint : Up")
        else:
            print("Hint : Down")

    if ran_num == my_num:
        print("정답입니다.")
        break

    if i == 10:
        retry = input("(y,n) : ")
        if retry == "y":
            i = 1
        if retry == "n":
            break
    i+=1

print("획득 점수 : ", score)




