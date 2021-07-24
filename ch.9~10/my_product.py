import datetime as dt

products = {'꼬부기': 1500,'새우깡': 1200, '츄파츕스':200, "쫀드기": 800, '자일리톨':100}
total_products = dict()

def register_product():
    name = input("상품명: ")
    price = int(input("가격: "))
    products['name'] = price

def display_product():
    for i in products.items():
        name, price = i
        print(name, price)

def search_product():
    name = input("상품명 : ")
    if name in products:
        print("가격은", products[name])
    else:
        print('존재하지 않은 상품입니다.')

def sale_product():
    name = input("상품명 : ")
    number = int(input("판매 수량 :"))
    if name in products:
        print(f'{name}의 판매금액은 {products[name] * number}원입니다.')

while True:
    print('1, 상품 등록')
    print('2, 상품 목록')
    print('3, 상품 가격 조회')
    print('4, 결제 대금')
    print('5, 매출 집계')
    print('6, 일일 매출 현황')
    print('9, 종료')
    choice = input('선택 >>> ')
    if choice == '1':
        register_product()
    elif choice == '2':
        display_product()
    elif choice == '3':
        search_product()
    elif choice == '4':
        sale_product()
    elif choice == '9':
        print("프로그램 종료")
        break
    else:
        print("프로그램을 종료하려면 '9'를 입력해주세요")
