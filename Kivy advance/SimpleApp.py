from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class ScatterTextWidget(BoxLayout):
    pass


class SimpleApp(App):
    def build(self):
        return ScatterTextWidget()


SimpleApp().run()
