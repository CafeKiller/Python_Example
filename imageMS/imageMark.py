import os
import os.path
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QFontDialog, QMainWindow
from PyQt5.QtGui import QFontMetrics, QFontInfo
from PIL import Image, ImageDraw, ImageFont, ImageEnhance


class Ui_MarkWindow(QMainWindow):
    def __init__(self):
        super(Ui_MarkWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)  # 只显示关闭按钮
        self.setupUi(self)  # 初始化窗体设置

    # 自动生成的代码，用来对窗体进行设置
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(578, 418)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 设置图片显示列表
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 141, 391))
        self.listWidget.setObjectName("listWidget")
        # 设置加载图片按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 0, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(150, 30, 421, 151))
        self.groupBox.setObjectName("groupBox")

        # 设置文字水印单选按钮
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.radioButton.setChecked(True)  # 默认选中
        self.radioButton.setObjectName("radioButton")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 50, 54, 16))
        self.label.setObjectName("label")

        # 设置要输入水印文字的文本框
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(90, 50, 241, 20))
        self.lineEdit.setObjectName("lineEdit")

        # 设置“字体设置”按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 50, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        # 设置图片水印单选按钮
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 80, 91, 16))
        self.radioButton_2.setChecked(False)  # 默认不选中
        self.radioButton_2.setObjectName("radioButton_2")

        # 设置选择水印图片按钮
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 110, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 54, 16))
        self.label_2.setObjectName("label_2")

        # 设置显示水印图片路径的文本框
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 110, 241, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(150, 190, 421, 71))
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(270, 31, 54, 21))
        self.label_3.setObjectName("label_3")

        # 设置水印位置选择框
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(330, 30, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem('左上角')
        self.comboBox.addItem('右上角')
        self.comboBox.addItem('左下角')
        self.comboBox.addItem('右下角')
        self.comboBox.addItem('居中位置')
        self.comboBox.setCurrentIndex(0)  # 设置默认选择第一项

        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 51, 21))
        self.label_4.setObjectName("label_4")

        # 设置水印透明度的滑动条
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(70, 30, 181, 22))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(150, 270, 421, 71))
        self.groupBox_3.setObjectName("groupBox_3")

        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 61, 21))
        self.label_6.setObjectName("label_6")

        # 设置显示保存路径的文本框
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 30, 241, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        # 设置选择图片保存路径的按钮
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 30, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        # 设置执行按钮
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(480, 350, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")

        MainWindow.setCentralWidget(self.centralwidget)
        # 设置状态栏
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        self.statusBar.showMessage('准备就绪…… ')  # 设置状态栏默认值
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 自动生成的代码，用来设置窗体中控件的默认值
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图片批量添加水印"))
        self.pushButton.setText(_translate("MainWindow", "加载图片"))
        self.groupBox.setTitle(_translate("MainWindow", "水印设置"))
        self.radioButton.setText(_translate("MainWindow", "添加文字水印"))
        self.label.setText(_translate("MainWindow", "水印文字："))
        self.pushButton_2.setText(_translate("MainWindow", "字体设置"))
        self.radioButton_2.setText(_translate("MainWindow", "添加图片水印"))
        self.pushButton_3.setText(_translate("MainWindow", "浏览"))
        self.label_2.setText(_translate("MainWindow", "水印图片："))
        self.groupBox_2.setTitle(_translate("MainWindow", "透明度及位置设置"))
        self.label_3.setText(_translate("MainWindow", "水印位置："))
        self.label_4.setText(_translate("MainWindow", "透明度："))
        self.groupBox_3.setTitle(_translate("MainWindow", "路径设置"))
        self.label_6.setText(_translate("MainWindow", "保存位置："))
        self.pushButton_4.setText(_translate("MainWindow", "浏览"))
        self.pushButton_5.setText(_translate("MainWindow", "执行"))
        # 关联“加载图片”按钮的方法
        self.pushButton.clicked.connect(self.getFiles)
        # 关联“字体设置”按钮的方法
        self.pushButton_2.clicked.connect(self.setFont)
        # 关联“选择图片”按钮的方法
        self.pushButton_3.clicked.connect(self.setImg)
        # 关联“选择保存路径”按钮的方法
        self.pushButton_4.clicked.connect(self.msg)
        # 关联“执行”按钮的方法
        self.pushButton_5.clicked.connect(self.addMark)
        # 关联列表单击方法，用来预览选中的图片
        self.listWidget.itemClicked.connect(self.itemClick)

    # 设置字体
    def setFont(self):
        self.waterfont, ok = QFontDialog.getFont() # 显示字体对话框
        if ok: # 判断是否选择了字体
            self.lineEdit.setFont(self.waterfont)
            self.fontSize = QFontMetrics(self.waterfont)
            self.fontInfo = QFontInfo(self.waterfont)

    # 是否为图片
    def isImg(self, file):
        file = file.lower()
        if file == '.jpg':
            return True
        elif file == '.png':
            return True
        elif file == '.jpeg':
            return True
        elif file == '.bmp':
            return True
        else:
            return False

    # 获取所有图片
    def getFiles(self):
        try:
            # 选择图片文件夹路径
            self.img_path = QFileDialog.getExistingDirectory(None, "选择图片文件夹路径", os.getcwd())
            self.list = os.listdir(self.img_path)  # 遍历选择的文件夹
            num = 0  # 记录图片数量
            self.listWidget.clear()  # 清空列表项
            for i in range(0, len(self.list)):  # 遍历图片列表
                filepath = os.path.join(self.img_path, self.list[i])  # 记录遍历到的文件名
                if os.path.isfile(filepath):  # 判断是否为文件
                    imgType = os.path.splitext(filepath)[1]  # 获取扩展名
                    if self.isImg(imgType):  # 判断是否为图片
                        num += 1  # 数量加1
                        self.item = QtWidgets.QListWidgetItem(self.listWidget)  # 创建列表项
                        self.item.setText(self.list[i])  # 显示图片列表
            self.statusBar.showMessage('共有图片 ' + str(num) + ' 张')  # 显示图片总数
        except  Exception:
            QMessageBox.warning(None, "警告", '请选择一个有效路径……', QMessageBox.Ok)

    # 预览图片
    def itemClick(self, item):
        os.startfile(self.img_path + "\\" + item.text())

    # 选择水印图片
    def setImg(self):
        try:
            # waterimg即为选择的水印图片，第二形参为对话框标题，第三个为对话框打开后默认的路径
            self.waterimg = QFileDialog.getOpenFileName(None, "选择水印图片", "C:\\", "图片文件(*.jpeg;*.png;*.jpg;*.bmp)")
            self.lineEdit_2.setText(self.waterimg[0]) # 显示选择的水印图片
        except Exception as e:
            print(e)
