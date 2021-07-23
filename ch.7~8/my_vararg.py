#가변인수에 대한 이해 (여기선 *ints)
#앞에 별(*)을 붙이면 여러 개의 인수 전달 가능

def intsum(*ints):
    print(type(ints))
    sum = 0
    for num in ints:
        sum += num
    return sum

print(intsum(1, 2, 3))
print(intsum(5, 6, 7, 9, 16))
print(intsum(1, 3, 4, 4, 5))

#기본값 지정
def calcstep(begin, end, step = 1):
    sum = 0
    for i in range(begin, end + 1, step):
        sum += i
        return sum

print("1~10 = ", calcstep(1, 10, 2))
print("1~10 = ", calcstep(1, 100))

print("1~10 = ", calcstep(end=10, begin=1, step=2))
#이런 걸 키워드인수라고 한다.
#이렇게 지정해주면 순서를 지키지 않아도 상관 없다
