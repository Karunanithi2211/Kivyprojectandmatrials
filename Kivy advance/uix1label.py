from kivy.app import App
from kivy.uix.label import Label


class SimpleApp(App):
    def build(self):
        l = Label(text="Welcome", font_size=150)
        return l


if __name__ == "__main__":
    SimpleApp().run()
