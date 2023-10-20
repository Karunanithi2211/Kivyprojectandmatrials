from kivy.app import App
# from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class GridLayoutEx(GridLayout):
    pass


class LoginApp(App):
    def build(self):

        return GridLayoutEx()


if __name__ == "__main__":
    g_app = LoginApp()
    g_app.run()
