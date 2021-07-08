#정수를 반복하여 입력 받아 가장 큰 값을 찾아 출력하는 프로그램
#단, 0을 입력하면 프로그램 종료
num = int(input("첫 번째 수 입력 : "))
maxnum = num

while num != 0:
    if num > maxnum:
        maxnum = num
    num = int(input("다음 수 입력 : "))

print("가장 큰 수 값은 ", maxnum, "이다")