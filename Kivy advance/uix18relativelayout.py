from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder

res = Builder.load_string('''
BoxLayout:
    Label:
        text:'left'
    Button:
        text:'middle'
        on_touch_down: print('Middle:{}'.format(args[1].pos))
    RelativeLayout:
        on_touch_down: print('Relative:{}'.format(args[1].pos))
    Button:
        text:'right'
        on_touch_down: print('Right: {}'.format(args[1].pos))
''')


class SimpleApp(App):
    def build(self):
        return res


SimpleApp().run()
