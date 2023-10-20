from kivy.app import App
from kivy.uix.video import Video


class SimpleApp(App):
    def build(self):
        s = Video(source="onepiece.mkv", play=True)
        return s


if __name__ == "__main__":
    SimpleApp().run()
