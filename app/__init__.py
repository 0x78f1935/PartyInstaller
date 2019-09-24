from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QPushButton

from app.utils.ui_tools import UITools
from app.utils.web_tools import WebTools
from app.window.main import Ui_MainWindow
from os.path import exists, join
import sys

class PartyInstaller(QtWidgets.QMainWindow):
    def __init__(self):
        super(PartyInstaller, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.tools = UITools()
        self.webtools = WebTools()

        self.data = self.webtools.scrape_all_pages()

        if exists(self.tools.find_storie_folder()): # Try to automatically find the stories folder
            self.configured = True
            self.installation_path = self.tools.find_storie_folder()
            self._configure_installation_dir()
        else: # It failed? 
            self.configured = False
            self.set_info("Please configure the application first before using.")
            self.set_statusbar(f'Game {self.data["current_version"]} | Game `Stories` folder not found')
            self.installation_path = None

        # data = [("hello", "https://google.com"), ("world", "https://codewars.nl")]
        
        rows = self.tools.create_rows(self.data, self.execute_installation, self.ui.layout)
        self.ui.rows = [ i for i in rows[0].children() if type(i) == QPushButton]

        self.ui.setFolder.triggered.connect(self.set_installation_folder)
  
    def set_info(self, text: str):
        """Sets the UI text to the given text parameter"""
        self.ui.Info.setText(text)

    def set_statusbar(self, text: str):
        """Sets the texts of the footer bar"""
        self.ui.statusbar.showMessage(text)

    def __set_buttons(self):
        """Get the rendered buttons"""
        result = {}
        for rowbuttons in self.ui.rows:
            for installbtn in rowbuttons.children():
                result[installbtn.objectName().lower()] = installbtn
        return result

    def execute_installation(self, name):
        
        # data = self.webtools.fetch_all_li(self.webtools.create_html_page_from_url("https://forum.eekllc.com/viewforum.php?f=8"))
        # for rowbuttons in self.ui.rows:
        #     for installbtn in rowbuttons.children():
        _buttons = self.__set_buttons()
        button = _buttons[name]
        forum = self.data['stories'][name]
        storyzips = self.webtools.scrape_zip(forum)
        print(f"Installing {storyzips}")
        # TODO show popup with zip installation choices
        return
        # for item in data: print(item)

    def _configure_installation_dir(self):
        if not self.configured:
            self.configured = True
            self.set_info(f"Party Installer found {len(self.data['stories'].items())} custom stories.")
            self.set_statusbar(f'Game {self.data["current_version"]} | {self.installation_path}')
            for rowbuttons in self.ui.rows:
                for installbtn in rowbuttons.children():
                    installbtn.setEnabled(True)

    def set_installation_folder(self):
        """This method fetches usefull data out of the path choosen.
        Configures the application for use.
        """
        self.installation_path = QFileDialog.getExistingDirectory(
            parent=self,
            directory=join(self.tools.find_my_document_folder(), 'Documents'),
            caption='Select the steam installation folder',
        )
        self._configure_installation_dir()

