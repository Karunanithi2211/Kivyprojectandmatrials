from kivy.app import App
from kivy.uix.image import AsyncImage


class MyKivyApp(App):

    def build(self):
        return AsyncImage(source="https://media.evo.co.uk/image/private/s--uq3A8bwR--/v1556223011/evo/2019/04/jeskolucerne-stevenwade-3.jpg")


MyKivyApp().run()
