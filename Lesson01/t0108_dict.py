# 딕셔너리

# 1. 딕셔너리 만들기,
# 딕셔너리 = {키1: 값1, 키2: 값2}
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

# 빈 딕셔너리 만들기
# 딕셔너리 = {}, 딕셔너리 = dict()

# dict로 딕셔너리 만들기
# 딕셔너리 = dict(키1=값1, 키2=값2)
# 딕셔너리 = dict(zip([키1, 키2], [값1, 값2]))
# 딕셔너리 = dict([(키1, 값1), (키2, 값2)])
# 딕셔너리 = dict({키1: 값1, 키2: 값2})
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)    # 키=값 형식으로 딕셔너리를 만듦
lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))# zip 함수로 키 리스트와 값 리스트를 묶음
lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})# dict 안에서 중괄호로 딕셔너리를 만듦

# 2. 딕셔너리 사용하기
# 딕셔너리 뒤에 [ ](대괄호)를 사용하며 [ ] 안에 키를 지정
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health']
# 딕셔너리의 키에 값을 할당
# 딕셔너리[키] = 값
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health'] = 2037    # 키 'health'의 값을 2037로 변경
# 딕셔너리에서 키가 있는지 확인
# 키 in 딕셔너리
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
'health' in lux