from PyQt5.QtWidgets import  QHBoxLayout, QVBoxLayout, QLineEdit, QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt
import sys
from calculator.addition.add import add
from calculator.division.divide import divide
from calculator.multiplication.multiply import multiply
from calculator.subtraction.subtract import subtract

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.output=QLineEdit()
        self.digit=QPushButton('+',self)
        self.digit__= QPushButton('-', self)
        self.digit____= QPushButton('/', self)
        self.digit___= QPushButton('*', self)
        self.digit00= QPushButton('00', self)
        self.digit0= QPushButton('0', self)
        self.digit1= QPushButton('1', self)
        self.digit2= QPushButton('2', self)
        self.digit3= QPushButton('3', self)
        self.digit4= QPushButton('4', self)
        self.digit5= QPushButton('5', self)
        self.digit6= QPushButton('6', self)
        self.digit7= QPushButton('7', self)
        self.digit8= QPushButton('8', self)
        self.digit9= QPushButton('9', self)
        self.digit_ = QPushButton('=', self)
        self.backspace= QPushButton('x',self)
        self.clear = QPushButton('CLR', self)

        self.initui()

    def initui(self):
#Calculator screen
     vbox=QVBoxLayout()

     vbox.addWidget(self.output)

 #row1
     row1=QHBoxLayout()
     row1.addWidget(self.digit)
     row1.addWidget(self.digit__)
     row1.addWidget(self.digit___)
     row1.addWidget(self.digit____)
     row1.addWidget(self.backspace)
     row1.addWidget(self.clear)
     vbox.addLayout(row1)
#row2
     row2=QHBoxLayout()
     row2.addWidget(self.digit0)
     row2.addWidget(self.digit1)
     row2.addWidget(self.digit2)
     row2.addWidget(self.digit3)
     vbox.addLayout(row2)
#row3
     row3=QHBoxLayout()
     row3.addWidget(self.digit4)
     row3.addWidget(self.digit5)
     row3.addWidget(self.digit6)
     row3.addWidget(self.digit7)
     vbox.addLayout(row3)
#row4
     row4=QHBoxLayout()
     row4.addWidget(self.digit8)
     row4.addWidget(self.digit9)
     row4.addWidget(self.digit00)
     row4.addWidget(self.digit_)
     vbox.addLayout(row4)

     self.setLayout(vbox)
     self.output.setMinimumHeight(60)

     self.digit.clicked.connect(lambda:self.output.insert('+'))
     self.digit__.clicked.connect(lambda:self.output.insert('-'))
     self.digit___.clicked.connect(lambda:self.output.insert('*'))
     self.digit____.clicked.connect(lambda:self.output.insert('/'))
     self.digit0.clicked.connect(lambda: self.output.insert('0'))
     self.digit00.clicked.connect(lambda: self.output.insert('00'))
     self.digit1.clicked.connect(lambda: self.output.insert('1'))
     self.digit2.clicked.connect(lambda: self.output.insert('2'))
     self.digit3.clicked.connect(lambda: self.output.insert('3'))
     self.digit4.clicked.connect(lambda: self.output.insert('4'))
     self.digit5.clicked.connect(lambda: self.output.insert('5'))
     self.digit6.clicked.connect(lambda: self.output.insert('6'))
     self.digit7.clicked.connect(lambda: self.output.insert('7'))
     self.digit8.clicked.connect(lambda: self.output.insert('8'))
     self.digit9.clicked.connect(lambda: self.output.insert('9'))




     self.setStyleSheet( """
    QPushButton {
        background-color: #f0f0f0;   
        border: 1px solid #b3b3b3;  
        border-radius: 8px;         
        padding: 10px;              
        font-size: 16px;           
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #e0e0e0;  
    }
    QPushButton:pressed {
        background-color: #d0d0d0; 
    }
"""
)

#set text: replaces former digit
#insert:insert new digit
     self.backspace.clicked.connect(self.backspace_background_code)
     self.clear.clicked.connect(self.clear_background_code)

    def backspace_background_code(self):
        text=self.output.text()
        self.output.setText(text[:-1])

    def clear_background_code(self):
        text = self.output.text()
        self.output.setText('')

    






































if __name__=='__main__':
    app=QApplication(sys.argv)
    calculator=Calculator()
    calculator.show()
    sys.exit(app.exec_())
