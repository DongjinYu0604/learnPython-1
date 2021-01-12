'''
Lesson01 파이썬 기초
t0103_varaiables.py - 변수와 타입
1. 변수의 개념 : 프로그램에서 사용할 데이터를 저장하는 메모리 공간에 붙여진 라벨
2. 변수만들기
   변수명 = 값      = 할당, 대입연산자
3. 변수명 규칙
변수 이름은 원하는 대로 지으면 되지만 다음과 같은 규칙을 지켜야 합니다.
  - 영문 문자와 숫자를 사용할 수 있다.
  - 대소문자를 구분한다.
  - 문자부터 시작해야 하며 숫자부터 시작하면 안 된다.
    _(밑줄 문자)로 시작할 수 있다.
  - 특수 문자(+, -, *, /, $, @, &, % 등)는 사용할 수 없다.
  - 파이썬의 키워드(if, for, while, and, or 등)는 사용할 수 없다.
  - 변수명에는 의미가 있어야 한다.
4. 변수에는 숫자 뿐만 아니라 문자열도 넣을 수 있다.
'''
x = 10  # x라는 변수에 상수값 10을 대입
y = 'hello, world'  # y라는 변수에 'hello, world' 문자열 값을 대입.
# 문자열은 큰따옴표나 작은따옴표 모두 사용가능
print(x)  # 변수 x를 화면에 출력
print(y)  # 변수 y를 화면에 출력
# 메서드를 사용해 문자열의 대소문자 바꾸기
name = 'python i love you'
print(name.title())  # 각 단어의 첫 글자를 대문자로
print(name.upper())  # 모두 대문자로
print(name.lower())  # 모두 소문자로

# 문자열 안에서 변수사용하기
firstName = 'korea'
lastName = 'academy'
# 변수 값을 문자열에 삽입할 때는 시작하는 따옴표 바로 앞에 f를 사용.
# 그리고 문자열 안에서 사용하고 싶은 변수 이름은 중괄호로 감싼다. 이런 문자열을 f-string이라고 부른다.
fullName = f'{firstName} {lastName}'
print(fullName)
# 탭이나 줄바꿈 문자를 써서 문자열에 공백문자(제어문자) - 스페이스, 탭, 줄바꿈 기호 등
# \n, \t, \n
# 공백 없애기; rstrip(), lstrip(), strp()

# 5. 변수의 타입 알아내기
x = 10
y = 'korea'
z = 1.234
print(type(x))
print(type(y))
print(type(z))

# 정수와 부동소수점 숫자 혼합 연산지 결과는 부동소수점으로 표현된다.
# 숫자와 밑줄 : 아주 큰 숫자를 쓸 때, 필요한 만큼 자릿수를 나눠서 자리를 밑줄로 구분
universeNumber = 1_234_567_890
# 정의할 때 밑줄을 사용하더라도, 출력할 때는 항상 밑줄 없이 출력됨
print(universeNumber)

# 6. 변수 여려 개를 한 번에 만들기
a, b, c = 10, 20, 30
print(a, b, c)
# 변수 값이 모두 같아도 된다면..
i = j = k = 10
print(i,j,k)
# 변수 삭제 :
del a,b,c,i,j,k
# print(a) # 오류 발생 a is not defined


# 상수 consant : 프로그램이 동작하는 동안 값이 바뀌지 않는 변수
PI = 3.1415292

'''
>>> import this 
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

'''