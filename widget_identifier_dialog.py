# -*- coding: utf-8 -*-

"""
Module implementing WidgetIdentifierDialog.
"""

from PyQt4.QtCore import pyqtSlot, Qt
from PyQt4.QtGui import QDialog, QApplication, QCursor

from .Ui_widget_identifier_dialog_base import Ui_WidgetIdentifierDialogBase


class WidgetIdentifierDialog(QDialog, Ui_WidgetIdentifierDialogBase):
    """
    Little Dialog to get informations of widgets.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(WidgetIdentifierDialog, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setupUi(self)

    def mouseReleaseEvent(self, e):
        self.releaseMouse()
        self.setCursor(QCursor(Qt.ArrowCursor))
        pos = self.mapToGlobal(e.pos())
        
        widget = QApplication.widgetAt(pos)
        if widget:
            print (widget.metaObject().className() + ": " + widget.objectName())
        else:
            print ("No widget")

    @pyqtSlot()
    def on_identifybutton_clicked(self):
        """
        grab mouse.
        """
        self.setCursor(QCursor(Qt.WhatsThisCursor))
        self.grabMouse()
