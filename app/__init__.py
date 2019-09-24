from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QPushButton

from app.utils.ui_tools import UITools
from app.utils.web_tools import WebTools
from app.window.main import Ui_MainWindow
import sys

class PartyInstaller(QtWidgets.QMainWindow):
    def __init__(self):
        super(PartyInstaller, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.configured = False
        self.set_info("^ Please configure the application first")


        self.tools = UITools()
        self.webtools = WebTools()

        self.installation_path = None

        # data = [("hello", "https://google.com"), ("world", "https://codewars.nl")]
        self.data = self.webtools.scrape_all_pages()
        
        self.ui.Version.setText(self.data["current_version"])
        rows = self.tools.create_rows(self.data, self.execute_installation, self.ui.layout)
        self.ui.rows = [ i for i in rows[0].children() if type(i) == QPushButton]

        self.ui.setFolder.triggered.connect(self.set_installation_folder)
    
    def set_info(self, text: str):
        """Sets the UI text to the given text parameter"""
        self.ui.Info.setText(text)


    def execute_installation(self):
        
        # data = self.webtools.fetch_all_li(self.webtools.create_html_page_from_url("https://forum.eekllc.com/viewforum.php?f=8"))
        print("Installing")
        return
        # for item in data: print(item)

    def set_installation_folder(self):
        """This method fetches usefull data out of the path choosen.
        Configures the application for use.
        """
        self.installation_path = QFileDialog.getExistingDirectory(
            parent=self,
            caption='Select the steam installation folder',
        )
        if not self.configured:
            self.configured = True
            self.set_info(f"Party Installer found {len(self.data['stories'].items())} custom stories.")
            for rowbuttons in self.ui.rows:
                for installbtn in rowbuttons.children():
                    installbtn.setEnabled(True)
            