# Pymysql-Project
Mini project using pymysql package &amp; Collection of example files used in Python class in Web Development DT Schools<br>
<br>
따릉이를 모티브로 한 <b>공용 자전거 대여 어플리케이션</b>을 구현해보았습니다.<br>
<br>
<h2>메인 화면</h2><br>
파일 실행하면 

1. 회원가입 
2. 로그인 
3. 프로그램 종료<br>


성공적으로 로그인하면<br>

1. 자전거 대여
2. 자전거 반납
3. 자전거 추가 배치 요청
4. 자전거 고장 신고
5. 회원 정보 조회
6. 로그아웃

<h2>주요 함수</h2>
db_connect(): <br>
db_close(): <br>
register_user(): 회원가입 기능<br>
login(): 로그인 기능<br>
center_lists(): 자전거 대여소 정보 리스트 반환하는 함수<br>
rental_center(): center_lists 데이터베이스에 저장하는 함수<br>
rental(): 대여함수 -> 대여시각과 대여소아이디 반환 -> 해당 대여소 자전거 -1<br>
rental_func(): <br>
func_return(): 반납함수 -> 대여시각과 대여소아이디 반환 -> 해당 대여소 자전거 +1<br>
request_cycle(): 자전거 추가 배치 요청 (입력한 숫자만큼 자전거 +)<br>
report_cycle(): 고장 신고 접수된 대여소의 자전거 처리<br>
user_information(id): 회원 정보 출력<br><br>
<h2>데이터베이스 설계</h2>

![image](https://user-images.githubusercontent.com/83086978/166724267-3774523b-c624-4be8-9b39-300144704eaf.png)



