import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QLabel
from PyQt5.QtCore import QUrl,Qt
from PyQt5.QtGui import QDesktopServices, QPixmap
from tkinter import messagebox
import subprocess
import os

class App(QWidget):
    def __init__(self):
        super().__init__()
        QMessageBox.information(None, '注册提示', '请先注册Steam账号，如果已有账号请忽视。')
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Steam 萌新帮助工具')
        self.setGeometry(100, 100, 280, 80)

        layout = QVBoxLayout()
        layout.addStretch(1)

        self.logo = QLabel(self)
        pix = QPixmap('logo.png')
        self.logo.setPixmap(pix.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(self.logo, alignment=Qt.AlignCenter)

        self.registerButton = QPushButton('先点注册 Steam', self)
        self.registerButton.clicked.connect(self.onRegisterButtonClick)
        layout.addWidget(self.registerButton)

        # 创建一个按钮，点击时将调用steam.py
        self.button = QPushButton('点击下载 Steam', self)
        self.button.clicked.connect(self.onButtonClick)
        layout.addWidget(self.button)
        layout.addStretch(1)

        self.setLayout(layout)

        self.contactAuthorButton = QPushButton('联系作者', self)
        self.contactAuthorButton.clicked.connect(self.onContactAuthorClick)
        layout.addWidget(self.contactAuthorButton)

        self.version_label = QLabel('版本号: 24.0.0.1 作者: Cxost 后续完善', self)
        self.version_label.setAlignment(Qt.AlignBottom | Qt.AlignLeft)  # 底部对齐
        layout.addWidget(self.version_label)




    def onButtonClick(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        steam_script_path = os.path.join(current_dir, 'steam.py')

        #  result = subprocess.call(['/usr/bin/python3', steam_script_path])

        result = subprocess.call(['python', steam_script_path])

        steam_exe_path = os.path.join(current_dir, 'steam.exe')

        if result == 0 and os.path.exists(steam_exe_path):
            QMessageBox.information(self, '下载器', 'Steam 下载完成 请手动启动steam进行安装!')
            #  directory = os.path.dirname(steam_exe_path)             QDesktopServices.openUrl(QUrl.fromLocalFile(directory))
            #打开steam.exe
            subprocess.Popen(steam_exe_path)

        else:
            QMessageBox.information(self, '下载器', 'Steam 下载失败，请重试!')



    def onRegisterButtonClick(self):

        main_url = 'https://store.steampowered.com/join/?&snr=1_60_4__62'
        QDesktopServices.openUrl(QUrl(main_url))

        reply = QMessageBox.question(self, '注册', '是否能访问？',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            pass 
        elif reply == QMessageBox.No:
            steam_tools_url = 'https://gitee.com/rmbgame/SteamTools/releases/tag/3.0.0-rc.9'
            QDesktopServices.openUrl(QUrl(steam_tools_url))

            QMessageBox.information(self, '加速器下载提示', '请手动下载exe后缀文件')

    def onContactAuthorClick(self):
        author_email = 'yiyuan.cn.official@gmail.com'  
        QMessageBox.information(self, '联系作者', f'作者邮箱: {author_email}')

def main():
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
