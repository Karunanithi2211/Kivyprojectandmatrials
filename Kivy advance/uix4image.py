from kivy.app import App
from kivy.uix.image import Image


class SimpleApp(App):
    def build(self):
        img = Image(source="onepiece.jpg")
        return img


if __name__ == "__main__":
    SimpleApp().run()
