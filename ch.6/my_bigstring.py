bigstring = ""

inputString = input("문자열을 입력하세요 : ")
while inputString != "...":
    bigstring += inputString
    inputString = input("문자열을 입력하세요 : ")

print("결과 문자열은 ", bigstring, "이고, 문자열 길이는 ", len(bigstring), "이다.")
