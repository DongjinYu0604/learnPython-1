# 윈도우창 띄우기
# 필요한 모듈 불러오기. 기본적 UI 구성요소를 제공하는 위젯(클래스)들은
# PyQt.QtWidgets 모듈에 포함되어 있다. 상세설명은 QtWidget 공식문서 참조
# http://pyqt.sourceforge.net/Docs/PyQt5/QtWidgets.html#PyQt5-QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('First Application') # 타이틀바에 나타나는 창 제목 설정
        self.move(300, 300)  # 위젯을 스크린의 x, y 위치로 이동
        self.resize(400, 200) # 위젯의 크기를 너비 400, 높이 200으로 조절
        self.show() # 위젯을 스크린에 보여줌

if __name__ == '__main__':   # name은 현재 모듈의 이름이 저장되는 내장 변수로 프로그램의 직접실행, 모듀을 통한 실행 여부 확인 가능
   app = QApplication(sys.argv) # PyQt5 어플리케이션 객체 생성하기
   ex = MyApp()
   sys.exit(app.exec_())