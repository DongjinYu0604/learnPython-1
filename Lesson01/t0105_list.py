'''
lesson01 파이썬 기초
t0105_list.py
리스트가 무엇인지, 리스트의 항목을 어떻게 다루는지 설명

리스트 : 특정 순서가 있는 데이터 항목의 모음, 보통 두 개 이상의 항목을 갖기에
         리스트 이름은  letters, digits, names처럼 복수형으로 사용
        파이썬에서는 []로 감싸서 표현하며, 각 항목은 콤마(,)로 구분
'''
kGenerals = ['괴유', '을지문덕', '연개소문', '이순신']
print(kGenerals)

# 1. 리스트 만들기
# 빈 리스트 만들 때는 []만 지정
kGenerals = []
print(kGenerals)
# 또는 list()
kGenerals = list()
print(kGenerals)
# range를 이용하여 리스트 만들기. range(횟수),  range(시작,끝), range(시작, 끝, 증가폭)
numberList = list(range(10))   # 0 ~ 9까지의 수 10개가 들어가는 리스트 생성
print(numberList)

# 2. 리스트 항목에 접근하기
# 인덱스 활용
print(kGenerals[0])  # 인덱스 위치는 0에서 시작. zero-base
print(kGenerals[-1])  # 리스트의 마지막 항목

# 3. 리스트 항목변경, 추가, 제거
# append(), insert(인덱스, 값)
kGenerals[3] = '양만춘'
print(kGenerals)
kGenerals.append('고선지')  # 리스트의 끝에 항목 추가
print(kGenerals)
kGenerals.insert(1,'온달')  # 지정 인덱스에 항목 추가
print(kGenerals)

#4. 리스트에서 항목제거
#  del 명령을 인덱스와 함께
del kGenerals[0] # del 리스트이름[제거할항목의인덱스]
print(kGenerals)
popped = kGenerals.pop() # 마지막 항목을 꺼내어 popped에 
print(popped)
print(kGenerals) # 나머지 항목 출력
# 리스트의 아무위치에서나 항목 꺼내기
# pop(인덱스)
first = kGenerals.pop(0)
print(first)
print(kGenerals)
# 값으로 항목 제거하기
# remove(키값)
kGenerals.remove('양만춘')  # 리스트에 같은 값이 여러 개 있다면 첫 번째 항목만 제거함
print(kGenerals)

#5. 리스트 정리하기
cars = ['SONATA', 'K7', 'GRANDEUR', 'SM5', 'AVANTE']
# 정렬 : sort(), sort(reverse=??)
cars.sort()
print(cars)
cars.sort(reverse=True) # descending sort
print(cars)
# 뒤집기 reverse()
cars.reverse() # 역순으로 바꾸기
print(cars)
# 길이 len()
print(len(cars)) # 리스트 길이 구하기

#6. 리스트에 여러 가지 자료형 저장
# 리스트는 문자열, 정수, 실수, 불 등 모든 자료형을 저장할 수 있으며, 혼합 저장도 가능
# 여러 가지 자료형을 사용하면 관련 정보를 하나로 묶기 좋다
person = ['김한국', 175, 65.8, True]  # 김한국의 신장, 몸무게, 학생여부
print(person)