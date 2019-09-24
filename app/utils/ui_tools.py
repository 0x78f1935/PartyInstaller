from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)
from functools import partial
from os.path import expanduser, join
import webbrowser

class UITools(object):
    def __init__(self):
        print(" * UI Tools initialized ...")
        self.row_margin = (-1, 60, -1, -1)

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
        return join(self.find_my_document_folder(), 'Documents', 'Eek', 'House Party', 'Stories')