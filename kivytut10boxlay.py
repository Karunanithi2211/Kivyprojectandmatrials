from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class BoxLayoutDemo(App):
    def build(self):
        superbox = BoxLayout(orientation="vertical")
        horizontalbox = BoxLayout(orientation="horizontal")
        button1 = Button(text="One")
        button2 = Button(text="Two")
        horizontalbox.add_widget(button1)
        horizontalbox.add_widget(button2)
        verticalbox = BoxLayout(orientation="vertical")
        button3 = Button(text="Three")
        button4 = Button(text="Four")
        verticalbox.add_widget(button3)
        verticalbox.add_widget(button4)
        superbox.add_widget(horizontalbox)
        superbox.add_widget(verticalbox)
        return superbox


if __name__ == "__main__":
    app = BoxLayoutDemo()
    app.run()
