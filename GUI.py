import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QGridLayout, QLineEdit, QApplication)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import Scraper as Scraper
import time

class GUI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.url = QLabel('URL of the Product :')
        self.price = QLabel('Max Price :')
        self.mail = QLabel('Contact Mail Account:')
        self.msg = QLabel('If the price goes below the max price it would be shown HERE')

        self.urlField = QLineEdit()
        self.priceField = QLineEdit()
        self.mailField = QLineEdit()

        btn = QPushButton('Search', self)
        btn.clicked.connect(self.track_product)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.url, 1, 0)
        grid.addWidget(self.urlField, 1, 1)

        grid.addWidget(self.price, 2, 0)
        grid.addWidget(self.priceField, 2, 1)

        grid.addWidget(self.mail, 3, 0)
        grid.addWidget(self.mailField, 3, 1)

        grid.addWidget(btn, 4, 1)

        grid.addWidget(self.msg, 5, 0)

        self.setLayout(grid)
        self.setGeometry(0, 0, 400, 200)
        self.setWindowTitle('Amazon Tracker')
        self.setWindowIcon(QIcon('icono_amazon_tracker.jpeg'))

        self.show()

    @pyqtSlot()
    def track_product(self):

        url_product = self.urlField.text()
        price_product = self.priceField.text()
        user_mail = self.mailField.text()

        Scraper.check_price(url_product, price_product, user_mail)
        self.msg.setText('The price is below the max price. Check your mail.')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())
