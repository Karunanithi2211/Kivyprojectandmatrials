from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout


class SimpleApp(App):
    def build(self):
        layout = PageLayout()
        layout.add_widget(Button(text='hello', background_color='red'))
        layout.add_widget(Button(text='h', background_color='green'))
        layout.add_widget(Button(text='hlo', background_color='yellow'))
        layout.add_widget(Button(text='ho', background_color='white'))
        return layout


SimpleApp().run(

)
