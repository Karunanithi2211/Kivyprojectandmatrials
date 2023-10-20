from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('main.kv')

    def on_save(self, instance, value, date_range):
        self.root.ids.date_label.text = f'{str(date_range[0])} - {str(date_range[1])}'

    def on_cancel(self, instance, value):
        self.root.ids.date_label.text = 'You Clicked cancel'

    def show_date_picker(self):
        date_dialog = MDDatePicker(mode='range')
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()


if __name__ == '__main__':
    root = MainApp()
    root.run()
