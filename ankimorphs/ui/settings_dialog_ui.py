# Form implementation generated from reading ui file 'ankimorphs/ui/settings_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SettingsDialog:
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        SettingsDialog.resize(925, 408)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=SettingsDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.note_filters_tab = QtWidgets.QWidget()
        self.note_filters_tab.setObjectName("note_filters_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.note_filters_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.note_filters_table = QtWidgets.QTableWidget(parent=self.note_filters_tab)
        self.note_filters_table.setObjectName("note_filters_table")
        self.note_filters_table.setColumnCount(7)
        self.note_filters_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(6, item)
        self.verticalLayout_3.addWidget(self.note_filters_table)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.delete_row_button = QtWidgets.QPushButton(parent=self.note_filters_tab)
        self.delete_row_button.setObjectName("delete_row_button")
        self.horizontalLayout_2.addWidget(self.delete_row_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.add_new_row_button = QtWidgets.QPushButton(parent=self.note_filters_tab)
        self.add_new_row_button.setObjectName("add_new_row_button")
        self.horizontalLayout_2.addWidget(self.add_new_row_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.note_filters_tab, "")
        self.extra_fields_tab = QtWidgets.QWidget()
        self.extra_fields_tab.setObjectName("extra_fields_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.extra_fields_tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.extra_fields_table = QtWidgets.QTableWidget(parent=self.extra_fields_tab)
        self.extra_fields_table.setObjectName("extra_fields_table")
        self.extra_fields_table.setColumnCount(4)
        self.extra_fields_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.extra_fields_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.extra_fields_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.extra_fields_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.extra_fields_table.setHorizontalHeaderItem(3, item)
        self.verticalLayout_5.addWidget(self.extra_fields_table)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.extra_fields_tab, "")
        self.tags_tab = QtWidgets.QWidget()
        self.tags_tab.setObjectName("tags_tab")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tags_tab)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(parent=self.tags_tab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.tags_tab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.tags_tab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.ready_tag_input = QtWidgets.QLineEdit(parent=self.tags_tab)
        self.ready_tag_input.setObjectName("ready_tag_input")
        self.verticalLayout_7.addWidget(self.ready_tag_input)
        self.not_read_tag_input = QtWidgets.QLineEdit(parent=self.tags_tab)
        self.not_read_tag_input.setObjectName("not_read_tag_input")
        self.verticalLayout_7.addWidget(self.not_read_tag_input)
        self.known_tag_input = QtWidgets.QLineEdit(parent=self.tags_tab)
        self.known_tag_input.setObjectName("known_tag_input")
        self.verticalLayout_7.addWidget(self.known_tag_input)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_10.addItem(spacerItem2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.restore_tags_defaults_button = QtWidgets.QPushButton(parent=self.tags_tab)
        self.restore_tags_defaults_button.setObjectName("restore_tags_defaults_button")
        self.horizontalLayout_7.addWidget(self.restore_tags_defaults_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.verticalLayout_12.addLayout(self.verticalLayout_10)
        self.tabWidget.addTab(self.tags_tab, "")
        self.parse_tab = QtWidgets.QWidget()
        self.parse_tab.setObjectName("parse_tab")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.parse_tab)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.parse_ignore_bracket_contents_input = QtWidgets.QCheckBox(parent=self.parse_tab)
        self.parse_ignore_bracket_contents_input.setObjectName("parse_ignore_bracket_contents_input")
        self.verticalLayout_9.addWidget(self.parse_ignore_bracket_contents_input)
        self.parse_ignore_round_bracket_contents_input = QtWidgets.QCheckBox(parent=self.parse_tab)
        self.parse_ignore_round_bracket_contents_input.setObjectName("parse_ignore_round_bracket_contents_input")
        self.verticalLayout_9.addWidget(self.parse_ignore_round_bracket_contents_input)
        self.parse_ignore_slim_round_bracket_contents_input = QtWidgets.QCheckBox(parent=self.parse_tab)
        self.parse_ignore_slim_round_bracket_contents_input.setObjectName("parse_ignore_slim_round_bracket_contents_input")
        self.verticalLayout_9.addWidget(self.parse_ignore_slim_round_bracket_contents_input)
        self.parse_ignore_names_morphemizer_input = QtWidgets.QCheckBox(parent=self.parse_tab)
        self.parse_ignore_names_morphemizer_input.setObjectName("parse_ignore_names_morphemizer_input")
        self.verticalLayout_9.addWidget(self.parse_ignore_names_morphemizer_input)
        self.parse_ignore_names_textfile_input = QtWidgets.QCheckBox(parent=self.parse_tab)
        self.parse_ignore_names_textfile_input.setObjectName("parse_ignore_names_textfile_input")
        self.verticalLayout_9.addWidget(self.parse_ignore_names_textfile_input)
        self.parse_ignore_suspended_cards_content_input = QtWidgets.QCheckBox(parent=self.parse_tab)
        self.parse_ignore_suspended_cards_content_input.setObjectName("parse_ignore_suspended_cards_content_input")
        self.verticalLayout_9.addWidget(self.parse_ignore_suspended_cards_content_input)
        self.verticalLayout_13.addLayout(self.verticalLayout_9)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_13.addItem(spacerItem4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.restore_parse_defaults_button = QtWidgets.QPushButton(parent=self.parse_tab)
        self.restore_parse_defaults_button.setObjectName("restore_parse_defaults_button")
        self.horizontalLayout_8.addWidget(self.restore_parse_defaults_button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout_13.addLayout(self.horizontalLayout_8)
        self.tabWidget.addTab(self.parse_tab, "")
        self.skip_tab = QtWidgets.QWidget()
        self.skip_tab.setObjectName("skip_tab")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.skip_tab)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.skip_only_known_morphs_cards_input = QtWidgets.QCheckBox(parent=self.skip_tab)
        self.skip_only_known_morphs_cards_input.setObjectName("skip_only_known_morphs_cards_input")
        self.verticalLayout_11.addWidget(self.skip_only_known_morphs_cards_input)
        self.skip_unknown_morph_seen_today_cards_input = QtWidgets.QCheckBox(parent=self.skip_tab)
        self.skip_unknown_morph_seen_today_cards_input.setObjectName("skip_unknown_morph_seen_today_cards_input")
        self.verticalLayout_11.addWidget(self.skip_unknown_morph_seen_today_cards_input)
        self.skip_show_num_of_skipped_cards_input = QtWidgets.QCheckBox(parent=self.skip_tab)
        self.skip_show_num_of_skipped_cards_input.setObjectName("skip_show_num_of_skipped_cards_input")
        self.verticalLayout_11.addWidget(self.skip_show_num_of_skipped_cards_input)
        self.verticalLayout_20.addLayout(self.verticalLayout_11)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_20.addItem(spacerItem6)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.restore_skip_defaults_button = QtWidgets.QPushButton(parent=self.skip_tab)
        self.restore_skip_defaults_button.setObjectName("restore_skip_defaults_button")
        self.horizontalLayout_11.addWidget(self.restore_skip_defaults_button)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.verticalLayout_20.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.skip_tab, "")
        self.recalc_tab = QtWidgets.QWidget()
        self.recalc_tab.setObjectName("recalc_tab")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.recalc_tab)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.recalc_on_sync_input = QtWidgets.QCheckBox(parent=self.recalc_tab)
        self.recalc_on_sync_input.setObjectName("recalc_on_sync_input")
        self.verticalLayout_21.addWidget(self.recalc_on_sync_input)
        self.verticalLayout_17.addLayout(self.verticalLayout_21)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_16 = QtWidgets.QLabel(parent=self.recalc_tab)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        self.recalc_interval_known_input = QtWidgets.QSpinBox(parent=self.recalc_tab)
        self.recalc_interval_known_input.setObjectName("recalc_interval_known_input")
        self.horizontalLayout_6.addWidget(self.recalc_interval_known_input)
        self.label_17 = QtWidgets.QLabel(parent=self.recalc_tab)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_6.addWidget(self.label_17)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_17.addLayout(self.horizontalLayout_6)
        spacerItem9 = QtWidgets.QSpacerItem(17, 37, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_17.addItem(spacerItem9)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.restore_recalc_defaults_button = QtWidgets.QPushButton(parent=self.recalc_tab)
        self.restore_recalc_defaults_button.setObjectName("restore_recalc_defaults_button")
        self.horizontalLayout_9.addWidget(self.restore_recalc_defaults_button)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem10)
        self.verticalLayout_17.addLayout(self.horizontalLayout_9)
        self.verticalLayout_18.addLayout(self.verticalLayout_17)
        self.tabWidget.addTab(self.recalc_tab, "")
        self.shortcuts_tab = QtWidgets.QWidget()
        self.shortcuts_tab.setObjectName("shortcuts_tab")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.shortcuts_tab)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_14 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_16.addWidget(self.label_14)
        self.label_13 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_16.addWidget(self.label_13)
        self.label_8 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_16.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_16.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_16.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_16.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_16.addWidget(self.label_12)
        self.horizontalLayout_5.addLayout(self.verticalLayout_16)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.shortcut_recalc_input = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcut_recalc_input.setObjectName("shortcut_recalc_input")
        self.verticalLayout_15.addWidget(self.shortcut_recalc_input)
        self.shortcut_settings_input = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcut_settings_input.setObjectName("shortcut_settings_input")
        self.verticalLayout_15.addWidget(self.shortcut_settings_input)
        self.shortcut_browse_ready_same_unknown_input = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcut_browse_ready_same_unknown_input.setObjectName("shortcut_browse_ready_same_unknown_input")
        self.verticalLayout_15.addWidget(self.shortcut_browse_ready_same_unknown_input)
        self.shortcut_browse_all_same_unknown_input = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcut_browse_all_same_unknown_input.setObjectName("shortcut_browse_all_same_unknown_input")
        self.verticalLayout_15.addWidget(self.shortcut_browse_all_same_unknown_input)
        self.shortcut_known_and_skip_input = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcut_known_and_skip_input.setObjectName("shortcut_known_and_skip_input")
        self.verticalLayout_15.addWidget(self.shortcut_known_and_skip_input)
        self.shortcut_learn_now_input = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcut_learn_now_input.setObjectName("shortcut_learn_now_input")
        self.verticalLayout_15.addWidget(self.shortcut_learn_now_input)
        self.shortcut_view_morphs_input = QtWidgets.QKeySequenceEdit(parent=self.shortcuts_tab)
        self.shortcut_view_morphs_input.setObjectName("shortcut_view_morphs_input")
        self.verticalLayout_15.addWidget(self.shortcut_view_morphs_input)
        self.horizontalLayout_5.addLayout(self.verticalLayout_15)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.verticalLayout_19.addLayout(self.horizontalLayout_5)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_19.addItem(spacerItem12)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.restore_shortcut_defaults_button = QtWidgets.QPushButton(parent=self.shortcuts_tab)
        self.restore_shortcut_defaults_button.setObjectName("restore_shortcut_defaults_button")
        self.horizontalLayout_10.addWidget(self.restore_shortcut_defaults_button)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem13)
        self.verticalLayout_19.addLayout(self.horizontalLayout_10)
        self.tabWidget.addTab(self.shortcuts_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.restore_all_defaults_button = QtWidgets.QPushButton(parent=SettingsDialog)
        self.restore_all_defaults_button.setObjectName("restore_all_defaults_button")
        self.horizontalLayout.addWidget(self.restore_all_defaults_button)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem14)
        self.ankimorphs_version_label = QtWidgets.QLabel(parent=SettingsDialog)
        self.ankimorphs_version_label.setObjectName("ankimorphs_version_label")
        self.horizontalLayout.addWidget(self.ankimorphs_version_label)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem15)
        self.cancel_button = QtWidgets.QPushButton(parent=SettingsDialog)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.save_button = QtWidgets.QPushButton(parent=SettingsDialog)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "AnkiMorph Settings"))
        item = self.note_filters_table.horizontalHeaderItem(0)
        item.setText(_translate("SettingsDialog", "Note Type"))
        item = self.note_filters_table.horizontalHeaderItem(1)
        item.setText(_translate("SettingsDialog", "Tags"))
        item = self.note_filters_table.horizontalHeaderItem(2)
        item.setText(_translate("SettingsDialog", "Field"))
        item = self.note_filters_table.horizontalHeaderItem(3)
        item.setText(_translate("SettingsDialog", "Morphemizer"))
        item = self.note_filters_table.horizontalHeaderItem(4)
        item.setText(_translate("SettingsDialog", "Morph Priority"))
        item = self.note_filters_table.horizontalHeaderItem(5)
        item.setText(_translate("SettingsDialog", "Read"))
        item = self.note_filters_table.horizontalHeaderItem(6)
        item.setText(_translate("SettingsDialog", "Modify"))
        self.delete_row_button.setText(_translate("SettingsDialog", "Delete Selected Row"))
        self.add_new_row_button.setText(_translate("SettingsDialog", "Add New Row"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.note_filters_tab), _translate("SettingsDialog", "Note Filters"))
        item = self.extra_fields_table.horizontalHeaderItem(0)
        item.setText(_translate("SettingsDialog", "Note Type"))
        item = self.extra_fields_table.horizontalHeaderItem(1)
        item.setText(_translate("SettingsDialog", "Unknowns"))
        item = self.extra_fields_table.horizontalHeaderItem(2)
        item.setText(_translate("SettingsDialog", "Highlighted"))
        item = self.extra_fields_table.horizontalHeaderItem(3)
        item.setText(_translate("SettingsDialog", "Difficulty"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.extra_fields_tab), _translate("SettingsDialog", "Extra Fields"))
        self.label_2.setText(_translate("SettingsDialog", "One unknown morph"))
        self.label_3.setText(_translate("SettingsDialog", "Multiple Unknown morphs"))
        self.label_4.setText(_translate("SettingsDialog", "All morphs known"))
        self.restore_tags_defaults_button.setText(_translate("SettingsDialog", "Restore Default Tags Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tags_tab), _translate("SettingsDialog", "Tags"))
        self.parse_ignore_bracket_contents_input.setText(_translate("SettingsDialog", "ignore content in square brackets []"))
        self.parse_ignore_round_bracket_contents_input.setText(_translate("SettingsDialog", "ignore content in round brackets（）"))
        self.parse_ignore_slim_round_bracket_contents_input.setText(_translate("SettingsDialog", "ignore content in slim round brackets ()"))
        self.parse_ignore_names_morphemizer_input.setText(_translate("SettingsDialog", "Ignore names found by the morphemizer"))
        self.parse_ignore_names_textfile_input.setText(_translate("SettingsDialog", "Ignore names found in \"names.txt\""))
        self.parse_ignore_suspended_cards_content_input.setText(_translate("SettingsDialog", "Ignore suspended cards"))
        self.restore_parse_defaults_button.setText(_translate("SettingsDialog", "Restore Default Parse Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parse_tab), _translate("SettingsDialog", "Parse"))
        self.skip_only_known_morphs_cards_input.setText(_translate("SettingsDialog", "Skip cards with only known morphs"))
        self.skip_unknown_morph_seen_today_cards_input.setText(_translate("SettingsDialog", "Skip cards that have unknown morphs already seen today"))
        self.skip_show_num_of_skipped_cards_input.setText(_translate("SettingsDialog", "Show \"skipped x cards\" notifications"))
        self.restore_skip_defaults_button.setText(_translate("SettingsDialog", "Restore Default Skip Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.skip_tab), _translate("SettingsDialog", "Skip"))
        self.recalc_on_sync_input.setText(_translate("SettingsDialog", "Recalc on sync"))
        self.label_16.setText(_translate("SettingsDialog", "Min. interval for known morphs:"))
        self.label_17.setText(_translate("SettingsDialog", "days"))
        self.restore_recalc_defaults_button.setText(_translate("SettingsDialog", "Restore Default Recalc Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recalc_tab), _translate("SettingsDialog", "Recalc"))
        self.label_14.setText(_translate("SettingsDialog", "Run recalc"))
        self.label_13.setText(_translate("SettingsDialog", "Open settings"))
        self.label_8.setText(_translate("SettingsDialog", "Browse ready cards with same unknown morph"))
        self.label_9.setText(_translate("SettingsDialog", "Browse all cards with same unknown morph"))
        self.label_10.setText(_translate("SettingsDialog", "Set card as known and skip"))
        self.label_11.setText(_translate("SettingsDialog", "Learn card now"))
        self.label_12.setText(_translate("SettingsDialog", "View card morphemes"))
        self.restore_shortcut_defaults_button.setText(_translate("SettingsDialog", "Restore Default Shortcut Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shortcuts_tab), _translate("SettingsDialog", "Shortcuts"))
        self.restore_all_defaults_button.setText(_translate("SettingsDialog", "Restore All Default Settings"))
        self.ankimorphs_version_label.setText(_translate("SettingsDialog", "AnkiMorphs version: x"))
        self.cancel_button.setText(_translate("SettingsDialog", "Cancel"))
        self.save_button.setText(_translate("SettingsDialog", "Save"))
