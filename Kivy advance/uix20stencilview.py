from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.stencilview import StencilView


class SimpleApp(App):
    def build(self):
        s = StencilView()  # to drag for specified spawce
        sc = Scatter()
        s.add_widget(sc)
        sc.add_widget(Label(text='welcome'))
        return s


SimpleApp().run()
