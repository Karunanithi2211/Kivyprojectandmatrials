from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDBottomAppBar


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primaty_palette = 'BlueGray'
        return Builder.load_file('man.kv')


if __name__ == '__main__':
    main = MainApp()
    main.run()
