from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class GriddemoApp(App):
    def build(self):
        grid_layout = GridLayout()
        grid_layout.cols = 3
        grid_layout.add_widget(Button(text="Button1"))
        grid_layout.add_widget(Button(text="Button2"))
        grid_layout.add_widget(Button(text="Button3"))
        grid_layout.add_widget(Button(text="Button4"))
        grid_layout.add_widget(Button(text="Button5"))
        grid_layout.add_widget(Button(text="Button6"))
        grid_layout.add_widget(Button(text="Button7"))
        grid_layout.add_widget(Button(text="Button8"))
        grid_layout.add_widget(Button(text="Button9"))
        grid_layout.add_widget(Button(text="*"))
        grid_layout.add_widget(Button(text="Button0"))
        grid_layout.add_widget(Button(text="#"))
        return grid_layout


if __name__ == "__main__":
    gridapp = GriddemoApp()
    gridapp.run()
