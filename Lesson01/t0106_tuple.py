# 튜플 : 파이썬에서 제공하는 또 다른 자료형
# 리스트처럼 요소를 일렬로 저장하지만, 안에 저장된 요소를 변경, 추가, 삭제가 불가능하다.
# 바꾸어말하면 튜플은 읽기 전용 리스트라고 생각할 수 있다.

#
# 1. 튜플 만들기
# 변수에 값을 저장할 때 ( )괄호로 묶어주면 튜플이 되며, 각 값은 ,(콤마)로 구분한다.
# 또는 괄호로 묶지 않고 값만 콤마로 구분해도 튜플이 된다.
#
# 튜플 = (값, 값, 값)
# 튜플 = 값, 값, 값
#
varTuple = (1, 2, 3, 4, 5)
print(varTuple)
varTuple = 1, 2, 3, 4, 5
print(varTuple)
print(type(varTuple))
#
# 튜플도 리스트처럼 여러 자료형을 혼합 저장할 수 있다.
person = ('김한국', 175, 65.8, True)
print(person)
print(type(person))

# 2. range를 사용하여 튜플 만들기
# 튜플 = tuple(range(횟수))
# 튜플 = tuple(range(시작, 끝,증가폭))

# 3. 튜플을 리스트로, 리스트를 튜플로 만들기
varLst = [1,2,3]
varTuple = tuple(varLst)
print(type(varTuple))