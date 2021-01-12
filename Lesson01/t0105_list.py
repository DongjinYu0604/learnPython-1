'''
lesson01 파이썬 기초
t0105_list.py
리스트가 무엇인지, 리스트의 항목을 어떻게 다루는지 설명

1. 리스트란 : 특정 순서가 있는 데이터 항목의 모음, 보통 두 개 이상의 항목을 갖기에
              리스트 이름은  letters, digits, names처럼 복수형으로 사용
              파이썬에서는 []로 감싸서 표현하며, 각 항목은 콤마(,)로 구분
'''
kGenerals = ['괴유', '을지문덕', '연개소문', '이순신']
print(kGenerals)


# 2. 리스트 항목에 접근하기
print(kGenerals[0])  # 인덱스 위치는 0에서 시작. zero-base
print(kGenerals[-1])  # 리스트의 마지막 항목

# 3. 리스트 항목변경, 추가, 제거
kGenerals[3] = '양만춘'
print(kGenerals)
kGenerals.append('고선지')  # 리스트의 끝에 항목 추가
print(kGenerals)
kGenerals.insert(1,'온달')  # 지정 인덱스에 항목 추가
print(kGenerals)

#4. 리스트에서 항목제거
del kGenerals[0] # del 리스트이름[제거할항목의인덱스]
print(kGenerals)
popped = kGenerals.pop() # 마지막 항목을 꺼내어 popped에 
print(popped)
print(kGenerals) # 나머지 항목 출력
# 리스트의 아무위치에서나 항목 꺼내기
first = kGenerals.pop(0)
print(first)
print(kGenerals)
# 값으로 항목 제거하기
kGenerals.remove('양만춘')  # 리스트에 같은 값이 여러 개 있다면 첫 번째 항목만 제거함
print(kGenerals)

#5. 리스트 정리하기
cars = ['SONATA', 'K7', 'GRANDEUR', 'SM5', 'AVANTE']
cars.sort()
print(cars)
cars.sort(reverse=True) # descending sort
print(cars)
cars.reverse() # 역순으로 바꾸기
print(cars)
print(len(cars)) # 리스트 길이 구하기
