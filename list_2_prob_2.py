# 5명의 학생의 최고점, 최소점, 평균점수를 구해주세요

# 5명의 점수를 입력받아 리스트에 저장
maro = []
동찬 = int(input('니 시험점수는?'))
maro.append(동찬)
상혁 = int(input('니 시험점수는?'))
maro.append(상혁)
규찬 = int(input('니 시험점수는?'))
maro.append(규찬)
예찬 = int(input('니 시험점수는?'))
maro.append(예찬)
사탄 = int(input('니 시험점수는?'))
maro.append(사탄)


# 가장 높은 점수와 가장 낮은 점수 찾기
maro.sort()
print("전체 점수:", maro)
maro.reverse()
print("최고 점수:", maro[0] )
maro.reverse()
print("최저 점수:", maro[0] )

