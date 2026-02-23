import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap, QImage, QKeyEvent

from src.utils import get_image
from src.map_config import Map

SCREEN_SIZE = (600, 450)


class MapWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.map_config = Map(37.530887, 55.703118, 0.002)
        self.show_map()

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Map')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(*SCREEN_SIZE)

    def show_map(self):
        if not self.map_config.updated:
            return
        self.map_config.updated = False
        image = get_image(self.map_config)
        pixmap = QPixmap(QImage.fromData(image.read()))
        self.image.setPixmap(pixmap)

    def keyPressEvent(self, event: QKeyEvent):
        match event.key():
            case Qt.Key.Key_PageDown:
                self.map_config.zome_down()
                self.show_map()
            case Qt.Key.Key_PageUp:
                self.map_config.zome_up()
                self.show_map()
            case Qt.Key.Key_Left:
                self.map_config.move_left()
                self.show_map()
            case Qt.Key.Key_Right:
                self.map_config.move_right()
                self.show_map()
            case Qt.Key.Key_Up:
                self.map_config.move_up()
                self.show_map()
            case Qt.Key.Key_Down:
                self.map_config.move_down()
                self.show_map()


def main():
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
