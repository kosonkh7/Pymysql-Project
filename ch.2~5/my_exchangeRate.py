con = input("미국, 중국, 일본, 유럽 중 하나를 선택: ")
money = float(input("환전할 금액(원)을 입력하시오: "))
#2021년 7월 6일 환율 기준

if con == "미국":
    money = money/1130.4
    print("환전하면 ", round(money, 2), "달러입니다.")

elif con == "일본":
    money = money/10.199
    print("환전하면 ", round(money, 2), "엔화입니다.")

elif con == "중국":
    money = money/174.95
    print("환전하면 ", round(money, 2), "위안입니다.")

elif con == "유럽":
    money = money/1344.14
    print("환전하면 ", round(money, 2), "유로입니다.")

else:
    print("유효하지 않은 국가명입니다.")
