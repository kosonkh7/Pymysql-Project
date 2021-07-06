#3개의 수를 입력 받아 가장 큰 값을 찾아 출력하는 프로그램
#단, 세 수는 모두 다르게 입력

num1 = int(input("첫 번째 수 입력 : "))
num2 = int(input("두 번째 수 입력 : "))
num3 = int(input("세 번째 수 입력 : "))

if num1 > num2 and num1 > num3:
    print(num1)
if num2 > num1 and num2 > num3:
    print(num2)
if num3 > num2 and num3 > num1:
    print(num3)
