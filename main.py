import sys, math

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox, QProgressBar
from PyQt5.QtWidgets import QTextBrowser, QStatusBar


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('plagiat.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.doubleSpinBox.valueChanged.connect(self.run)

    def run(self):
        m = self.doubleSpinBox.value()
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
            per = eq / lt2 * 100
        if m < round(per, 2):
            self.statusBar().showMessage(f'Ваш код похож на {str(per)}%')
            self.statusBar().setStyleSheet("""
        QWidget {
            background-color: rgb(255, 0, 0);
            }
        """)
        else:
            self.statusBar().showMessage(f'Ваш код похож на {str(per)}%')
            self.statusBar().setStyleSheet("""
            QWidget {
                background-color: rgb(0, 255, 0);
                }
            """)
        m = 0
        eq = 0
        text = 0
        text2 = 0
        lt = 0
        lt2 = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
