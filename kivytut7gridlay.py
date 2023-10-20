from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class GriddemoApp(App):
    def build(self):
        grid_layout = GridLayout()
        grid_layout.cols = 3
        grid_layout.row_force_default = True
        grid_layout.row_default_height = 40
        grid_layout.col_force_default = True
        grid_layout.col_default_width = 200
        grid_layout.add_widget(Button(text="Button1", font_size="30sp"))
        grid_layout.add_widget(Button(text="Button1", font_size="30sp"))
        grid_layout.add_widget(Button(text="Button1", font_size="30sp"))
        grid_layout.add_widget(Button(text="Button1", font_size="30sp"))
        grid_layout.add_widget(Button(text="Button2", font_size="30sp"))
        grid_layout.add_widget(Button(text="Button3", font_size="30sp"))
        grid_layout.add_widget(Button(text="Button4", font_size="30sp"))
        grid_layout.add_widget(Button(text="Button5", font_size="30sp"))
        grid_layout.add_widget(Button(text="Button6", font_size="30sp"))
        grid_layout.add_widget(Button(text="Button7", font_size="30sp"))
        grid_layout.add_widget(Button(text="Button8", font_size="30sp"))
        grid_layout.add_widget(Button(text="Button9", font_size="30sp"))
        grid_layout.add_widget(Button(text="*", font_size="30sp"))
        grid_layout.add_widget(Button(text="Button0", font_size="30sp"))
        grid_layout.add_widget(Button(text="#", font_size="30sp"))
        return grid_layout


if __name__ == "__main__":
    gridapp = GriddemoApp()
    gridapp.run()
