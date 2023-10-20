from kivy.app import App
from kivy.uix.button import Button


class KivyButton(App):
    def build(self):
        # btn = Button(text="Press Button", size_hint=(.2, .2), pos=(300, 240))
        btn = Button(text="Press Button", color=(1, 0, .65, 1), background_normal="onepiece.jpg",
                     size_hint=(.4, .4), pos_hint={"x": .39, "y": .3})

        return btn


root = KivyButton()
root.run()
