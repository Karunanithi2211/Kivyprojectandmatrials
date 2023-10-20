from kivy.app import App
from kivy.uix.button import Button


class SimpleApp(App):
    def build(self):
        def a(instance, value):
            print("Welcome bro")
        btn = Button(text="Welcome,", font_size=100)
        btn.bind(state=a)
        return btn


if __name__ == "__main__":
    SimpleApp().run()
