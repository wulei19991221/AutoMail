# !/usr/bin/python3
# --coding:utf-8--
# @Author:吴磊
# @Time: 2020年05月08日17时
# @File: 邮箱密码生成器桌面版.py
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, \
    QLineEdit, QGridLayout, QComboBox, QMessageBox
from PyQt5.QtGui import QIntValidator, QIcon
from sys import argv, exit
import random


class MailGenerate(QWidget):
    def __init__(self):
        super(MailGenerate, self).__init__()
        self.lib = self.add_lib()
        self.setWindowIcon(QIcon('mail.ico'))
        self.initUI()
        self.num1 = 8
        self.num2 = 8
        self.type = '@google.com'

    # create a lib to save characters and numbers
    def add_lib(self):
        # 新建一个字符列表
        lib = []
        # 添加数字集合
        lib.extend(i for i in range(0, 20))
        # 添加大写字母 64-90
        lib.extend(chr(i) for i in range(65, 91))
        # 添加小写字母 97-122
        lib.extend(chr(i) for i in range(97, 123))
        return lib

    def initUI(self):
        layout = QGridLayout()
        # self.resize(800, 600)
        self.setWindowTitle('账号密码生成器')
        # 行编辑框: 账号
        self.line = QLineEdit()
        self.line.setPlaceholderText('账号前缀生成位数,默认8位')
        intvali = QIntValidator(8, 12)
        self.line.setValidator(intvali)
        # 行编辑框: 密码
        self.line2 = QLineEdit()
        self.line2.setPlaceholderText('密码生成位数,默认8位')
        self.line2.setValidator(intvali)
        # 列表框: 邮箱类型
        self.combox = QComboBox()
        self.combox.addItems(['选择邮箱类型', '@google.com', '@qq.com', '@163.com'])
        # 确认按钮
        self.btn = QPushButton('确认')
        # 读取本地已经生成的账号密码: 文本框
        self.tEdit = QTextEdit()
        self.tEdit.setReadOnly(True)
        # 清除所有内容: 清除按钮
        self.btn2 = QPushButton('清除所有')
        # 查看历史记录: 按钮
        self.btn3 = QPushButton('历史记录')
        # 清空历史记录: 按钮
        self.btn5 = QPushButton('清空历史记录')
        # 退出程序
        self.btn4 = QPushButton('退出')
        # 添加内容
        layout.addWidget(self.line, 0, 0, 1, 1)  # 账号位数
        layout.addWidget(self.combox, 0, 1, 1, 1)  # 邮箱类型选择
        layout.addWidget(self.line2, 1, 0, 1, 1)  # 密码位数
        layout.addWidget(self.btn, 1, 1, 1, 1)  # 确认按钮
        layout.addWidget(self.tEdit, 2, 0, 4, 1)  # 文本编辑框
        layout.addWidget(self.btn3, 2, 1, 1, 1)  # 查看历史记录
        layout.addWidget(self.btn2, 3, 1, 1, 1)  # 清除所有
        layout.addWidget(self.btn4, 5, 1, 1, 1)  # 退出
        layout.addWidget(self.btn5, 4, 1, 1, 1)  # 清空历史

        self.setLayout(layout)

    def get_select(self):
        self.type = self.sender().currentText()

    # 开始合成
    def synthesis(self):
        if self.type == '选择邮箱类型':
            self.type = '@google.com'
        if self.num2 == '' or self.num1 == '' or int(self.num1) < 8 or int(self.num2) < 8:
            QMessageBox.information(self, '通知', '位数必须大于8\n已经生成默认长度8的账号密码')
            self.num1 = 8
            self.num2 = 8
        account = ''
        password = ''
        for i in range(int(self.num1)):
            account += str(random.choice(self.lib))
        for i in range(int(self.num2)):
            password += str(random.choice(self.lib))
        account += self.type
        return account, password

    def save_data(self, account, password):
        with open('./账号密码.csv', 'a', encoding='utf-8')as f:
            f.write(f'{account},{password}\n')

    def get_numbers(self):
        self.num1 = self.line.text()
        self.num2 = self.line2.text()
        # 3.获取邮箱类型
        self.combox.currentIndexChanged.connect(self.get_select)
        # 4.开始随机生成设置并返回
        account, password = self.synthesis()
        # 5.写入文本方便下次读取使用(新增text用来显示)
        self.save_data(account, password)
        self.tEdit.setText(f"{account}\n{password}\n{'-' * 20}\n{self.tEdit.toPlainText()}")

    def clear_all(self):
        self.line.setText('')
        self.line2.setText('')
        self.tEdit.setText('')
        self.combox.setCurrentIndex(0)

    def history(self):
        try:
            with open('./账号密码.csv', 'r', encoding='utf-8') as f:
                text = f.readlines()
            content = ''
            for i in text:
                j = i.split(',')
                content += f"\n{j[0]}\n{j[1]}{'-' * 20}"
            self.tEdit.setText(content)
        except:
            QMessageBox.critical(self, '错误', '文件已被删除,或者还未生成历史记录', QMessageBox.Yes)

    def clear_history(self):
        with open('./账号密码.csv', 'w', encoding='utf-8')as f:
            f.write('')
        self.tEdit.setText('')

    def exit(self):
        exit(app.exec_())

    def run(self):
        self.btn.clicked.connect(self.get_numbers)
        self.btn2.clicked.connect(self.clear_all)
        self.btn3.clicked.connect(self.history)
        self.btn4.clicked.connect(self.exit)
        self.btn5.clicked.connect(self.clear_history)


if __name__ == '__main__':
    app = QApplication(argv)
    desktop = MailGenerate()
    desktop.show()
    desktop.run()
    exit(app.exec_())
