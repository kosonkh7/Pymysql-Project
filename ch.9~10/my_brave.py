#우효의 brave내 몇 구절
brave = """Every little moment that you wish that you were stronger
Every little moment of despair
Every little word that loses meaning in the air
Every little voice that goes unheard

Every single day that passes by as if the wind
Always steady yet so out of reach
Every stormy sea that sets ablaze a whole new fear
Every little sweet lie in disguise"""

alphabet = dict()
for ch in brave:
    #알파벳은 소문자로, 아니면 다음 반복문으로 이동
    if ch.isalpha() == False:
        continue
    ch = ch.lower()
    #alphabet 딕셔너리에 개수 넣는 조건문
    if ch not in alphabet:
        alphabet[ch] = 1
    else:
        alphabet[ch] += 1

print(alphabet)
# 문자열 안의 단어가 1.알파벳이 아니거나 2.공백일 경우에 continue
# 해당 문자를 lower 해준 다음 조건문 실행

key = list(alphabet.keys())
key.sort()
for i in key:
    num = alphabet[i]
    print(i, "=>", num)
#키의 리스트를 만들어 문자열 순서대로 정렬한 후 개수 출력

#for문 통해 알파벳 순서대로 정렬하는 방법(위와 결과는 같다)
for code in range(ord('a'), ord('z')+1):    #ord함수는 문자를 코드로 변환(range에 이용하기 위함)
    c = chr(code)                           #코드로 바꾼 걸 다시 chr함수로 문자로 바꿔줌
    num = alphabet.get(c, 0)                #없는 문자 0으로 설정하기 위함
    print(c, "=>", num)