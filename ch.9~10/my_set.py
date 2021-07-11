login_ID = {'kokhyeh', 'hm_son7', 'yj.04.23'}

def register_loginID():
    id = input('아이디 입력: ')
    if id in login_ID:
        print(f'{id}는 이미 사용중인 ID입니다.')
    else:
        print(f'{id} ID가 정상적으로 등록되었습니다.')
        login_ID.add(id)
    print(login_ID)

register_loginID()