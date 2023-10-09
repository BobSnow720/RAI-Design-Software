
from PyQt5.QtWidgets import QApplication
import sys
from MainUI import MainCode

if __name__ == '__main__':
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # Qt从5.6.0开始，支持High-DPI
    app = QApplication(sys.argv)
    md = MainCode()
    md.show()
    sys.exit(app.exec_())