from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.spinner import Spinner
from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'resizable', True)


class spinnerExample(App):
    def build(self):
        layout = FloatLayout()
        self.spinnerObject = Spinner(text='Python', values=(
            'Python', 'Java', 'PHP', 'C++', 'C'), background_color=(.22, .23, .13))
        self.spinnerObject.size_hint = (.3, .2)
        self.spinnerObject.pos_hint = {'x': .35, 'y': .75}
        layout.add_widget(self.spinnerObject)
        self.spinnerObject.bind(text=self.onspinnerselect)
        self.spinnerselection = Label(
            text='Selected value in spinner is %s' % self.spinnerObject.text)
        layout.add_widget(self.spinnerselection)
        self.spinnerselection.pos_hint = {'x': .01, 'y': .1}
        return layout

    def onspinnerselect(self, spinner, text):
        self.spinnerselection.text = 'Selected value in spinner is %s' % self.spinnerObject.text
        print('The spinner ', spinner, 'have ', text)


spinnerExample().run()
