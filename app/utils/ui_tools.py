from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)
from app.window.popup import Ui_Form
from app.utils.web_tools import WebTools
from functools import partial
from os.path import expanduser, join, exists
import webbrowser, platform, os

class UITools(object):
    def __init__(self, root):
        print(" * UI Tools initialized ...")
        self.row_margin = (-1, 60, -1, -1)
        self.root = root

    def action_open_forum_page(self, url):
        return webbrowser.open(url)

    def create_rows(self, data:list, callback, contentview):
        """ This method generates a listview (with rows) with the data provided.
        In this particulair case the row exists with a label, and two buttons.
        Assign a list to the data variable consistent with tuples. The Tuples
        have the following format:

        ("label", "Hyperlink")

        Note
        ----
        The third button is in this case a button with a function assigned.
        which is the `callback` parameter

        Parameters
        ----------
        data
            List,
                label
                    String, The text displayed in the UI
                hyperlink
                    String, The link the button should go to
        callback
            Method, Callback function for the install button to execute
        contentview
            Panel, The PyQt5 panel which the rows should be rendered on

        Returns
        -------
        Returns the rows we just created in list format, this way we can
        manipulate the rows themself in code
        """
        rows = []
        for name, url in data["stories"].items():
            ForumButton = QPushButton(name)
            ForumButton.clicked.connect(partial(self.action_open_forum_page, url=url))
            ItemInstall = QPushButton(ForumButton)
            ItemInstall.setText('Install')
            ItemInstall.clicked.connect(partial(callback, name=name))
            ItemInstall.setEnabled(False)
            ItemInstall.setObjectName(name)
            contentview.addWidget(ForumButton)
            rows.append(ForumButton.parentWidget())
        return rows

    def find_my_document_folder(self):
        """Locates my documents also works if documents location and/or default save location is changed by user."""
        return expanduser("~")

    def find_storie_folder(self):
        """Locates Stories folder"""
        if platform.system() == 'Windows':
            return join(self.find_my_document_folder(), 'Documents', 'Eek', 'House Party', 'Mods', 'Stories')
        else:  # Default wine prefix
            return join(expanduser('~'), '.steam', 'steam', 'steamapps', 'compatdata', '611790', 'pfx', 'drive_c', 'users', 'steamuser', 'My Documents', 'Eek', 'House Party', 'Mods', 'Stories')
            

class InstallationPopup(QtWidgets.QDialog):
    def __init__(self, root, name, storyzips, forum, button):
        super(InstallationPopup, self).__init__()

        self.name = name
        self.forum = forum
        self.storyzips = storyzips
        self.root = root
        self.installation_location = self.root.installation_path
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.tools = UITools(self)
        self.webtools = WebTools()

        self.ui.Name.setText(self.name) # Set title
        # Set information for install screen
        self.ui.installinfo.setText("""
        Make sure you install the base story first.
        Still having issues? Check out the forum page.
        """ )
        # Set forum button
        self.ui.forumbutton.clicked.connect(partial(self.tools.action_open_forum_page, url=forum))
        self.ui.backButton.clicked.connect(self.back)

        self.buttons = []
        for item in self.storyzips:    
            ForumButton = QPushButton(name)
            ForumButton.clicked.connect(partial(self.download, name=item[1], url=item[0], button=button))
            ForumButton.setText(item[1])  # Set the name
            ForumButton.url = item[0]
            ForumButton.name = item[1]
            self.buttons.append(ForumButton)
            self.ui.contentview.addWidget(ForumButton)

    def back(self):
        self.root.toggle_view()
        self.setParent(None)
        return

    def download(self, name, url, button):
        print(f"{name} - {url}")
        self.webtools.download_zip(url, name, self.installation_location)
        button.setStyleSheet("background-color: green")
        self.back()
