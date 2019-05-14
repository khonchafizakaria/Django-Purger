# -*- coding: utf-8 -*-
#
#!/bin/bash
#
# Form implementation generated from reading ui file 'main_0.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import os
import sys
import shutil
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets

PY_Version = 'python3'

class Ui_Main_0(QtWidgets.QMainWindow):
 
    def __init__(self):
        super(Ui_Main_0, self).__init__()
        #qtRectangle = self.frameGeometry()
        #centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        #qtRectangle.moveCenter(centerPoint)
        #self.move(qtRectangle.topLeft())
        self.setupUi(self)

    def setupUi(self, Main_0):
        Main_0.setObjectName("Main_0")
        Main_0.resize(926, 564)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("win_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main_0.setWindowIcon(icon)
        Main_0.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(Main_0)
        self.centralwidget.setObjectName("centralwidget")
        self.cw_gl = QtWidgets.QGridLayout(self.centralwidget)
        self.cw_gl.setObjectName("cw_gl")
        self.dir_wget = QtWidgets.QWidget(self.centralwidget)
        self.dir_wget.setObjectName("dir_wget")
        self.gridLayout = QtWidgets.QGridLayout(self.dir_wget)
        self.gridLayout.setObjectName("gridLayout")
        self.cw_gl.addWidget(self.dir_wget, 9, 3, 2, 1)
        self.reset_hl = QtWidgets.QHBoxLayout()
        self.reset_hl.setObjectName("reset_hl")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.reset_hl.addItem(spacerItem)
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.reset_btn.setFont(font)
        self.reset_btn.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_btn.setIcon(icon1)
        self.reset_btn.setIconSize(QtCore.QSize(20, 20))
        self.reset_btn.setDefault(False)
        self.reset_btn.setFlat(False)
        self.reset_btn.setObjectName("reset_btn")
        self.reset_hl.addWidget(self.reset_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.reset_hl.addItem(spacerItem1)
        self.cw_gl.addLayout(self.reset_hl, 3, 0, 1, 3)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.app_gb = QtWidgets.QGroupBox(self.frame)
        self.app_gb.setStyleSheet("")
        self.app_gb.setObjectName("app_gb")
        self.da_gb = QtWidgets.QVBoxLayout(self.app_gb)
        self.da_gb.setObjectName("da_gb")
        self.bd_le = QtWidgets.QLineEdit(self.app_gb)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bd_le.setFont(font)
        self.bd_le.setStyleSheet("background-color: rgb(0, 0, 0);""color: rgb(255, 255, 255);")
        self.bd_le.setClearButtonEnabled(True)
        self.bd_le.setObjectName("bd_le")
        self.da_gb.addWidget(self.bd_le)
        self.bd_btn = QtWidgets.QPushButton(self.app_gb)
        self.bd_btn.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bd_btn.setFont(font)
        self.bd_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("loop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bd_btn.setIcon(icon2)
        self.bd_btn.setIconSize(QtCore.QSize(16, 16))
        self.bd_btn.setObjectName("bd_btn")
        self.da_gb.addWidget(self.bd_btn)
        self.app_gb_ahl = QtWidgets.QVBoxLayout()
        self.app_gb_ahl.setObjectName("app_gb_ahl")
        self.da_gb.addLayout(self.app_gb_ahl)
        self.app_gb_hl0 = QtWidgets.QHBoxLayout()
        self.app_gb_hl0.setObjectName("app_gb_hl0")
        self.select_btn = QtWidgets.QPushButton(self.app_gb)
        self.select_btn.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.select_btn.setFont(font)
        self.select_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_btn.setIcon(icon3)
        self.select_btn.setObjectName("select_btn")
        self.app_gb_hl0.addWidget(self.select_btn)
        self.deselect_btn = QtWidgets.QPushButton(self.app_gb)
        self.deselect_btn.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.deselect_btn.setFont(font)
        self.deselect_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("uncheck.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deselect_btn.setIcon(icon4)
        self.deselect_btn.setObjectName("deselect_btn")
        self.app_gb_hl0.addWidget(self.deselect_btn)
        self.da_gb.addLayout(self.app_gb_hl0)
        self.push_hl = QtWidgets.QHBoxLayout()
        self.push_hl.setObjectName("push_hl")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.push_hl.addItem(spacerItem2)
        self.push_btn = QtWidgets.QPushButton(self.app_gb)
        self.push_btn.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.push_btn.setFont(font)
        self.push_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("push.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_btn.setIcon(icon5)
        self.push_btn.setObjectName("push_btn")
        self.push_hl.addWidget(self.push_btn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.push_hl.addItem(spacerItem3)
        self.da_gb.addLayout(self.push_hl)
        self.gridLayout_2.addWidget(self.app_gb, 0, 2, 1, 1)
        self.cw_gb = QtWidgets.QGroupBox(self.frame)
        self.cw_gb.setFlat(False)
        self.cw_gb.setObjectName("cw_gb")
        self.cw_gb_gl = QtWidgets.QGridLayout(self.cw_gb)
        self.cw_gb_gl.setObjectName("cw_gb_gl")
        self.venv_yes_radio = QtWidgets.QRadioButton(self.cw_gb)
        self.venv_yes_radio.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.venv_yes_radio.setFont(font)
        self.venv_yes_radio.setObjectName("venv_yes_radio")
        self.cw_gb_gl.addWidget(self.venv_yes_radio, 6, 1, 1, 1)
        self.venv_no_radio = QtWidgets.QRadioButton(self.cw_gb)
        self.venv_no_radio.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.venv_no_radio.setFont(font)
        self.venv_no_radio.setChecked(True)
        self.venv_no_radio.setObjectName("venv_no_radio")
        self.cw_gb_gl.addWidget(self.venv_no_radio, 6, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.cw_gb)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cw_gb_gl.addWidget(self.label, 6, 0, 1, 1)
        self.migration_btn = QtWidgets.QPushButton(self.cw_gb)
        self.migration_btn.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.migration_btn.setFont(font)
        self.migration_btn.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("migrate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.migration_btn.setIcon(icon6)
        self.migration_btn.setObjectName("migration_btn")
        self.cw_gb_gl.addWidget(self.migration_btn, 8, 0, 1, 3)
        self.purge_btn = QtWidgets.QPushButton(self.cw_gb)
        self.purge_btn.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.purge_btn.setFont(font)
        self.purge_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("purge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.purge_btn.setIcon(icon7)
        self.purge_btn.setObjectName("purge_btn")
        self.cw_gb_gl.addWidget(self.purge_btn, 4, 0, 1, 3)
        self.venv_level_lb = QtWidgets.QLabel(self.cw_gb)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.venv_level_lb.setFont(font)
        self.venv_level_lb.setObjectName("venv_level_lb")
        self.cw_gb_gl.addWidget(self.venv_level_lb, 7, 0, 1, 1)
        self.venv_level_sb = QtWidgets.QSpinBox(self.cw_gb)
        self.venv_level_sb.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.venv_level_sb.setFont(font)
        self.venv_level_sb.setMinimum(-10)
        self.venv_level_sb.setMaximum(-2)
        self.venv_level_sb.setProperty("value", -2)
        self.venv_level_sb.setObjectName("venv_level_sb")
        self.cw_gb_gl.addWidget(self.venv_level_sb, 7, 1, 1, 1)
        self.gridLayout_2.addWidget(self.cw_gb, 1, 2, 1, 1)
        self.treeView = QtWidgets.QTreeView(self.frame)
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath('')
        self.model.setFilter(QtCore.QDir.AllDirs)
        self.treeView.setModel(self.model)
        self.treeView.setColumnHidden(1, True)
        self.treeView.setColumnHidden(2, True)
        self.treeView.setColumnHidden(3, True)
        self.treeView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.treeView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.treeView.setObjectName("treeView")
        self.gridLayout_2.addWidget(self.treeView, 0, 0, 2, 1)
        self.cw_gl.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.console_gl = QtWidgets.QGridLayout()
        self.console_gl.setObjectName("console_gl")
        self.clear_btn = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.clear_btn.setFont(font)
        self.clear_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_btn.setIcon(icon8)
        self.clear_btn.setObjectName("clear_btn")
        self.console_gl.addWidget(self.clear_btn, 4, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.console_gl.addItem(spacerItem4, 4, 0, 1, 1)
        self.console_log = QtWidgets.QTextEdit(self.frame_2)
        self.console_log.setStyleSheet("background-color: rgb(0, 0, 0);""color: rgb(255, 255, 255);")
        self.console_log.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.console_log.setReadOnly(True)
        self.console_log.setObjectName("console_log")
        self.console_gl.addWidget(self.console_log, 3, 0, 1, 2)
        self.gridLayout_3.addLayout(self.console_gl, 1, 0, 1, 1)
        self.cw_gl.addWidget(self.frame_2, 0, 2, 1, 1)
        self.venv_detail = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.venv_detail.setFont(font)
        self.venv_detail.setObjectName("venv_detail")
        self.cw_gl.addWidget(self.venv_detail, 9, 0, 1, 3)
        Main_0.setCentralWidget(self.centralwidget)
        self.dp_statusbar = QtWidgets.QStatusBar(Main_0)
        self.dp_statusbar.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.dp_statusbar.setObjectName("dp_statusbar")
        Main_0.setStatusBar(self.dp_statusbar)

        self.retranslateUi(Main_0)
        self.venv_yes_radio.toggled['bool'].connect(self.venv_level_sb.setEnabled)
        self.bd_le.textChanged.connect(self.enablebtn)
        QtCore.QMetaObject.connectSlotsByName(Main_0)
        Main_0.setTabOrder(self.treeView, self.bd_le)
        Main_0.setTabOrder(self.bd_le, self.bd_btn)
        Main_0.setTabOrder(self.bd_btn, self.select_btn)
        Main_0.setTabOrder(self.select_btn, self.deselect_btn)
        Main_0.setTabOrder(self.deselect_btn, self.push_btn)
        Main_0.setTabOrder(self.push_btn, self.purge_btn)
        Main_0.setTabOrder(self.purge_btn, self.venv_yes_radio)
        Main_0.setTabOrder(self.venv_yes_radio, self.venv_no_radio)
        Main_0.setTabOrder(self.venv_no_radio, self.migration_btn)
        Main_0.setTabOrder(self.migration_btn, self.console_log)
        Main_0.setTabOrder(self.console_log, self.clear_btn)
        Main_0.setTabOrder(self.clear_btn, self.reset_btn)
    
        self.treeView.doubleClicked.connect(self.on_treeView_clicked)
        self.bd_btn.clicked.connect(self.loop)
        self.select_btn.clicked.connect(self.select_all)
        self.deselect_btn.clicked.connect(self.deselect_all)
        self.push_btn.clicked.connect(self.target_folders)
        self.purge_btn.clicked.connect(self.purge_cache_migration)
        self.migration_btn.clicked.connect(self.run_migration)
        self.clear_btn.clicked.connect(self.clear_console)
        self.reset_btn.clicked.connect(self.reset_gui)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())
        filePath = self.model.filePath(indexItem)
        self.bd_le.setText(filePath)

    @QtCore.pyqtSlot(str)
    def enablebtn(self):
        bd = self.bd_le.text()
        if len(bd) > 0:
            self.purge_btn.setEnabled(True)
            self.migration_btn.setEnabled(True)
            self.push_btn.setEnabled(True)
            self.bd_btn.setEnabled(True)
            self.select_btn.setEnabled(True)
            self.deselect_btn.setEnabled(True)
            self.venv_yes_radio.setEnabled(True)
            self.venv_no_radio.setEnabled(True)
        else:
            self.purge_btn.setEnabled(False)
            self.migration_btn.setEnabled(False)
            self.push_btn.setEnabled(False)
            self.bd_btn.setEnabled(False)
            self.select_btn.setEnabled(False)
            self.deselect_btn.setEnabled(False)
            self.venv_yes_radio.setEnabled(False)
            self.venv_no_radio.setEnabled(False)

    def target_folders(self):
        layout = self.app_gb_ahl
        targets = self.console_log
        targets.clear()
        path = self.bd_le.text()

        widgets = [layout.itemAt(i).widget() for i in range(layout.count())]
        for widget in widgets:
            if widget.isChecked():
                t = widget.text()
                txt = t.replace('&', '')
                cache = '{}/{}/{}'.format(path, txt, '__pycache__')
                migr = '{}/{}/{}'.format(path, txt, 'migrations')
                targets.append(cache)
                targets.append(migr)

    def loop(self):
        layout = self.app_gb_ahl
        path = self.bd_le.text()

        if layout.count() > 0:
            for widget in reversed(range(layout.count())):
                layout.itemAt(widget).widget().close()

        try:
            folders = os.listdir(path)
            for obj in folders:
                if obj.endswith('.py') or obj.endswith('.sqlite3') or obj == '.vscode':
                    folders.remove(obj)

            for folder in folders:
                layout.addWidget(QtWidgets.QCheckBox(folder))

        except Exception as e:
            errorReply = QtWidgets.QMessageBox.information(self, 'Error', str(e), QtWidgets.QMessageBox.Ok)
            if errorReply == QtWidgets.QMessageBox.Ok:
                pass

    def select_all(self):
        layout = self.app_gb_ahl
        widgets = [layout.itemAt(i).widget() for i in range(layout.count())]
        for widget in widgets:
            if isinstance(widget, QtWidgets.QCheckBox):
                widget.setChecked(True)

    def deselect_all(self):
        layout = self.app_gb_ahl
        widgets = [layout.itemAt(i).widget() for i in range(layout.count())]
        for widget in widgets:
            if isinstance(widget, QtWidgets.QCheckBox):
                widget.setChecked(False)

    def purge_cache_migration(self):
        console = self.console_log
        console_log = console.toPlainText()
        target_list = console_log.split('\n')

        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText("Warning")
        msgBox.setInformativeText('Are you sure ?')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes| QtWidgets.QMessageBox.No)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.No)
        purgeReply = msgBox.exec_()

        if purgeReply == QtWidgets.QMessageBox.Yes:
            for target in target_list:
                try:
                    shutil.rmtree(target)
                    console.append('{} --- STATUS: PURGED.'.format(target))
                except Exception as e:
                    console.append(str(e))

            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Question)
            msgBox.setText("Question")
            msgBox.setInformativeText('Do you want to purge "db.sqlite3" ?')
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes| QtWidgets.QMessageBox.No)
            msgBox.setDefaultButton(QtWidgets.QMessageBox.No)
            dbReply = msgBox.exec_()

            if dbReply == QtWidgets.QMessageBox.Yes:
                try:
                    path = self.bd_le.text()
                    db_path = path+'/db.sqlite3'
                    os.unlink(db_path)
                    console.append('db.sqlite3 --- STATUS: PURGED ...\nYou can run migrations now!')
                except Exception as e:
                    console.append(str(e))

    def run_migration(self):
        console = self.console_log
        layout = self.app_gb_ahl
        path = self.bd_le.text()
        ls = path.split('/')
        venv = ls[self.venv_level_sb.value()]
        del ls[-1]
        venv_path = "/".join(x for x in ls)
        full_venv_path = venv_path+'/bin/activate'
        widgets = [layout.itemAt(i).widget() for i in range(layout.count())]

        if self.venv_yes_radio.isChecked():
            try:
                console.append('Detected Venv : {}'.format(venv))
                console.append('---RUNNING MIGRATIONS---')
                for widget in widgets:
                    if widget.isChecked():
                        t = widget.text()
                        txt = t.replace('&', '')
                        subprocess.call('source {}; cd {}; ./manage.py makemigrations {}'.format(full_venv_path, path, txt), shell=True, executable='/bin/bash')
                subprocess.call('source {}; cd {}; ./manage.py migrate'.format(full_venv_path, path), shell=True, executable='/bin/bash')
                console.append('Migrations == OK. \nThe subprocess did not return an error.\nPlease check your project folder.')

            except Exception as e:
                console.append(str(e))
        else:
            try:
                console.append('---RUNNING MIGRATIONS---')
                for widget in widgets:
                    if widget.isChecked():
                        t = widget.text()
                        txt = t.replace('&', '')
                        subprocess.call('cd {}; {} manage.py makemigrations {}'.format(path, PY_Version, txt), shell=True, executable='/bin/bash')
                subprocess.call('cd {}; {} manage.py migrate'.format(path, PY_Version), shell=True, executable='/bin/bash')
                console.append('Migrations == OK. \nThe subprocess did not return an error.\nPlease check your project folder.')
            except Exception as e:
                console.append(str(e))

    def clear_console(self):
        self.console_log.clear()

    def reset_gui(self):
        self.bd_le.clear()
        self.venv_yes_radio.setChecked(False)
        self.venv_no_radio.setChecked(True)
        self.console_log.clear()
        layout = self.app_gb_ahl

        if layout.count() > 0:
            for widget in reversed(range(layout.count())):
                layout.itemAt(widget).widget().close()

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def retranslateUi(self, Main_0):
        _translate = QtCore.QCoreApplication.translate
        Main_0.setWindowTitle(_translate("Main_0", "Django Purger"))
        self.reset_btn.setText(_translate("Main_0", "Reset"))
        self.app_gb.setTitle(_translate("Main_0", "DJANGO APPLICATION"))
        self.bd_le.setPlaceholderText(_translate("Main_0", "/path/to/your/djang_project"))
        self.bd_btn.setText(_translate("Main_0", "Loop"))
        self.select_btn.setText(_translate("Main_0", "Select All"))
        self.deselect_btn.setText(_translate("Main_0", "Deselect All"))
        self.push_btn.setText(_translate("Main_0", "Push Targets"))
        self.cw_gb.setTitle(_translate("Main_0", "ACTIONS"))
        self.venv_yes_radio.setText(_translate("Main_0", "&Yes"))
        self.venv_no_radio.setText(_translate("Main_0", "&No"))
        self.label.setText(_translate("Main_0", "Virtual Environment ?"))
        self.migration_btn.setText(_translate("Main_0", "Run Migrations"))
        self.purge_btn.setText(_translate("Main_0", "Purge Targets"))
        self.venv_level_lb.setText(_translate("Main_0", "Venv Level*"))
        self.clear_btn.setText(_translate("Main_0", "Clear"))
        self.venv_detail.setText(_translate("Main_0", "*Venv level ==  the reversed position of the virtual environment name in the path ( i;e : /home/user/Desktop/*venv*/project ), in this case the venv level == -2."))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Main_0()
    app.setWindowIcon(QtGui.QIcon('ico1.ico'))
    window.setWindowIcon(QtGui.QIcon('ico1.ico'))
    window.show()
    app.exec_()
