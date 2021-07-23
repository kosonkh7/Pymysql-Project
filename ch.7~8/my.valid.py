#함수와 조건문을 이용한 간단한 유효성 검사

def check_id(myid):
    if len(myid) != 14:
        return False
    if myid[6] != '-':
        return False
    return True

jid = input("id : ")
if check_id(jid) == True:
    print("확인되었습니다.")
else:
    print("잘못된 주민등록번호입니다.")

def check_phone(myphone):
    if len(myphone) != 13:
        return ""
    elif myphone[3] != '-' or myphone[8] !='-':
        return ""
    else:
        return myphone.replace('-', '')

jphone = input("전화번호: ")
if check_phone(jphone) == "":
    print("사용 불가능한 전화번호입니다.")
else:
    print("사용 가능한 전화번호 입니다. (", check_phone(jphone), ")")
