import decimal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

from numpy import number
import keyboard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.mainDisplayScreen = QVBoxLayout()
        self.displayValue = QLabel()
        self.displayValue.setText("0")
        self.displayValue.setFont(QFont('Arial', 12))
        self.inputField = QLineEdit()
        self.inputField.setValidator(QIntValidator())

        self.zeroRow = QHBoxLayout()
        self.inputField.textChanged.connect(self.displayValue.setText)
        self.number1 = QPushButton("1")
        self.number1.clicked.connect(self.clickAction)

        self.number2 = QPushButton("2")
        self.number2.clicked.connect(self.clickAction)

        self.number3 = QPushButton("3")
        self.number3.clicked.connect(self.clickAction)

        self.clearButton = QPushButton("Clear")
        self.clearButton.clicked.connect(self.clearEntry)

        self.deleteButton = QPushButton("del")
        self.deleteButton.clicked.connect(self.backspace)

        self.mainDisplayScreen.addWidget(self.displayValue)
        self.mainDisplayScreen.addWidget(self.inputField)
        
        self.zeroRow.addWidget(self.number1)
        self.zeroRow.addWidget(self.number2)
        self.zeroRow.addWidget(self.number3)
        self.zeroRow.addWidget(self.clearButton)
        self.zeroRow.addWidget(self.deleteButton)
        self.mainDisplayScreen.addLayout(self.zeroRow)

        self.firstRow = QHBoxLayout()
        
        self.number4 = QPushButton("4")
        self.number4.clicked.connect(self.clickAction)

        self.number5 = QPushButton("5")
        self.number5.clicked.connect(self.clickAction)

        self.number6 = QPushButton("6")
        self.number6.clicked.connect(self.clickAction)

        self.openBracket = QPushButton("(")
        self.openBracket.clicked.connect(self.clickAction)

        self.closeBracket = QPushButton(")")
        self.closeBracket.clicked.connect(self.clickAction)

        self.firstRow.addWidget(self.number4)
        self.firstRow.addWidget(self.number5)
        self.firstRow.addWidget(self.number6)
        self.firstRow.addWidget(self.openBracket)
        self.firstRow.addWidget(self.closeBracket)

        self.mainDisplayScreen.addLayout(self.firstRow)

        self.secondRow = QHBoxLayout()
        
        self.number7 = QPushButton("7")
        self.number7.clicked.connect(self.clickAction)

        self.number8 = QPushButton("8")
        self.number8.clicked.connect(self.clickAction)

        self.number9 = QPushButton("9")
        self.number9.clicked.connect(self.clickAction)

        self.numberPlus = QPushButton("+")
        self.numberPlus.clicked.connect(self.clickAction)

        self.numberMinus = QPushButton("-")
        self.numberMinus.clicked.connect(self.clickAction)

        self.secondRow.addWidget(self.number7)
        self.secondRow.addWidget(self.number8)
        self.secondRow.addWidget(self.number9)
        self.secondRow.addWidget(self.numberPlus)
        self.secondRow.addWidget(self.numberMinus)

        self.mainDisplayScreen.addLayout(self.secondRow)

        self.thirdRow = QHBoxLayout()
        
        self.numberDecimal = QPushButton(".")
        self.numberDecimal.clicked.connect(self.clickAction)

        self.number0 = QPushButton("0")
        self.number0.clicked.connect(self.clickAction)

        self.equals = QPushButton("=")
        self.equals.clicked.connect(self.clickAction)

        self.numberMultiply = QPushButton("*")
        self.numberMultiply.clicked.connect(self.clickAction)

        self.numberDevide = QPushButton("/")
        self.numberDevide.clicked.connect(self.clickAction)

        self.thirdRow.addWidget(self.numberDecimal)
        self.thirdRow.addWidget(self.number0)
        self.thirdRow.addWidget(self.equals)
        self.thirdRow.addWidget(self.numberMultiply)
        self.thirdRow.addWidget(self.numberDevide)

        self.mainDisplayScreen.addLayout(self.thirdRow)

        self.container = QWidget()
        self.container.setLayout(self.mainDisplayScreen)

        self.setCentralWidget(self.container)

        self.operators = ["+", "-", "*", "/", "=", "(", ")"]
        self.value = []
        self.decimalPointAdded = False
        self.inputValue = None
        
    def clickAction(self):
        
        sender = self.sender().text()
        self.value.append(sender)

        try:
            self.inputValue = "".join(self.value)
            
            result = []
            temp_list = []
            for i in self.inputValue:
                if i in self.operators:
                    self.numberDecimal.setEnabled(True)
                    temp_list.append(i)
                    temp_list = "".join(temp_list)
                    result.append(temp_list)
                    temp_list = [] 
                else:
                    if i == ".":
                        self.numberDecimal.setDisabled(True)
                        temp_list.append(i)
                    else:
                        temp_list.append(i)
            result.append(temp_list)
            self.inputField.setText(self.inputValue)

            if sender == "=":
                self.doOperation(result)

        except ValueError:
            pass
        except SyntaxError:
            print("Invalid expression")
    
    def doOperation(self, res):
        self.clearEntry()
        equation = ''.join(map(str, res))[:-3]
        result = eval(equation)
        print(result)
        self.displayValue.setText(str(result))
        
    def clearEntry(self):
        self.inputField.setText("0")
        self.value.clear()
        self.numberDecimal.setEnabled(True)

    def backspace(self):
        if self.inputValue is not None:
            self.inputValue = self.inputValue[:-1]
            self.value = self.value[:-1]
            self.inputField.setText(self.inputValue)
            if "." not in self.inputValue:
                self.numberDecimal.setEnabled(True)
        
    def showValue(self, v):
        self.inputField.setText(v)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
        