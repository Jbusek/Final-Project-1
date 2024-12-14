import csv

from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QRadioButton, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QIntValidator

class Logic(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Voting Application")
        self.setGeometry(100, 100, 350, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.label = QLabel("Enter Identification:", self)
        self.lineEdit = QLineEdit(self)

        self.lineEdit.setValidator(QIntValidator())

        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)

        self.label_2 = QLabel("Choose a Candidate:", self)
        layout.addWidget(self.label_2)

        self.button_jane = QRadioButton("Jane", self)
        self.button_john = QRadioButton("John", self)
        layout.addWidget(self.button_jane)
        layout.addWidget(self.button_john)

        self.button_submit = QPushButton("Submit", self)
        layout.addWidget(self.button_submit)
        self.button_submit.clicked.connect(self.process_vote)

        self.label_status = QLabel("", self)
        layout.addWidget(self.label_status)

    def process_vote(self):
        identification = self.lineEdit.text()

        if not identification.isdigit():
            self.label_status.setText("Identification must be integers only.")
            return

        if self.check_vote(identification):
            self.label_status.setText("You have already voted with this identification.")
            return

        if self.button_jane.isChecked():
            candidate = "Jane"
        elif self.button_john.isChecked():
            candidate = "John"
        else:
            candidate = "No candidate selected"

        self.save_vote(identification, candidate)

        self.label_status.setText(f"Vote cast for {candidate}")

    def save_vote(self, identification, candidate):
        with open('votes.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([identification, candidate])

    def check_vote(self, identification):
        try:
            with open('votes.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == identification:
                        return True
        except FileNotFoundError:
            return False
        return False
    def reset(self):
        self.lineEdit.clear()
        self.button_jane.setChecked(False)
        self.button_john.setChecked(False)

# https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/

