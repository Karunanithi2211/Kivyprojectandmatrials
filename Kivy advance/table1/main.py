from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class MainApp(MDApp):
    def build(self):
        screen = Screen()
        tabel = MDDataTable(
            pos_hint={'center_x': .5, 'center_y': .5},
            size_hint=(.9, .6),
            check=True,
            use_pagination=True,  # page split aganu
            rows_num=3,
            pagination_menu_height='240dp',
            pagination_menu_pos='auto',
            background_color=[1, 0, 0, .5],
            column_data=[
                ("First Name", dp(30)),
                ("Last Name", dp(30)),
                ("Email Address", dp(30)),
                ("Phone Number", dp(30)),
            ],
            row_data=[
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
                ("kavin", "M", "kavin@gmail.com", "81828182"),
            ]
        )
        tabel.bind(on_check_press=self.checked)
        tabel.bind(on_row_press=self.row_checked)

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

        screen.add_widget(tabel)
        return screen

    def checked(self, instance_table, current_row):
        print(instance_table, current_row)

    def row_checked(self, instance_table, instance_row):
        print(instance_table, instance_row)


MainApp().run()
