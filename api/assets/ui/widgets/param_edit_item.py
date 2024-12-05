import uuid as uuid
from PySide6.QtWidgets import QHBoxLayout, QLabel, QTextEdit

from assets.components import Parameter
from assets.ui.util import color
from assets.ui.widgets.combo_box import CustomComboBox
from assets.ui.widgets.menu_button import AtMenuButton
from model.DataTypes import DATA_TYPES


class ParamEditItem(QHBoxLayout):
    def __init__(self, parameter, do_when_remove_is_clicked=None):
        super().__init__()
        self.name = parameter.name
        self.param_type = parameter.type_name
        self.id = uuid.uuid4() if parameter.identifier is None else parameter.identifier

        label_styleSheet = """
                           QLabel {
                               font-family: Arial; 
                               font-size: 14px;
                           }
                           """

        name_label = QLabel("Name:")
        name_label.setStyleSheet(label_styleSheet)
        self.addWidget(name_label)
        self.name_text_edit = QTextEdit()
        self.name_text_edit.setStyleSheet("QTextEdit {border-radius: 10px; background-color: white}")
        self.name_text_edit.setText(self.name)
        # self.name_text_edit.setFixedWidth(120)
        self.name_text_edit.setFixedHeight(30)
        self.addWidget(self.name_text_edit)

        type_label = QLabel("Type:")
        type_label.setMinimumWidth(1)
        type_label.setStyleSheet(label_styleSheet)
        self.addWidget(type_label)

        self.type_combo_box = CustomComboBox()
        index = 0
        for i in range(0, len(DATA_TYPES)):
            self.type_combo_box.addItem(DATA_TYPES[i])
            if self.param_type == DATA_TYPES[i]:
                index = i
        self.type_combo_box.setCurrentIndex(index)
        self.addWidget(self.type_combo_box)

        remove_button = AtMenuButton(
            text="Remove",
            btn_color=color.REMOVE_BUTTON,
            height=30,
            minimum_width=80,
            maximum_width=80,
            do_when_clicked=do_when_remove_is_clicked
        )
        self.addWidget(remove_button)

    def get_param(self):
        return Parameter(self.name_text_edit.toPlainText(), self.type_combo_box.currentText(), self.id)
