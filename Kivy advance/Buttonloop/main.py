from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    some_text = 'Hello bro!'
    our_list = ['Luffy', 'Zoro', 'Sanji']

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primaty_palette = 'BlueGray'
        return Builder.load_file('main.kv')


if __name__ == '__main__':
    main = MainApp()
    main.run()
