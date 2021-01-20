# Application Icon 삽입하기
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      self.setWindowTitle('Show Icon at title bar')
      self.setWindowIcon(QIcon('web.png')) # 애플리케이션의 아이콘 설정
      self.setGeometry(300, 300, 300, 200) # 창의 위치와 크기를 동시에 설정. 앞의 move() + resize()
      self.show()


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())