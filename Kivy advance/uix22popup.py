from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout


class PopupDemo(App):
    def build(self):
        layout = GridLayout(cols=1, padding=10)
        self.button = Button(text='Click here to view popup',
                             size_hint=(.8, .2), pos_hint={'x': .1, 'y': .1})
        layout.add_widget(self.button)
        self.button.bind(on_press=self.onButtonPress)
        return layout

    def onButtonPress(self, button):
        layout = GridLayout(cols=1, padding=10)
        popuplabel = Label(text='Welcome')
        closeButton = Button(text="Close")

        layout.add_widget(popuplabel)
        layout.add_widget(closeButton)

        popup = Popup(title='Demopopup', content=layout)

        popup.open()
        closeButton.bind(on_press=popup.dismiss)


PopupDemo().run()
