from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout


class Stacklayoutdemo(App):
    def build(self):
        # lr=left to right,tb=top to bottom
        sl = StackLayout(orientation='lr-tb')

        button1 = Button(text='1', font_size=18, size_hint=(.1, .1))
        button2 = Button(text='2', font_size=18, size_hint=(.1, .1))
        button3 = Button(text='3', font_size=18, size_hint=(.1, .1))
        button4 = Button(text='4', font_size=18, size_hint=(.1, .1))
        button5 = Button(text='5', font_size=18, size_hint=(.1, .1))
        button6 = Button(text='6', font_size=18, size_hint=(.1, .1))
        button7 = Button(text='7', font_size=18, size_hint=(.1, .1))
        button8 = Button(text='8', font_size=18, size_hint=(.1, .1))
        button9 = Button(text='9', font_size=18, size_hint=(.1, .1))
        button0 = Button(text='0', font_size=18, size_hint=(.1, .1))

        sl.add_widget(button1)
        sl.add_widget(button2)
        sl.add_widget(button3)
        sl.add_widget(button4)
        sl.add_widget(button5)
        sl.add_widget(button6)
        sl.add_widget(button7)
        sl.add_widget(button8)
        sl.add_widget(button9)
        sl.add_widget(button0)
        return sl


Stacklayoutdemo().run()
