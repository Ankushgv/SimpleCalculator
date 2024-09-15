import decimal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

from numpy import number

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.mainDisplayScreen = QVBoxLayout()
        self.displayValue = QLabel()
        self.displayValue.setText("0")
        self.inputField = QLineEdit()
        self.inputField.setValidator(QIntValidator())

        # self.inputField  ## to accept only numbers and signs
        self.zeroRow = QHBoxLayout()
        self.inputField.textChanged.connect(self.displayValue.setText)
        self.clearButton = QPushButton("Clear")
        self.clearButton.clicked.connect(self.clearEntry)

        self.equals = QPushButton("=")
        self.equals.clicked.connect(self.clickAction)

        self.openBracket = QPushButton("(")
        self.openBracket.clicked.connect(self.clickAction)

        self.closeBracket = QPushButton(")")
        self.closeBracket.clicked.connect(self.clickAction)

        self.mainDisplayScreen.addWidget(self.displayValue)
        self.mainDisplayScreen.addWidget(self.inputField)
        
        self.zeroRow.addWidget(self.clearButton)
        self.zeroRow.addWidget(self.equals)
        self.zeroRow.addWidget(self.openBracket)
        self.zeroRow.addWidget(self.closeBracket)
        self.mainDisplayScreen.addLayout(self.zeroRow)

        self.firstRow = QHBoxLayout()
        
        self.number1 = QPushButton("1")
        self.number1.clicked.connect(self.clickAction)
        self.number2 = QPushButton("2")
        self.number2.clicked.connect(self.clickAction)
        self.number3 = QPushButton("3")
        self.number3.clicked.connect(self.clickAction)
        self.number4 = QPushButton("4")
        self.number4.clicked.connect(self.clickAction)
        self.number5 = QPushButton("5")
        self.number5.clicked.connect(self.clickAction)

        self.firstRow.addWidget(self.number1)
        self.firstRow.addWidget(self.number2)
        self.firstRow.addWidget(self.number3)
        self.firstRow.addWidget(self.number4)
        self.firstRow.addWidget(self.number5)

        self.mainDisplayScreen.addLayout(self.firstRow)

        self.secondRow = QHBoxLayout()
        
        self.number6 = QPushButton("6")
        self.number6.clicked.connect(self.clickAction)
        self.number7 = QPushButton("7")
        self.number7.clicked.connect(self.clickAction)
        self.number8 = QPushButton("8")
        self.number8.clicked.connect(self.clickAction)
        self.number9 = QPushButton("9")
        self.number9.clicked.connect(self.clickAction)
        self.number0 = QPushButton("0")
        self.number0.clicked.connect(self.clickAction)

        self.secondRow.addWidget(self.number6)
        self.secondRow.addWidget(self.number7)
        self.secondRow.addWidget(self.number8)
        self.secondRow.addWidget(self.number9)
        self.secondRow.addWidget(self.number0)

        self.mainDisplayScreen.addLayout(self.secondRow)

        self.thirdRow = QHBoxLayout()
        
        self.numberDecimal = QPushButton(".")
        self.numberDecimal.clicked.connect(self.clickAction)
        self.numberPlus = QPushButton("+")
        self.numberPlus.clicked.connect(self.clickAction)
        self.numberMinus = QPushButton("-")
        self.numberMinus.clicked.connect(self.clickAction)
        self.numberMultiply = QPushButton("*")
        self.numberMultiply.clicked.connect(self.clickAction)
        self.numberDevide = QPushButton("/")
        self.numberDevide.clicked.connect(self.clickAction)

        self.thirdRow.addWidget(self.numberDecimal)
        self.thirdRow.addWidget(self.numberPlus)
        self.thirdRow.addWidget(self.numberMinus)
        self.thirdRow.addWidget(self.numberMultiply)
        self.thirdRow.addWidget(self.numberDevide)

        self.mainDisplayScreen.addLayout(self.thirdRow)

        self.container = QWidget()
        self.container.setLayout(self.mainDisplayScreen)

        self.setCentralWidget(self.container)

        self.operators = ["+", "-", "*", "/", ".", "=", "(", ")"]
        self.value = []
        # self.number_ = 0
        # self.secondNumber = 0
        # self.operator = ""
        # self.decimalPointAdded = False
        
    def clickAction(self):
        
        sender = self.sender().text()
        self.value.append(sender)

        try:
            value = "".join(self.value)
            print(value)
            
            result = []
            temp_list = []
            for i in value:
                if i in self.operators:
                    temp_list.append(i)
                    temp_list = "".join(temp_list)
                    result.append(temp_list)
                    temp_list = []
                else:
                    temp_list.append(i)
            result.append(temp_list)
            print(str(result))

            self.inputField.setText(value)
        except ValueError:
            pass
        # try:
        #     if int(sender) in range(0, 10):
        #         self.value.append(sender)
        #         self.firstNumber = "".join(self.value)
        #         self.showValue(self.firstNumber)
                
        # except ValueError:
        #     pass
        
        # try:
        #     if int(sender) in self.operators:
        #         self.value.append(sender)
        #         self.operator = "".join(self.value)
                
            
        # except ValueError:
        #     pass

        # if sender == "." and not self.decimalPointAdded:
        #     self.value.append(sender)
        #     self.decimalPointAdded = True
        #     self.firstNumber = "".join(self.value)
        #     self.showValue(self.firstNumber)
        #     print(self.value, '==============')

        # if sender == "(" or sender == ")":
        #     self.value.append(sender)
        #     self.firstNumber = "".join(self.value)
        #     self.showValue(self.firstNumber)
        #     print(self.value, '==============')

    def clearEntry(self):
        self.inputField.setText("0")
        self.value.clear()
        self.decimalPointAdded = False

    def showValue(self, v):
        self.inputField.setText(v)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
        