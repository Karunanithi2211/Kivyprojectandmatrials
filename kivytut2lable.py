import kivy
from kivy.app import App
from kivy.uix.button import Label


class HelloKivy(App):
    def click_l(self, instance, value):
        print("user clicked bro")

    def build(self):
        lab = Label(text='[color=3333ff][i]Welcome[/i][/color] [ref=bro][color=ff3333][b]bro[/b][/color][/ref]',
                    font_size='50sp', markup=True)
        lab.bind(on_ref_press=self.click_l)
        return lab


kivyapp = HelloKivy()
kivyapp.run()
