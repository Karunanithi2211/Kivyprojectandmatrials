from kivy.app import App
from kivy.uix.progressbar import ProgressBar


class SimpleApp(App):
    def build(self):
        bar = ProgressBar(max=100)
        bar.value = 60
        return bar


if __name__ == "__main__":
    SimpleApp().run()
