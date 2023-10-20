from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.theme_palette = 'BlueGray'
        return Builder.load_file('main.kv')

    def logger(self):
        self.root.ids.welcome_label.text = f'Hi {self.root.ids.user.text}!'

    def clear(self):
        self.root.ids.welcome_label.text = "Welcome"
        self.root.ids.user.text = ''
        self.root.ids.password.text = ''


if __name__ == '__main__':
    root = MainApp()
    root.run()
