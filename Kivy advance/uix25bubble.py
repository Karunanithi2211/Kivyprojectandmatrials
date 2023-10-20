from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.bubble import Bubble
from kivy.properties import ObjectProperty


class Cut_copy_paste(Bubble):
    pass


class BubbleDemo(FloatLayout):
    def __init__(self, **kwargs):
        super(BubbleDemo, self).__init__(**kwargs)
        self.but_bubble = Button(text='Press to show Bubble')
        self.but_bubble.bind(on_release=self.show_bubble)
        self.add_widget(self.but_bubble)
        self.bubb = Cut_copy_paste()

    def show_bubble(self, *l):
        self.add_widget(self.bubb)


class uix25BubbleApp(App):
    def build(self):
        return BubbleDemo()


uix25BubbleApp().run()
