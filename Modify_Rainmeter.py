import sys
import os
import time
from PyQt5.QtWidgets import QApplication, QGridLayout, QFileDialog, QMainWindow
from PyQt5.QtWidgets import QColorDialog, QPushButton, QWidget
from PyQt5.QtWidgets import QLineEdit, QSizePolicy, QFontDialog
from PyQt5 import QtGui
from PyQt5.QtCore import QSettings
# Function made separated from the main app
from app import modify_files

# Put your path to the skins in here


# Main Window config


class ColorWheel(QMainWindow, object):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.setLayout(self.grid)
        self.icon = QtGui.QIcon(
            r'Rainmeter_Code\\Principal\\Color_Wheel.png')
        self.setWindowIcon(self.icon)
        self.setWindowTitle('Color')
        self.setFixedSize(600, 300)
        self.setStyleSheet(
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:2, stop:0 #21002c, stop:1 #000000)")

        self.grid.setVerticalSpacing(1)
        self.grid.setContentsMargins(0, 15, 0, 0)


# Display where the rgb coordinates are reinformed

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 2, 10)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '*{border: 1px black solid; border-radius: 12px;'
            'background: #16001e; color: white; font-size: 50px;}'
        )

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHeightForWidth(
            self.display.sizePolicy().hasHeightForWidth())
        self.display.setSizePolicy(sizePolicy)

        # Buttons in the Main Window
        self.btn = QPushButton('Open Folder Selection')
        self.btn.setStyleSheet(
            "QPushButton{"
            "border: 2px solid black; font-size: 20px;"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #39004d, stop:1 #000000);"
            "color: #f2f2f2;"
            "border-radius: 2px;"
            "}"
            "QPushButton:hover {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #5e0080, stop:1 #000000);"
            "color: #fff;"
            "}"
            "QPushButton:pressed {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #4b0066, stop:1 #000000);"
            "color: #cccccc;"
            "}"
        )
        self.grid.addWidget(self.btn, 2, 3, 2, 4)
        self.btn.clicked.connect(self.SetupWindow)

    # Buttons in the Main Window
        self.btn = QPushButton('Color Selection')
        self.btn.setStyleSheet(
            "QPushButton{"
            "border: 2px solid black; font-size: 25px;"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #4d0000, stop:1 #000000);"
            "color: #d9d9d9;"
            "border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #660000, stop:1 #000000);"
            "color: #fff;"
            "}"
            "QPushButton:pressed {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #330000, stop:1 #000000);"
            "color: #cccccc;"
            "}"
        )
        self.grid.addWidget(self.btn, 7, 0, 2, 5)
        self.btn.clicked.connect(self.color_picker)

        self.btnSelectPathTD = QPushButton('Change Time color')
        self.btnSelectPathTD.setStyleSheet(
            "QPushButton{"
            "border: 2px solid black; font-size: 25px;"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #4d0000, stop:1 #000000);"
            "color: #d9d9d9;"
            "border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #660000, stop:1 #000000);"
            "color: #fff;"
            "}"
            "QPushButton:pressed {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #330000, stop:1 #000000);"
            "color: #cccccc;"
            "}"
        )
        self.grid.addWidget(self.btnSelectPathTD, 10, 0, 2, 5)
        self.btnSelectPathTD.clicked.connect(self.path_selector_TD)

        self.btnSelectPathSYS = QPushButton('Change System color')
        self.btnSelectPathSYS.setStyleSheet(
            "QPushButton{"
            "border: 2px solid black; font-size: 25px;"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #4d0000, stop:1 #000000);"
            "color: #d9d9d9;"
            "border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #660000, stop:1 #000000);"
            "color: #fff;"
            "}"
            "QPushButton:pressed {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #330000, stop:1 #000000);"
            "color: #cccccc;"
            "}"
        )
        self.grid.addWidget(self.btnSelectPathSYS, 10, 5, 2, 5)
        self.btnSelectPathSYS.clicked.connect(self.path_selector_System)
        self.setCentralWidget(self.cw)

        self.btnSelectPathTD_Font = QPushButton('Change Font Color')
        self.btnSelectPathTD_Font.setStyleSheet(
            "QPushButton{"
            "border: 2px solid black; font-size: 25px;"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #4d0000, stop:1 #000000);"
            "color: #d9d9d9;"
            "border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #660000, stop:1 #000000);"
            "color: #fff;"
            "}"
            "QPushButton:pressed {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #330000, stop:1 #000000);"
            "color: #cccccc;"
            "}"
        )
        self.grid.addWidget(self.btnSelectPathTD_Font, 16, 0, 2, 5)
        self.btnSelectPathTD_Font.clicked.connect(self.font_selection_TD)

        self.btnSetGradient = QPushButton('Set Gradient')
        self.btnSetGradient.setStyleSheet(
            "QPushButton{"
            "border: 2px solid black; font-size: 25px;"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #4d0000, stop:1 #000000);"
            "color: #d9d9d9;"
            "border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #660000, stop:1 #000000);"
            "color: #fff;"
            "}"
            "QPushButton:pressed {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #330000, stop:1 #000000);"
            "color: #cccccc;"
            "}"
        )
        self.grid.addWidget(self.btnSetGradient, 16, 5, 2, 5)
        self.btnSetGradient.clicked.connect(self.set_gradient)

        self.btnSetFont = QPushButton('Select Font')
        self.btnSetFont.setStyleSheet(
            "QPushButton{"
            "border: 2px solid black; font-size: 25px;"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #4d0000, stop:1 #000000);"
            "color: #d9d9d9;"
            "border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #660000, stop:1 #000000);"
            "color: #fff;"
            "}"
            "QPushButton:pressed {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #330000, stop:1 #000000);"
            "color: #cccccc;"
            "}"
        )
        self.grid.addWidget(self.btnSetFont, 7, 5, 2, 5)
        self.btnSetFont.clicked.connect(self.font_selctor)

        self.kindoflabel = QPushButton('By Gabriel A.S.')
        self.kindoflabel.setStyleSheet(
            "QPushButton{"
            "border: 0px solid black; font-size: 15px;"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #110017, stop:1 #000000);"
            "color: #fff;"
            "border-radius: 10px;"
            "}"

        )
        self.grid.addWidget(self.kindoflabel, 17, 4, 2, 2)

        self.setCentralWidget(self.cw)

# Method to get the rgb coordinates
    def color_picker(self):
        self.color = QColorDialog.getColor()
        self.selected_rgb = str(QtGui.QColor.getRgb(
            self.color))[:-6].replace('(', '')
        self.display.setText(self.selected_rgb)

# Paths in my computer
    def path_selector_TD(self):
        self.path = Setup.path_to_date
        self.section = 'Color2'
        self.modifier()

    def path_selector_System(self):
        self.path = Setup.path_to_system
        self.section = 'Color2'
        self.modifier()

    def font_selection_TD(self):
        self.path = Setup.path_to_date
        self.section = 'Color1'
        self.modifier()

# Method to apply the configurations

    def modifier(self, path=None, key=None, value=None):
        try:
            if path is None or key is None or value is None:
                modify_files(self.path, 'Variables',
                             self.section, self.selected_rgb)
            else:
                modify_files(path, 'Variables', key, value)

            time.sleep(0.5)
            os.system(
                'cmd /c "C:/Program Files/Rainmeter/Rainmeter.exe" !RefreshApp')

        except Exception as e:
            self.display.setText('Path or color not properly selected')

            print(e)


# Method to open second window for gradient selection

    def font_selctor(self):
        self.wf = FontSelectorWindow()
        self.wf.show()

# This method calls the "subclass" to open other window
    def set_gradient(self):
        self.w = GradientSelectorWindow()
        self.w.show()
        modify_files(Setup.path_to_date,
                     'MeterDate', 'inlinesetting', 'GradientColor | #Direction# | #Color2# ; 0.0 | #Color3# ; 1.0')

# This method opens a folder selection window
    def SetupWindow(self):
        self.Setup = Setup()
        self.Setup.show()


class Setup(QMainWindow, object):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.getSettingValues()

        Setup.path_to_date = self.setting_paths.value('path_to_date')
        Setup.path_to_system = self.setting_paths.value('path_to_system')
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.icon = QtGui.QIcon(r'Rainmeter_Code\Principal\Color_Wheel.png')
        self.setWindowIcon(self.icon)
        self.setWindowTitle('First Time Huh?')
        self.setFixedSize(350, 100)

        self.btnDir = QPushButton('Open Folders')
        self.grid.addWidget(self.btnDir, 1, 1, 1, 1)
        self.btnDir.clicked.connect(self.getDirectory)

        self.setCentralWidget(self.cw)

# Folder Location Setup

    def getSettingValues(self):
        self.setting_paths = QSettings('Modify Rainmeter', 'Path')

    def getDirectory(self):
        response = QFileDialog.getExistingDirectory(
            self,
            caption="Select Folder"
        )

        updated_path_to_date = str(
            response)+r'\Skins\Ageo\Time and Date\Time and Date.ini'

        updated_path_to_system = str(
            response) + r'\Skins\Minimalist 2\System\System.ini'

        self.setting_paths.setValue('path_to_date', updated_path_to_date)
        self.setting_paths.setValue(
            'path_to_system', updated_path_to_system)


# "Subclass" to open another window
class FontSelectorWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.icon = QtGui.QIcon(
            r'Rainmeter_Code\Principal\Color_Wheel.png')
        self.setWindowIcon(self.icon)
        self.setWindowTitle('Change Font')
        self.setFixedSize(400, 200)
        self.setStyleSheet(
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:2, stop:0 #21002c, stop:1 #000000)")
# buttons
        self.btnPathDayNum = QPushButton('Change Num font')
        self.btnPathDayNum.setStyleSheet(
            "QPushButton{"
            "border: 2px solid black; font-size: 25px;"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #4d0000, stop:1 #000000);"
            "color: #d9d9d9;"
            "border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #660000, stop:1 #000000);"
            "color: #fff;"
            "}"
            "QPushButton:pressed {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #330000, stop:1 #000000);"
            "color: #cccccc;"
            "}"
        )
        self.grid.addWidget(self.btnPathDayNum, 1, 0, 5, 4)
        self.btnPathDayNum.clicked.connect(self.font_choice_num)

        self.btnPathMonth = QPushButton('Change Letter Font')
        self.btnPathMonth.setStyleSheet(
            "QPushButton{"
            "border: 2px solid black; font-size: 25px;"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #4d0000, stop:1 #000000);"
            "color: #d9d9d9;"
            "border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #660000, stop:1 #000000);"
            "color: #fff;"
            "}"
            "QPushButton:pressed {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #330000, stop:1 #000000);"
            "color: #cccccc;"
            "}"
        )
        self.grid.addWidget(self.btnPathMonth, 5, 0, 5, 4)
        self.btnPathMonth.clicked.connect(self.font_choice_month)

        self.btnPathSystem = QPushButton('Change System Font')
        self.btnPathSystem.setStyleSheet(
            "QPushButton{"
            "border: 2px solid black; font-size: 25px;"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #4d0000, stop:1 #000000);"
            "color: #d9d9d9;"
            "border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #660000, stop:1 #000000);"
            "color: #fff;"
            "}"
            "QPushButton:pressed {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #330000, stop:1 #000000);"
            "color: #cccccc;"
            "}"
        )
        self.grid.addWidget(self.btnPathSystem, 9, 0, 5, 4)
        self.btnPathSystem.clicked.connect(self.font_choice_sys)

        self.setCentralWidget(self.cw)

# method to change font 2
    def font_choice_month(self):
        font, valid = QFontDialog.getFont()

        if valid:
            QtGui.QFontInfo(font)
            self.selectedfontM = font.toString()[0:-28].replace(',', '')

        try:
            modify_files(Setup.path_to_date,
                         'Variables',
                         'font2', self.selectedfontM)
            time.sleep(0.2)
            os.system(
                'cmd /c "C:/Program Files/Rainmeter/Rainmeter.exe" !RefreshApp')

        except Exception as e:
            print(e)

# method to change font 1
    def font_choice_num(self):
        font, valid = QFontDialog.getFont()

        if valid:
            QtGui.QFontInfo(font)
            self.selectedfontD = font.toString()[0:-27].replace(',', '')

        try:
            modify_files(Setup.path_to_date,
                         'Variables',
                         'font1', self.selectedfontD)
            time.sleep(0.2)
            os.system(
                'cmd /c "C:/Program Files/Rainmeter/Rainmeter.exe" !RefreshApp')
            print(self.selectedfontD)

        except Exception as e:
            print(e)

    def font_choice_sys(self):
        font, valid = QFontDialog.getFont()

        if valid:
            QtGui.QFontInfo(font)
            self.selectedfontS = font.toString()[0:-27].replace(',', '')

        try:
            modify_files(Setup.path_to_system,
                         'Variables',
                         'font1', self.selectedfontS)
            time.sleep(0.2)
            os.system(
                'cmd /c "C:/Program Files/Rainmeter/Rainmeter.exe" !RefreshApp')
            print(self.selectedfontS)

        except Exception as e:
            print(e)

# "Subclass" to create another window with gradient configs


class GradientSelectorWindow(QMainWindow, object):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.icon = QtGui.QIcon(
            r'Rainmeter_Code\Principal\Color_Wheel.png')
        self.setWindowIcon(self.icon)
        self.setWindowTitle('Set Gradient')
        self.setFixedSize(400, 200)
        self.setStyleSheet(
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:2, stop:0 #21002c, stop:1 #000000)")
# Buttons that sets directions to the gradient
        self.btnTopTB = QPushButton('Top to Bottom')
        self.btnTopTB.setStyleSheet(
            "QPushButton{"
            "border: 2px solid black; font-size: 25px;"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #4d0000, stop:1 #000000);"
            "color: #d9d9d9;"
            "border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #660000, stop:1 #000000);"
            "color: #fff;"
            "}"
            "QPushButton:pressed {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #330000, stop:1 #000000);"
            "color: #cccccc;"
            "}"
        )
        self.grid.addWidget(self.btnTopTB, 2, 0, 5, 5)
        self.btnTopTB.clicked.connect(self.top_to_bottom)

        self.btnBotT = QPushButton('Bottom to Top')
        self.btnBotT.setStyleSheet(
            "QPushButton{"
            "border: 2px solid black; font-size: 25px;"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #4d0000, stop:1 #000000);"
            "color: #d9d9d9;"
            "border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #660000, stop:1 #000000);"
            "color: #fff;"
            "}"
            "QPushButton:pressed {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #330000, stop:1 #000000);"
            "color: #cccccc;"
            "}"
        )
        self.grid.addWidget(self.btnBotT, 2, 5, 5, 5)
        self.btnBotT.clicked.connect(self.bottom_to_top)

        self.btnLeftRight = QPushButton('Left to Right')
        self.btnLeftRight.setStyleSheet(
            "QPushButton{"
            "border: 2px solid black; font-size: 25px;"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #4d0000, stop:1 #000000);"
            "color: #d9d9d9;"
            "border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #660000, stop:1 #000000);"
            "color: #fff;"
            "}"
            "QPushButton:pressed {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #330000, stop:1 #000000);"
            "color: #cccccc;"
            "}"
        )
        self.grid.addWidget(self.btnLeftRight, 5, 0, 5, 5)
        self.btnLeftRight.clicked.connect(self.left_to_right)

        self.btnRightLeft = QPushButton('Right to Left')
        self.btnRightLeft.setStyleSheet(
            "QPushButton{"
            "border: 2px solid black; font-size: 25px;"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #4d0000, stop:1 #000000);"
            "color: #d9d9d9;"
            "border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #660000, stop:1 #000000);"
            "color: #fff;"
            "}"
            "QPushButton:pressed {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #330000, stop:1 #000000);"
            "color: #cccccc;"
            "}"
        )
        self.grid.addWidget(self.btnRightLeft, 5, 5, 5, 5)
        self.btnRightLeft.clicked.connect(self.right_to_left)

        self.btnNoGrad = QPushButton('None')
        self.btnNoGrad.setStyleSheet(
            "QPushButton{"
            "border: 2px solid black; font-size: 25px;"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #4d0000, stop:1 #000000);"
            "color: #d9d9d9;"
            "border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #660000, stop:1 #000000);"
            "color: #fff;"
            "}"
            "QPushButton:pressed {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #330000, stop:1 #000000);"
            "color: #cccccc;"
            "}"
        )
        self.grid.addWidget(self.btnNoGrad, 7, 3, 5, 4)
        self.btnNoGrad.clicked.connect(self.no_grad)

# Select the gradient final color(will combine with main app color)
        self.btnGradColor = QPushButton('Select Color')
        self.btnGradColor.setStyleSheet(
            "QPushButton{"
            "border: 2px solid black; font-size: 25px;"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #4d0000, stop:1 #000000);"
            "color: #d9d9d9;"
            "border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #660000, stop:1 #000000);"
            "color: #fff;"
            "}"
            "QPushButton:pressed {"
            "background-color: QLinearGradient(x1:0, y1:0 , x2:0, y2:1.5, stop:0 #330000, stop:1 #000000);"
            "color: #cccccc;"
            "}"
        )
        self.grid.addWidget(self.btnGradColor, 0, 3, 5, 4)
        self.btnGradColor.clicked.connect(self.grad_color)

        self.setCentralWidget(self.cw)

# Buttons methods/commands
    def grad_color(self):
        self.color = QColorDialog.getColor()
        self.selected_rgb = str(QtGui.QColor.getRgb(
            self.color))[:-6].replace('(', '')
        modify_files(Setup.path_to_date,
                     'Variables', 'Color3', self.selected_rgb)

    def top_to_bottom(self):
        self.path = Setup.path_to_date
        modify_files(self.path, 'Variables', 'Direction', '270')
        os.system(
            'cmd /c "C:/Program Files/Rainmeter/Rainmeter.exe" !RefreshApp')

    def bottom_to_top(self):
        self.path = Setup.path_to_date
        modify_files(self.path, 'Variables', 'Direction', '90')
        os.system(
            'cmd /c "C:/Program Files/Rainmeter/Rainmeter.exe" !RefreshApp')

    def left_to_right(self):
        self.path = Setup.path_to_date
        modify_files(self.path, 'Variables', 'Direction', '180')
        os.system(
            'cmd /c "C:/Program Files/Rainmeter/Rainmeter.exe" !RefreshApp')

    def right_to_left(self):
        self.path = Setup.path_to_date
        modify_files(self.path, 'Variables', 'Direction', '0')
        os.system(
            'cmd /c "C:/Program Files/Rainmeter/Rainmeter.exe" !RefreshApp')

    def no_grad(self):
        self.path = Setup.path_to_date
        modify_files(self.path, 'MeterDate', 'inlinesetting', '')
        os.system(
            'cmd /c "C:/Program Files/Rainmeter/Rainmeter.exe" !RefreshApp')
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    color = ColorWheel()
    color.show()
    app.exec_()
