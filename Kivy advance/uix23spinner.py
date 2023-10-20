from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


class spinnerExample(App):
    def build(self):
        layout = FloatLayout()
        self.spinnerObject = Spinner(text='Python', values=(
            'Python', 'Java', 'PHP', 'C++', 'C'), background_color=(.22, .23, .13))
        self.spinnerObject.size_hint = (.3, .2)
        self.spinnerObject.pos_hint = {'x': .3, 'y': .75}
        layout.add_widget(self.spinnerObject)
        return layout


spinnerExample().run()
