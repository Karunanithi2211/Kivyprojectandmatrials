import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
kivy_as_a_file = Builder .load_file("myfirstkivy.kv")


class MyFirstWidget(Widget):
    pass


class MyFirstKivyApp(App):
    def build(self):
        return kivy_as_a_file


if __name__ == "__main__":
    kv_app = MyFirstKivyApp()
    kv_app.run()
