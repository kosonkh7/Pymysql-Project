#2g, 3g, 5g 추가 각각 10개씩 있다, 추 무게의 합이 81g이 되는 조합을 찾는 것
count = 0

for i in range(11):
    for j in range(11):
        for k in range(11):
            if (2*i + 3*j + 5*k) == 81:
                print("2g추 : ", i, "개 3g추 : ", j, "개 5g추 : ", k, "개")
                count +=  1

print("총", count, "번 발생")