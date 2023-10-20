from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class LineEllipse1(Widget):
    pass


class LineEllipse2(Widget):
    pass


class LineEllipse3(Widget):
    pass


class LineCircle1(Widget):
    pass


class LineCircle2(Widget):
    pass


class LineCircle3(Widget):
    pass


class LineCircle4(Widget):
    pass


class LineRectangle(Widget):
    pass


class LineBezier(Widget):
    pass


class Simple2App(App):
    def build(self):
        root = GridLayout(cols=3, padding=50, spacing=100)

        root.add_widget(LineEllipse1())
        root.add_widget(LineEllipse2())
        root.add_widget(LineEllipse3())
        root.add_widget(LineCircle1())
        root.add_widget(LineCircle2())
        root.add_widget(LineCircle3())
        root.add_widget(LineCircle4())
        root.add_widget(LineRectangle())
        root.add_widget(LineBezier())
        return root


Simple2App().run()
