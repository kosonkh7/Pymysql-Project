import pymysql
import random
import datetime

conn = 0
curs = 0

def db_connect():
    global conn, curs
    try:
        conn = pymysql.connect(host='SERVER_ADDRESS', user='USER_NAME', password='PASSWORD',
                               db='DB_NAME', charset='utf8')
    except:
        print("DB 연결을 실패했습니다.")
        return False
    print(conn)
    curs = conn.cursor(pymysql.cursors.DictCursor)
    return True

def db_close():
    curs.close()
    conn.close()

#회원가입 함수
def register_user():
    user_id = input("새 아이디를 입력하시오: ")
    user_phone = input("전화번호(010********)를 입력하시오: ")
    sql = f'insert into user (user_id, user_phone) values ("{user_id}", "{user_phone}")'
    curs.execute(sql)
    conn.commit()
    return True

#로그인 함수
def login():
    id = input("아이디를 입력해주세요. :")
    phone = input("핸드폰 번호를 입력해주세요. :")
    sql = f'select user_phone from user where user_id = "{id}"'
    curs.execute(sql)
    row = curs.fetchone()
    if row == None:
        print(" 등록되지 않은 아이디 입니다.")
        return False
    if row['user_phone'] == phone:
        return id
    else:
        print(" 비밀번호가 잘못 되었습니다.")
        return False

def center_lists():
    centers = [
        [2321, '학여울역 사거리'], [2420, '학여울역 사거리(LG베스트샵 앞)'], [2404, '대모산입구역 4번 출구'],
        [3624, "대모산입구역 7번 출구"], [2403, "공무원연금매점"], [2372, "대치역 사거리"],
        [2431, "대치역 7번 출구"], [2324, "천주교 대치 2동 교회 옆"], [2323, "주식회사 오뚜기 정문 앞"],
        [3621, "휘문고교 사거리"], [3614, "은마아파트 입구 사거리"], [3622, "은마아파트입구 사거리"],
        [2325, "대치동 버거킹대치점"], [2373, "개포동역 사거리"], [2342, "대청역 1번출구 뒤"],
        [2320, "도곡역 대치지구대 방향"], [2413, "도곡역 1번 출구"], [2370, "한티역 3번출구"],
        [2322, "삼성역 3번 출구"], [3603, "삼성역 2번 출구"]
    ]
    return centers

def rental_center():
    for rc_id, rc_name in center_lists() :
        sql = f'insert into rental_center (rc_id,rc_name, rc_cycle) values \
        ("{rc_id}","{rc_name}","{random.randint(1,5)}")'
        curs.execute(sql)
    conn.commit()

def rental_func(id):
    if isRent(id):
        time, num = rental()
        sql = f'insert into rental_information (user_id,rental_time, rent_place_id) values \
                ("{id}","{time}","{num}")'
        curs.execute(sql)
        conn.commit()
    else:
        print("이전 사용의 반납 이후 이용해주십시오.")

def isRent(id):
    sql = f'select rental_time, return_time from rental_information where user_id = "{id}"'
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows :
        if row["return_time"] == None:
            return False
    return True

def rental():
    isName = False
    centers = center_lists()
    for lists in centers:
        print(f"{lists[0]} : {lists[1]}")
    num = int(input("위 대여소 중 하나를 고르시오.(숫자)]\n"))
    for lists in centers:
        if num in lists:
            isName = True
            sql = f"select a.rc_name , a.rc_cycle from rental_center a where a.rc_id = '{num}'"
            curs.execute(sql)
            row = curs.fetchone()
            rc_name = row['rc_name']
            cy_num = row['rc_cycle']
            print(f"대여소 : {rc_name}, 자전거 수 : {cy_num}")
            if cy_num >0:
                rent = input("이 대여소에서 빌리시겠습니까 ? (Y/N)\n")
                if rent == 'Y':
                    sql = f'update rental_center set rc_cycle = "{cy_num-1}" where rc_id = "{num}"'
                    curs.execute(sql)
                    conn.commit()
                    print("대여가 완료되었습니다.")
                    return datetime.datetime.now(), num
                elif rent == "N" :
                    return rental()
            else:
                print("남은 자전거가 없습니다. 다른 대여소를 이용해주십시오.")
                return rental()
    if not isName:
        print("올바른 숫자을 입력해주십시오. ")
        return False

def return_func(id):
    if not isRent(id):
        time, num = func_return()
        sql = f'update rental_information set return_time = "{time}",return_place_id = "{num}" \
              WHERE user_id = "{id}" AND return_time IS NULL'
        curs.execute(sql)
        conn.commit()
        print("반납이 완료되었습니다.")

def func_return():
    isName = False
    centers = center_lists()
    for lists in centers:
        print(f"{lists[0]} : {lists[1]}")
    num = int(input("반납할 대여소를 고르시오.(숫자)\n"))
    for lists in centers :
        if num in lists :
            isName = True
            sql = f"select a.rc_cycle from rental_center a where a.rc_id = '{num}'"
            curs.execute(sql)
            row = curs.fetchone()
            cy_num = row['rc_cycle']
            sql = f'update rental_center set rc_cycle = "{cy_num+1}" where rc_id = "{num}"'
            curs.execute(sql)
            conn.commit()
            return datetime.datetime.now(), num
    if not isName:
        print("올바른 숫자을 입력해주십시오. ")
        return func_return()

#자전거 추가 배치 요청 함수 (입력한 숫자만큼 자전거 +)
def request_cycle():
    isName = False
    centers = center_lists()
    for lists in centers:
        print(f"{lists[0]} : {lists[1]}")
    num = int(input("자전거 추가 배치를 요청할 대여소를 고르시오(숫자)]\n"))
    for lists in centers:
        if num in lists:
            isName = True
            sql = f"select a.rc_name , a.rc_cycle from rental_center a where a.rc_id = '{num}'"
            curs.execute(sql)
            row = curs.fetchone()
            rc_name = row['rc_name']
            cy_num = row['rc_cycle']
            print(f"대여소 : {rc_name}, 자전거 수 : {cy_num}")
            rent = input("이 대여소에 추가 요청하시겠습니까? (Y/N)\n")
            if rent == 'Y':
                request_num = int(input("요청하실 자전거 개수를 입력하시오 : "))
                sql = f'update rental_center set rc_cycle = "{cy_num+request_num}" where rc_id = "{num}"'
                curs.execute(sql)
                conn.commit()
                print("자전거 추가 배치가 완료되었습니다.")
            elif rent == "N" :
                print("요청이 취소되었습니다.")
    if not isName:
        print("올바른 숫자을 입력해주십시오. ")
        return False


#자전거 고장 신고함수 (-1)
def report_cycle():
    isName = False
    centers = center_lists()
    for lists in centers:
        print(f"{lists[0]} : {lists[1]}")
    num = int(input("고장난 자전거가 위치한 대여소를 고르시오(숫자)]\n"))
    for lists in centers:
        if num in lists:
            isName = True
            sql = f"select a.rc_name , a.rc_cycle from rental_center a where a.rc_id = '{num}'"
            curs.execute(sql)
            row = curs.fetchone()
            rc_name = row['rc_name']
            cy_num = row['rc_cycle']
            print(f"대여소 : {rc_name}, 자전거 수 : {cy_num}")
            rent = input("이 대여소에 신고 요청하시겠습니까? (Y/N)\n")
            if rent == 'Y':
                sql = f'update rental_center set rc_cycle = "{cy_num - 1}" where rc_id = "{num}"'
                curs.execute(sql)
                conn.commit()
                print("고장 신고가 성공적으로 접수되었습니다.")
            elif rent == "N":
                print("요청이 취소되었습니다.")
    if not isName:
        print("올바른 숫자을 입력해주십시오. ")
        return False

def user_information(id):
    sql = f'select use_time from user where user_id = "{id}"'
    curs.execute(sql)
    row = curs.fetchone()
    total_time = row['use_time']
    second = int(total_time.total_seconds())
    print(f'"{id}"님의 총 사용량은 {total_time}')
    print(f'총 이동거리는 {second*5}m')
    print(f'총 칼로리 소모는 {second*0.133}kcal')
    print(f'총 탄소 절감량은 {second*0.83}g')

if __name__ == '__main__':
    db_connect()
    #rental()
    #print(func_return())
    #rental_center()
    isRent("김원혁")
