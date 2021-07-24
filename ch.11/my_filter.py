#filter 함수 - 조건에 해당하는 것만 추출
def flunk(s):
    return s < 60

score = [40, 20, 30, 90, 75]
for s in filter(flunk, score): #lambda s:s < 60으로 표현 가능
    print(s)

#map 함수 - 함수를 일괄 적용하는 것
def half(s):
    return s / 2
#lambda s : s / 2와 같은 의미
for s in map(lambda s : s / 2, score):
    print(s, end = ', ')

score = [ ['kim', 90], ['lee', 80], ['han', 85]]
