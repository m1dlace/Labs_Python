import re
import sys
import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication,QPushButton, QCheckBox, QSpinBox, QRadioButton)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        #-----------Creation---------------------------------------------
        #label
        labelStroka = QLabel('Строка: ')
        labelResult = QLabel('Результат: ')
        #lineEdit
        self.lineEditInput = QLineEdit()
        self.lineEditResult = QLineEdit()
        self.input_ = self.lineEditInput.text()
        self.output_ = self.lineEditResult.text()
        #chekbox
        self.checkbox1 = QCheckBox('Удалить слова размером меньше n символов, n = ')
        self.checkbox2 = QCheckBox('Заменить все цифры на *')
        self.checkbox3 = QCheckBox('Вставить по пробелу между символами')
        self.checkbox4 = QCheckBox('Сортировать слова в строке')
        #QSpinBox
        self.spinBox1 = QSpinBox()
        #QPushButton
        buttonFormat = QPushButton('Форматировать!',self)
        #QRadioButton
        self.radio1 = QRadioButton('По размеру')
        self.radio1.setChecked(True)
        self.radio2 = QRadioButton('Лексиграфически')
        #---------------Position-----------------------------
        grid = QGridLayout()
        grid.setSpacing(10)
        #label
        grid.addWidget(labelStroka,1,0)
        grid.addWidget(labelResult,9,0)
        #lineEdit
        grid.addWidget(self.lineEditInput,1,1)
        grid.addWidget(self.lineEditResult,9,1)
        #chekbox
        grid.addWidget(self.checkbox1,2,1)
        grid.addWidget(self.checkbox2,3,1)
        grid.addWidget(self.checkbox3,4,1)
        grid.addWidget(self.checkbox4,5,1)

        #QPushButton
        grid.addWidget(buttonFormat,8,1)
        #QSpinBox
        grid.addWidget(self.spinBox1,2,2)
        #QRadioButton
        grid.addWidget(self.radio1,6,1)
        grid.addWidget(self.radio2,7,1)
        buttonFormat.clicked.connect(self.buttonClicked)
        #---------------------------------------------------------
        self.setLayout(grid)
        self.setGeometry(350, 350, 400, 350)
        self.setWindowTitle('Review')
        self.show()
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close
    def buttonClicked(self):
        #---on button click starts formatting------
        self.input_ = ''
        self.output_ = ''
        self.input_ = self.lineEditInput.text()
        self.output_ = self.input_
        tempArr = []
        #------------------------------------------
        #--------1st checkbox 'Удалить слова размером меньше n символов, n = '----------------------
        if (self.checkbox1.checkState()==2):
            n = self.spinBox1.value()
            splitInputArr = self.input_.split(' ')
            for i in range(len(splitInputArr)):
                if len(splitInputArr[i])>=n:
                    tempArr.append(splitInputArr[i])
                self.output_ = ' '.join(tempArr)
            self.lineEditResult.setText(self.output_)
        #--------2nd checkbox 'Заменить все цифры на *'----------------------
        if (self.checkbox2.checkState()==2):
            self.output_ = re.sub('\d','*',self.output_)    
            self.lineEditResult.setText(self.output_)
        #--------3rd checkbox 'Вставить по пробелу между символами'----------------------
        if (self.checkbox3.checkState()==2):
            #tempSubArr = list(self.output_)
            self.output_ = ' '.join(list(self.output_))
            self.lineEditResult.setText(self.output_)
        #--------4th checkbox 'Сортировать слова в строке'----------------------
        if (self.checkbox4.checkState()==2) and (self.radio1.isChecked): #Size
            tempSplit = self.output_.split()
            tempSplit.sort(key=len)
            for i in range(len(tempSplit)):
                self.output_ = ' '.join(tempSplit)
            self.lineEditResult.setText(self.output_)
        if (self.checkbox4.checkState()==2) and (self.radio2.isChecked): #Lex
            tempSplit = self.output_.split()
            tempSplit.sort()
            for i in range(len(tempSplit)):
                self.output_ = ' '.join(tempSplit)
            self.lineEditResult.setText(self.output_)
        #----------Output--------------------------
        if ((self.checkbox1.checkState() == 0) and (self.checkbox2.checkState()==0) and (self.checkbox3.checkState()==0) and (self.checkbox4.checkState()==0)):
            self.output_ = self.input_
            self.lineEditResult.setText(self.output_)
        #------------------------------------------
        self.lineEditResult.setText(self.output_)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())