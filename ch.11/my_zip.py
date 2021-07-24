#zip 함수에 대한 이해

yoil = ['월', '화', '수', '목', '금', '토', '일']
food = ['갈비탕', '순대국', '칼국수', '삼겹살']

menu = zip(yoil, food)
for y, f in menu:
    print(f"{y}요일 메뉴 : {f}")