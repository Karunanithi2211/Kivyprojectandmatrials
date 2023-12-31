from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class Float_LayourApp(App):

    def build(self):

        Layout = FloatLayout(size=(300, 300))
        btn = Button(text='kivy',
                     size_hint=(.3, .5),
                     background_color=(.6, .7, .7, 1),
                     pos_hint={'x': .4, 'y': .3})

        Layout.add_widget(btn)

        return Layout


root = Float_LayourApp()
root.run()
