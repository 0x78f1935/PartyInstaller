from PyQt5 import QtWidgets
from app import PartyInstaller
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = PartyInstaller()
    application.show()
    sys.exit(app.exec_())