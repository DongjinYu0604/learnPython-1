#        1         2         3         4         5         6         7         8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# lesson01 파이썬 기초
# t001 : hello.py
# python, pycharm 설치 및 환경 설정  설정 후
# create project > create new python file로
# 간단한 메시지를 출력하는 프로그램을 작성하여

#
# 0. Python 설치
#    https://www.python.org/downloads/ 에서 다운로드 설치
#    Jan.07, 2021 현재, latest Python 3 Release - Python 3.9.1 은
#    2020년 12월 7일자로 released.
# 0. Pycharm 설치
#    https://www.jetbrains.com/ko-kr/pycharm/  에서 community 다운로드 설치
#    Jan.07, 2021 현재, 2020.3.2 버전, 빌드 203.6682.179, 2020-12-30
# 0. Github 설치
# 0. Git 설치
#
# ※ 파이썬 설치없이 파이썬 실행하기 :
#   a. 파이썬 메인 홈페이지 중간부분에 노란색 버튼 클릭
#   b. 구글 colab 사용하기

# pycharm settings :
#   File > settings
#     - Appearnace & Behavior > Appearance에서
#       Theme 선택
#       Use custom font 체크선택하고 폰트와 크기를 결정한다.
#   Editor
#     > General에서
#       - Mouse Contrl : Change font size with Ctrl + Mouse Wheel 체크 설정
#                           Move code fragments with drag-and-drop 체크 설정
#    > Font 에서 Font, Size, Line spacing 설정
#    > Code Style
#      - Python : Tab size, Indent, Continuation indent를 각각 4,4,8 확인
#    > Version Control :  + 클릭 후, 디렉토리, VCS를 Git으로
#           GitHub에서 +클릭하여 github 계정 정보로 로그인 정보 추가후 OK
#
print('Hello, Python with PyCharm')
# 1. 실행을 확인한다.
# 실행 단축키 : Ctrl + Shift + F10

# 위 출력문의 실행결과를 확인하고,

#  먼저, 주석에 대해 설명하자.
#  #기호는 한 행 주석,  단축키는 Ctrl + /
#    ''' ~ ''' 는 블록 주석
# TODO: 주석
# TODO: 주석문은 연두색으로 눈에 띄게 표시되고, 오른쪽으로 파란색 bar가 생긴다.
# TODO: 못다한 코딩이 있을 때 유용하게 사용한다.
# todo: 주석을 끝내려면 아래에 공백라인을 하나 추가하여야 한다.

#  2. 편집창을 설명한다.
#     먼저, 왼쪽의 줄 번호 line number. Ctrl + G를 이용하여 원하는 라인이동 가능
#
# 3. 우측 상단의 빨간 느낌표는 현재 이 파일에 sysntax error가 숫자만큼 있다는 의미
##
# 4. 편집 창의 빈공간에서 마우스 우클릭 Local History > Show History 클릭
#     해당 파일이 어떻게 수정되어 왔는지가 저장된다.

# 5. Ctrl + 마우스휠드라이브 : 편집창 폰트 크기 변경
#    File > Settings > Editor > General > Mouse Control에서 Change Font Size..

# 6. 자동완성기능 : File >Settings > Editor > General > Smart Keys에서 변경가능
#   함수나 클래스 정의시, 삼중 따옴표를 함수 prototype 바로 밑에 써 주면
#   깔끔하게 사용법을 정리할 수 있는 주석이 나타남. 빈 줄에는 함수설명을,
#   param에는 각 인자의 설명을, return에는 이 함수의 반환값 설명을 적어준다.

# 7. 빠른 선택, 코드 정리, 편집 등 단축키

# 8. Refactor(이름 재지정)
# 변수명을 바꾸고 싶을 때가 있다.
# 일일이 바꾸거나, Find and Replace도 가능하나
#  해당변수를 선택하고, Sift + F6를 누른다.
#  원하는 이름으로 바꾸고 Refactor를 누르면 해당변수만
# 정확하게 원하는 이름으로 바꾼다. 다른 파일에서도 바뀐다.

# 9. 디버깅 방법
#
# 10. Github 버저닝 방법 설명
# https://ellun.tistory.com/280
#
#        1         2         3         4         5         6         7         8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890