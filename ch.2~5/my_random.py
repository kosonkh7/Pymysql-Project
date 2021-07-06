import random
score = 0
my_num = random.randint(1, 5)
your_num = int (input("1-5사이 정수 입력 : "))
if your_num == my_num :
    print("승리..")
    score += 1
else :
    print("패배")

#반복문 배우면 내용 수정 예정
