from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('main.kv')

    def get_time(self, instance, time):
        self.root.ids.time_label.text = str(time)

    def on_cancel(self, instance, time):
        self.root.ids.time_label.text = "You Canceled"

    def show_time_picker(self):
        from datetime import datetime
        default_time = datetime.strptime("4:20:00", "%H:%M:%S").time()

        time_dialog = MDTimePicker()

        time_dialog.set_time(default_time)
        time_dialog.bind(on_cancel=self.on_cancel, time=self.get_time)
        time_dialog.open()


MainApp().run()
