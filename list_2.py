




# # 리스트를 생성하는법!
# empty_list1 = []
# empty_list2 = list()

# # 초기 데이터를 아는경우
# # numbers = [1, 2, 3, 4, 5]
# mixed = [1, "Hello", 3.14, True] # 파이썬에서는 데이터를 혼용가능하다

# # 다른 군집 자료형들
# tuple = (1, 2, 3)
# dictionary = {'a':1, 'b':3}


# # 인덱스
# # 자료의 순서!
# # 주의! 0부터 시작함
# # 인덱스 값이 자료의 길이보다 크면?
# # 오류가 납니다
# # -인덱스 값은 뒤에서부터 다시 자료를 찾습니다


# # 슬라이싱
# # 자르는거
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# # 2, 3, 4 만 잘라내려면?
# print(numbers[2:5])
# print(numbers[:5])
# print(numbers[2:])
# print(numbers[::2])

# fruits = ['사과', '바나나', '오렌지', '체리']
# # 사과 바나나만 슬라이스!
# print(fruits[:2])


#0 = 빈공간


# 리스트 연장하기
fruits = ['사과', '바나나', '오렌지', '체리']

fruits.append('폭탄')
# fruits.clear()
# print(fruits)
# fruits.append('마로')
# fruits.append('아기')
# print(fruits)
# fruits.remove('아기')
# print(fruits)
# fruits.append('마로')

# insert
# 원하는 위치에 데이터 추가
fruits.insert(1 , '데이터')
print(fruits)
# reverse
# 순서를 뒤집음
fruits.reverse()
print(fruits)
# pop
# 맨 '마지막' 데이터를 삭제
fruits.pop()
print(fruits)
# extend - 확장하다
# 두개의 리스트를 합칠때 사용
more_fruits = ['망고','수박']
fruits.extend(more_fruits)
print(fruits)
# count
# 특정 값이 몇개가 포함되어 있는지 확인
fruits.append('데이터')
fruits.append('데이터')
fruits.append('데이터')
fruits.append('데이터')
fruits.append('데이터')
fruits.append('데이터')
print(fruits.count('데이터'))

# sort (정렬)
# 데이터를 가나다 순으로 정리
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)


# 깊은 복사와 얕은 복사
# 깊은 복사 : 데이터를 복사해서 새로 저장
# 얕은 복사 : 데이터를 복사하지 않고 하나의 데이터를 조회하는 두개의 변수가 생김
# fruit_copy = fruits.copy()
# fruit_copy.clear()
# print(fruit_copy)
# print(fruits)










































