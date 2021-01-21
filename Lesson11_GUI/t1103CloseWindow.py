# 창 닫기
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication  # QtCore의 QCoreApplication 클래스를 불러온다.


class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      # 푸시버튼 생성, 이 버튼 btn은 QPushButton 클래스의 인스턴스이다.
      # 첫 번째 파라미터는 버튼에 표시될 텍스트, 두 번재 패러미터는 버튼이 위치할 부모 위젯
      btn = QPushButton('Exit', self)
      btn.move(50, 50)
      btn.resize(btn.sizeHint())
      btn.clicked.connect(QCoreApplication.instance().quit)
      # PyQt5의 이벤트 처리는 시그널과 슬롯 메커니즘
      # 버튼 클릭시 clicked 시그널 생성, instance() 메서드는 현재 인스턴스 반환
      # clicked 시그널은 현재인스턴스의 quit()메서드와 연결
      # 발신자와 수신자 두 객체간 커뮤니케이션이 이루어진다.
      # 발신자는 푸시버튼, 수신자는 애플리케이션 객체(app)

      self.setWindowTitle('Exit Button')
      self.setGeometry(300, 300, 300, 200)
      self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())