import kivy
from kivy.app import App
from kivy.uix.label import Label


class MyKivyApp(App):
    def build(self):
        return Label(text="Hello World!")


MyKivyApp().run()
