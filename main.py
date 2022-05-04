import project_function as pf

conn = 0
curs = 0

def first_page():
    print('1. 회원가입\n2. 로그인\n3. 프로그램 종료')
    action = int(input('실행할 메뉴 번호 입력 : '))
    if action >= 1 and action <= 3:
        pass
    else:
        print(' 1 ~ 2 사이의 번호를 입력해주세요. ')
    return action

def after_login(id):
    print('1. 자전거 대여\n2. 자전거 반납\n3. 자전거 추가 배치 요청\n4. 자전거 고장 신고\n5. 회원 정보 조회\n6. 로그아웃')
    action = int(input('실행할 메뉴 번호 입력 : '))
    if action >= 1 and action <= 6:
        pass
    else:
        print(' 1 ~ 6 사이의 번호를 입력해주세요. ')
    if action == 1:
        pf.rental_func(id)
    elif action == 2:
        pf.return_func(id)
    elif action == 3:
        pf.request_cycle()
    elif action == 4:
        pf.report_cycle()
    elif action == 5:
        pf.user_information(id)
    elif action == 6:
        print("로그아웃 되었습니다.")
        return
    if action != 6:
        after_login(id)

while (True):
    pf.db_connect()
    action = first_page()
    if action == 1:
         pf.register_user()
         isLog = input("회원가입이 완료되었습니다. 로그인하시겠습니까? : (Y/N)")
         if isLog == "Y":
             id = pf.login()
             if id:
                 after_login(id)
    elif action == 2:
        id = pf.login()
        if id:
            after_login(id)
    elif action == 3:
        print("프로그램이 종료되었습니다.")
        break
