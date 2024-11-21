# 점수를 입력받아 A, B, C, D, F 등급 판별하기
## 태도가 올바른지 o x 를 입력받아서
## 태도가 올바르면 점수에 +를 추가
## ex) A점 -> A+점

miro = int(input('너의 시험점수'))
maro = input('o')

if miro > 90 :
    print('A점!!!')
elif miro > 65 :
    print('B점!!')
elif miro > 50 :
    print('C점!')
elif miro > 30 :
    print('D점')
elif miro > 0 :
    print('F...')
else :
    print('you so suck')






if maro == 'o' :
    print('....점수에 +')
elif maro == 'x' :
    print('...점수에 -')
else :
    print('뭐 어쩌라고...')