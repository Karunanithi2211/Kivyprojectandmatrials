from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primaty_palette = 'Indigo'
        self.theme_cls.accent_palette = 'Red'
        return Builder.load_file('main.kv')


if __name__ == '__main__':
    main = MainApp()
    main.run()
