#리스트 내의 유효하지 않은 점수는 continue를 통해 제외하고 집계하여 평균을 구하는 프로그램

score_list = [67,96,88,62,-78,90,100,85,80,107,45,69,73]
total = 0 ; count =0 ; no = 0

for score in score_list:
    if score >= 0 and score <= 100:
        total += score
        count += 1
    else:
        print(no, "번의 시험 점수가 유효하지 않습니다")
        continue
    no += 1

print("평균 : ",round(total/count, 1))