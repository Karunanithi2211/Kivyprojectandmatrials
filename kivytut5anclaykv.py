import kivy
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class Grid_layout(GridLayout):
    pass


class Anchor_LayoutDemoApp(App):
    def build(self):

        return Grid_layout()


if __name__ == "__main__":
    app1 = Anchor_LayoutDemoApp()
    app1.run()
