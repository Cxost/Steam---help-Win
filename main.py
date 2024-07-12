import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QLabel
from PyQt5.QtCore import QUrl,Qt
from PyQt5.QtGui import QDesktopServices, QPixmap
from tkinter import messagebox
import subprocess
import os
class O00000O00OOO0OO0OOO0(QWidget):
    def __init__(self):
        super().__init__()
        QMessageBox.information(None, '注册提示', '请先注册Steam账号，如果已有账号请忽视。')
        self.OO0O0O0OO00OO0O0OOOOOO()
    def OO0O0O0OO00OO0O0OOOOOO(self):
        self.setWindowTitle('Steam 萌新帮助工具')
        self.setGeometry(100, 100, 280, 80)
        layout = QVBoxLayout()
        layout.addStretch(1)
        self.logo = QLabel(self)
        pix = QPixmap('images/logo.png')  
        self.logo.setPixmap(pix.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(self.logo, alignment=Qt.AlignCenter)
        self.registerButton = QPushButton('先点注册 Steam', self)
        self.registerButton.clicked.connect(self.OO000OOOO00OO00OO0OOOO)
        layout.addWidget(self.registerButton)
        self.button = QPushButton('点击下载 Steam', self)
        self.button.clicked.connect(self.O0OOOOOOO00OO0O00O0OO0)
        layout.addWidget(self.button)
        layout.addStretch(1)
        self.setLayout(layout)
        self.contactAuthorButton = QPushButton('联系作者', self)
        self.contactAuthorButton.clicked.connect(self.OO00OO0OO0000O000O0OO0)
        layout.addWidget(self.contactAuthorButton)
        self.version_label = QLabel('版本号: 24.0.0.1 作者: Cxost 后续完善', self)
        self.version_label.setAlignment(Qt.AlignBottom | Qt.AlignLeft)  
        layout.addWidget(self.version_label)
    def O0OOOOOOO00OO0O00O0OO0(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        steam_script_path = os.path.join(current_dir, 'dow', 'steam.py')
        result = subprocess.call(['python', steam_script_path])
        steam_exe_path = os.path.join(current_dir, 'steam.exe')
        if result == 0 and os.path.exists(steam_exe_path):
            QMessageBox.information(self, '下载器', 'Steam 下载完成 请手动启动steam进行安装!')
            subprocess.Popen(steam_exe_path)
        else:
            QMessageBox.information(self, '下载器', 'Steam 下载失败，请重试!')
    def OO000OOOO00OO00OO0OOOO(self):
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
    def OO00OO0OO0000O000O0OO0(self):
        author_email = 'yiyaun.cn.official@gmail.com'  
        QMessageBox.information(self, '联系作者', f'作者邮箱: {author_email}')
def OO00OO0OO00OOOOOOO00O0():
    app = QApplication(sys.argv)
    ex = O00000O00OOO0OO0OOO0()
    ex.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    OO00OO0OO00OOOOOOO00O0()
