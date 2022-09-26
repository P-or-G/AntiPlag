import sys, math

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox, QProgressBar
from PyQt5.QtWidgets import QTextBrowser



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('plagiat.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.doubleSpinBox.valueChanged.connect(self.ch)
        self.m = self.doubleSpinBox.value()
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def ch(self):
        self.m = self.doubleSpinBox.value()
        print(self.m)

    def run(self):
        eq = 0
        text = self.plainTextEdit.toPlainText().split('\n')
        text2 = self.plainTextEdit_2.toPlainText().split('\n')
        lt = len(text)
        lt2 = len(text2)
        for st in text:
            for st2 in text2:
                if st2 == st:
                    if lt > lt2:
                        text.remove(st)
                    else:
                        text2.remove(st2)
                    eq += 1
        if lt > lt2:
            per = eq / lt * 100
        else:
            per = 100 - (eq / lt2 * 100)
        if per >= self.m:
            per = round(per)
            self.progressBar.setValue(per)
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
