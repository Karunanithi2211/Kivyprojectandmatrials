from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton


class Demo(MDApp):
    def build(self):
        screen = Screen()

        btn = MDRectangleFlatButton(text='Submit', pos_hint={
                                    'center_x': .5, 'center_y': .3}, on_release=self.btnfunc)
        screen.add_widget(btn)
        # btn.bind(on_press=self.btnfunc)

        return screen

    def btnfunc(self, onj):
        print('Button is pressed!!')


if __name__ == '__main__':
    Demo().run()
