from PyQt5 import QtWidgets, QtCore, QtGui, QtWidgets, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QPushButton, QApplication

from app.utils.ui_tools import UITools, InstallationPopup
from app.utils.web_tools import WebTools
from app.window.main import Ui_MainWindow
from os.path import exists, join
import os, pathlib
import sys

class PartyInstaller(QtWidgets.QMainWindow):
    def __init__(self):
        super(PartyInstaller, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.installwidget = None

        # Turn off the popup view #######################
        self.ui.layoutframe.setVisible(True)            #
        self.ui.layoutversionsframe.setVisible(False)   #

        self.statustext = "" # Set a empty status bar

        # Initialize custom tools #######
        self.tools = UITools(self)      #
        self.webtools = WebTools(self)  #

        self.data = self.webtools.scrape_all_pages() # Fetch data from eek
        
        # Time to generate buttons from the information fetched
        rows = self.tools.create_rows(self.data, self.look_for_story_versions, self.ui.layout) 
        self.ui.rows = [i for i in rows[0].children() if type(i) == QPushButton]  # Assign the buttons to the UI
        
        self.configured = False # Application is not yet configured
        
        # Try to automatically find the stories folder
        if exists(self.tools.find_storie_folder()):
            # If it exists then the installation path is piece of cake
            self.installation_path = self.tools.find_storie_folder()
            # Also set the mod path
            self.mod_path = pathlib.Path(self.installation_path).resolve().parent

            # For UI sake ###################################################
            if os.path.exists(os.path.join(self.mod_path, 'Censorship')):   #
                self.ui.setCensorship.setText("Turn Censorship Off")        #
            else: self.ui.setCensorship.setText("Turn Censorship on")       #
            self.ui.setCensorship.setEnabled(True)                          #
            
            self._configure_installation_dir()  # Prep the installation dir

        else: # It failed? 
            self.installation_path = None # Unknown
            self.mod_path = None  # Unknown
            self.ui.setCensorship.setEnabled(False) # No install path no nudity
            # inform the user to set the installation path
            self.set_info("Please configure the application first before using.")
            self.statustext = f'Game {self.data["current_version"]} | Game `Stories` folder not found'
            self.set_statusbar(self.statustext)

        # Assign actions to header menu #####################################
        self.ui.setFolder.triggered.connect(self.set_installation_folder)   #
        self.ui.setCensorship.triggered.connect(self.set_censorship)        #

    def event(self, e):
        """This method makes sure the status bar text is always what is should be, uses the self.statustext as text.
        The texts used here should be `root` text. Important messages that you want to show to fill in gaps.
        """
        if e.type() == QtCore.QEvent.StatusTip:
            if e.tip() == '':
                e = QtGui.QStatusTipEvent(self.statustext)  # Set this to whatever you like
        return super().event(e)

    def set_info(self, text: str):
        """Sets the UI text to the given text parameter"""
        self.ui.Info.setText(text)

    def set_statusbar(self, text: str):
        """Sets the texts of the footer bar"""
        self.ui.statusbar.showMessage(text)
        QApplication.processEvents()  # Refreshes the ui mid execution

    def __set_buttons(self):
        """Get the rendered buttons"""
        result = {}
        for rowbuttons in self.ui.rows:
            for installbtn in rowbuttons.children():
                result[installbtn.objectName().lower()] = installbtn
        return result

    def look_for_story_versions(self, name):
        self.statustext = f'Game {self.data["current_version"]} | Looking for versions ...'
        self.set_statusbar(self.statustext)

        _buttons = self.__set_buttons()
        button = _buttons[name]
        forum = self.data['stories'][name]
        storyzips = self.webtools.scrape_zip(forum)

        self.installwidget = InstallationPopup(self, name, storyzips, forum, button=button)
        self.ui.layoutversions.addWidget(self.installwidget)
        self.toggle_view(options=True)
        

        self.statustext = f'Game {self.data["current_version"]} | {self.installation_path}'
        self.set_statusbar(self.statustext)

    def toggle_view(self, options=False):
        """Toggles between main view and the popup installation view
        If options is enabled, the popup ui installation will be forced
        """
        if options:
            self.ui.layoutframe.setVisible(False)
            self.ui.layoutversionsframe.setVisible(True)
        else:
            self.ui.layoutframe.setVisible(True)
            self.ui.layoutversionsframe.setVisible(False)

    def _configure_installation_dir(self):
        """Activates all install buttons if installation path has been set"""
        if not self.configured:
            self.configured = True
            for rowbuttons in self.ui.rows:
                for installbtn in rowbuttons.children():
                    installbtn.setEnabled(True)
            self.ui.setCensorship.setEnabled(True)

        self.set_info(f"Party Installer found {len(self.data['stories'].items())} custom stories.")
        self.statustext = f'Game {self.data["current_version"]} | {self.installation_path}'
        self.set_statusbar(self.statustext)

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

    def _create_dir_if_not_exists(self, _dir:str):
        if not os.path.exists(_dir): os.makedirs(_dir)
        
    def set_censorship(self):
        """This method installs the censorship mod or if its installed it removes it."""
        if self.mod_path is None: self.mod_path = pathlib.Path(self.installation_path).resolve().parent
        self._create_dir_if_not_exists(os.path.join(self.mod_path, 'Censorship'))
        if os.path.exists(os.path.join(self.mod_path, 'Censorship')):
            if os.path.exists(os.path.join(self.mod_path, 'Censorship', 'FuckCensorship.txt')):
                os.remove(os.path.join(self.mod_path, 'Censorship', 'FuckCensorship.txt'))
                os.rmdir(os.path.join(self.mod_path, 'Censorship'))
                self.ui.setCensorship.setText("Turn Censorship On")
            else:
                with open(os.path.join(self.mod_path, 'Censorship', 'FuckCensorship.txt'), 'w') as f:
                    f.write("")
                self.ui.setCensorship.setText("Turn Censorship Off")
        else:
            self.statustext = f'Game {self.data["current_version"]} | Unable to set Censorship'
            self.set_statusbar(self.statustext)  