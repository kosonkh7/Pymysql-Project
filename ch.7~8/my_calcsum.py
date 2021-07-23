#함수 정의
def calcsum(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum

def calcrange(begin, end):
    sum = 0
    for i in range(begin, end + 1):
        sum += i
    return sum

#함수 호출
print("4까지의 합 : ", calcsum(4))
print("10까지의 합 : ", calcsum(10))
print("3에서 8까지의 합", calcrange(3, 8))

