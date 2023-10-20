from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
# from kivy.uix.floatlayout import FloatLayout


class SimpleApp(App):
    def build(self):

        b = ToggleButton(text="python", border=(26, 26, 26, 26), font_size=200)
        return b


SimpleApp().run()
