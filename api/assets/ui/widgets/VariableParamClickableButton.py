from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton, QToolButton

from assets.ui.util import color
from assets.ui.widgets.menu_button import AtMenuButton


class VariableParamClickableButton(AtMenuButton):
    def __init__(
            self,
            id="",
            text="",
            height=50,
            minimum_width=50,
            maximum_width=None,
            text_padding=55,
            font_size=12,
            border_radius=10,
            text_color=color.MENU_BUTTON_TEXT,
            btn_color=color.MENU_BUTTON_BACKGROUND,
            btn_hover=color.MENU_BUTTON_HOVER,
            btn_pressed=color.MENU_BUTTON_PRESSED,
            is_active=False,
            do_when_clicked=None,
            do_when_clicked_params=None
    ):
        self.do_when_clicked = do_when_clicked
        super().__init__(id, text, height, minimum_width, maximum_width, text_padding, font_size, border_radius,
                         text_color, btn_color, btn_hover, btn_pressed, is_active, True,
                         lambda: do_when_clicked(do_when_clicked_params))
