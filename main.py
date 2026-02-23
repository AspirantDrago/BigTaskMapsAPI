import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap, QImage

from src.utils import get_image

SCREEN_SIZE = (600, 450)


class Map(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show_map()

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Map')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(*SCREEN_SIZE)

    def show_map(self):
        image = get_image(
            37.530887, 55.703118, 0.002
        )
        pixmap = QPixmap(QImage.fromData(image.read()))
        self.image.setPixmap(pixmap)


def main():
    app = QApplication(sys.argv)
    window = Map()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
