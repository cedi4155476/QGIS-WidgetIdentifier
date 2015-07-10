# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cch/.qgis2/python/plugins/WidgetIdentifier/widget_identifier_dialog_base.ui'
#
# Created: Fri Jul 10 14:52:30 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_WidgetIdentifierDialogBase(object):
    def setupUi(self, WidgetIdentifierDialogBase):
        WidgetIdentifierDialogBase.setObjectName(_fromUtf8("WidgetIdentifierDialogBase"))
        WidgetIdentifierDialogBase.resize(99, 32)
        WidgetIdentifierDialogBase.setMaximumSize(QtCore.QSize(300, 100))
        self.verticalLayout = QtGui.QVBoxLayout(WidgetIdentifierDialogBase)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.identifybutton = QtGui.QPushButton(WidgetIdentifierDialogBase)
        self.identifybutton.setObjectName(_fromUtf8("identifybutton"))
        self.verticalLayout.addWidget(self.identifybutton)

        self.retranslateUi(WidgetIdentifierDialogBase)
        QtCore.QMetaObject.connectSlotsByName(WidgetIdentifierDialogBase)

    def retranslateUi(self, WidgetIdentifierDialogBase):
        WidgetIdentifierDialogBase.setWindowTitle(_translate("WidgetIdentifierDialogBase", "Widget Identifier", None))
        self.identifybutton.setText(_translate("WidgetIdentifierDialogBase", "Identify", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WidgetIdentifierDialogBase = QtGui.QDialog()
    ui = Ui_WidgetIdentifierDialogBase()
    ui.setupUi(WidgetIdentifierDialogBase)
    WidgetIdentifierDialogBase.show()
    sys.exit(app.exec_())

