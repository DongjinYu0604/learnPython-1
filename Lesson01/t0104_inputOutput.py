# Lesson01 파이썬 기초
# t004 - 입출력함수
# 1. input 함수 : 사용자로 부터 입력 받기
# 변수 = input(메시지내용)
a = input("a값을 입력해주세요.")
print(a)

# 두 숫자의 합 구하기
a = input()
# a = input('숫자 1을 입력하세요')
b = input()
# b = input('숫자 2를 입력하세요')
print(a+b)  # 문자열의 결합...
type(a)     # str 확인
# int() 함수 이용, 입력값을 정수로 변환하기
print(int("100")) # 문자열 100을 정수 100을 변환하여 출력
# 변수 = int(input('문자열')

# 입력값을 두개의 정수로 저장하기
# 변수1, 변수2 = input('문자열').slit()
# 변수1, 변수2 = input('문자열').slit(구분기호)
# map을 사용하여 정수로 변환
#   변수1, 변수2 = map(int, input().split())
#   변수1, 변수2 = map(int, input().split('기준문자열'))
#   변수1, 변수2 = map(int, input('문자열').split())
#   변수1, 변수2 = map(int, input('문자열').split('기준문자열'))

# 2. Print 함수
# print에는 변수나 값 여러 개를 ,(콤마)로 구분하여 넣을 수 있다.
# print(값1, 값2, 값3)
# print(변수1, 변수2, 변수3)
#
# 값 사이에 공백이 아닌 다른 문자를 넣을 때
# print(값1, 값2, sep='문자 또는 문자열')
# print(변수1, 변수2, sep='문자 또는 문자열')
#
# sep에 \n, \t, \\ 사용
#
#
