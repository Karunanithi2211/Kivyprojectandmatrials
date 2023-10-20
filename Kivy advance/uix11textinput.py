from kivy.app import App
from kivy.uix.textinput import TextInput


class SimpleApp(App):
    def build(self):
        t = TextInput(font_size=100)

        return t


SimpleApp().run()
