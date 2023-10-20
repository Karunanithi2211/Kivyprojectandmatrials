from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image


class SimpleApp(App):
    def build(self):
        s = Scatter()
        s.add_widget(Image(source='onepiece.jpg'))
        return s


SimpleApp().run()
