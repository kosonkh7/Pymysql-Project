#23의 배수를 모두 출력하고 그 합과 개수도 출력하는 프로그램

i = 1
num = 0
sum = 0

for i in range(1, 10000):
    if i % 23 == 0:
        print(i)
        num += 1
        sum += i
print("합 : ", sum, "개수 : ", num)