from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button


class Anchor_LayoutDemo(App):
    def build(self):
        anchorLayout1 = AnchorLayout(anchor_x='left', anchor_y='center')
        button1 = Button(text='Python', size_hint=(.4, .4),
                         background_color=(.6, 1, .7, 1))
        anchorLayout1.add_widget(button1)

        anchorLayout2 = AnchorLayout(anchor_x='center', anchor_y='top')
        button2 = Button(text='kivy', size_hint=(.2, .2),
                         background_color=(.6, 1, .7, 1))
        anchorLayout2.add_widget(button2)

        anchorLayout3 = AnchorLayout(anchor_x='right', anchor_y='center')
        button3 = Button(text='OpenGl', size_hint=(.4, .4),
                         background_color=(.6, 1, .7, 1))
        anchorLayout3.add_widget(button3)

        boxlayout = BoxLayout()

        boxlayout.add_widget(anchorLayout1)
        boxlayout.add_widget(anchorLayout2)
        boxlayout.add_widget(anchorLayout3)

        return boxlayout


Anchor_LayoutDemo().run()
