import sys
from utils.snellsLaw import SnellsLaw
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('Snell\'s Law')

    myApp = SnellsLaw()

    sys.exit(app.exec())
