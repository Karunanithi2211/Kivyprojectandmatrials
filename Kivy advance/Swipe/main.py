from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('main.kv')

    def on_swipe_left(self):
        self.root.ids.toolbar.title = "Ypu swiped Left"

    def on_swipe_right(self):
        self.root.ids.toolbar.title = "Ypu swiped Right"


MainApp().run()
