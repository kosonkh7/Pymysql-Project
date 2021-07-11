one_list = ['ko', 54.2, 94.3, 34.3]

def calcavg(list):
    sum = 0
    for i in list[1:]:
        sum += i
    avg = sum / len(list[1:])
    print(list[0], '의 평균:', round(avg, 2))
    #print(f'{st_list[0]}의 평균 점수는 {round(avg,2)}입니다.')

calcavg(one_list)

three_list = [ [ 'kim', 95.4, 67.8, 89.5 ],
                [ 'lee', 85.4, 78.8, 84.5 ],
                [ 'park', 76.3, 73.8, 68.5 ] ]

for i in three_list:
    calcavg(i)
#i가 리스트이므로 i를 전달하는 것이 옳다
#이중리스트에 이중 for문 사용하는 원리 정확하게 이해하기