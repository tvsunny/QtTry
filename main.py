import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from EyeTrackerDataAnalysis import Ui_EyeTrackerDataAnalysisClass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_EyeTrackerDataAnalysisClass()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
