
from PyQt4.QtGui import QApplication

from main_window import MainWindow


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main = MainWindow()
    with open('tema.qss', 'r') as f:
        tema = f.read()
    app.setStyleSheet(tema)
    main.show()

    sys.exit(app.exec_())
