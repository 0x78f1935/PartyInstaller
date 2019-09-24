from PyQt5 import QtWidgets
from app.utils.ui_tools import UITools
from app.utils.web_tools import WebTools
from app.window.main import Ui_MainWindow
import sys

class PartyInstaller(QtWidgets.QMainWindow):
    def __init__(self):
        super(PartyInstaller, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.tools = UITools()
        self.webtools = WebTools()

        # data = [("hello", "https://google.com"), ("world", "https://codewars.nl")]
        self.data = self.webtools.scrape_all_pages()
        self.set_info(f"Party Installer found {len(self.data['stories'].items())} custom stories.")
        self.tools.create_rows(self.data, self.test, self.ui.layout)
    
    def set_info(self, text: str):
        """Sets the UI text to the given text parameter"""
        self.ui.Info.setText(text)


    def test(self):
        
        # data = self.webtools.fetch_all_li(self.webtools.create_html_page_from_url("https://forum.eekllc.com/viewforum.php?f=8"))
        print("Installing")
        return
        # for item in data: print(item)
