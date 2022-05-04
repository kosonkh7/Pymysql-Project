import db_function as df


while(True):
    print('1. 회원가입\n2. 로그인\n3. 프로그램 종료')
    action = int(input('실행할 메뉴 번호 입력 : '))
    if action >= 1 and action <= 3:
        pass
    else:
        print(' 1 ~ 2 사이의 번호를 입력해주세요. ')

    if action == 1:
        df.register_user()

    elif action == 2:
        login_id = input("아이디를 입력하세요 : ")
        login_phone = input("전화번호(010********)를 입력하세요 : ")
        if df.login(login_id,login_phone) == False:
            continue
        else:
            while (True):
                print('1. 자전거 대여\n2. 자전거 반납\n3. 자전거 추가 배치 요청\n4. 자전거 고장 신고\n5. 회원 정보 조회\n6. 로그아웃')
                action = int(input('실행할 메뉴 번호 입력 : '))
                if action >= 1 and action <= 6:
                    pass
                else:
                    print(' 1 ~ 6 사이의 번호를 입력해주세요. ')
                if action == 1:
                    print("")

                elif action == 2:
                    print("")

                elif action == 3:
                    print("")

                elif action == 4:
                    print("")

                elif action == 5:
                    print("")

                elif action == 6:
                    print("로그아웃 되었습니다.")
                    break

    elif action == 3:
        print("프로그램이 종료되었습니다.")
        break
