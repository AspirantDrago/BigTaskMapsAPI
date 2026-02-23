import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap, QImage, QKeyEvent, QGuiApplication

from src.toponym import Toponym
from src.utils import get_image
from src.map_config import Map

from forms.main import Ui_Form

SCREEN_SIZE = (600, 450)


class MapWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.map_config = Map(37.530887, 55.703118, 0.002)
        self.show_map()
        self.btnLightTheme.clicked.connect(self.set_light_theme)
        self.btnDarkTheme.clicked.connect(self.set_dark_theme)
        self.btnSearch.clicked.connect(self.find_toponym)
        self.btnResetSearch.clicked.connect(self.reset_search)

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

    def set_light_theme(self) -> None:
        self.image.setFocus()
        QGuiApplication.styleHints().setColorScheme(Qt.ColorScheme.Light)
        self.map_config.set_light_theme()
        self.show_map()

    def set_dark_theme(self) -> None:
        self.image.setFocus()
        QGuiApplication.styleHints().setColorScheme(Qt.ColorScheme.Dark)
        self.map_config.set_dark_theme()
        self.show_map()

    def find_toponym(self):
        self.image.setFocus()
        text = self.textSearch.text().strip()
        toponym = Toponym.from_search_text(text)
        self.map_config.set_toponym(toponym)
        self.show_map()

    def reset_search(self):
        self.image.setFocus()
        self.textSearch.clear()
        self.map_config.clear_toponym()
        self.show_map()


def main():
    app = QApplication(sys.argv)
    QGuiApplication.styleHints().setColorScheme(Qt.ColorScheme.Light)
    window = MapWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
