#이름과 성별을 입력 받아 출력하는 프로그램

name = ""
sex = ""

while True:
    name = input("이름 : ")
    sex = input("성별(M/F) : ")
    if sex == "M" or sex == "F":
        print("이름 : ", name, "성별 : ", sex)
    elif name == '.':
        break #이름에 .을 입력하면 반복문 종료
    else:
        print("성별을 정확하게 입력하세요")