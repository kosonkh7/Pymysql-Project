#나이를 입력 받아 나이에 해당하는 티켓값을 출력하는 프로그램

age = int(input("입장객의 나이를 입력하시오: "))
while age > 0:
    price = 0

    if 0 < age <= 7:
        price = 0
    elif age <= 13:
        price = 4000
    elif age <= 19:
        price = 7000
    elif age <= 64:
        price = 10000
    else:
        price = 4000
    print("티켓값은 ", price, "원입니다.")
    age = int(input("입장객의 나이를 입력하시오: "))

print("프로그램 종료")