import kivy
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class AnchorLayoutDemoApp(App):
    def build(self):
        ancl = AnchorLayout(anchor_x="left", anchor_y="center")
        btn1 = Button(text="Press here", size_hint=(0.5, 0.5))
        ancl.add_widget(btn1)

        ancl2 = AnchorLayout(anchor_x="right", anchor_y="center")
        btn2 = Button(text="Don't Press", size_hint=(0.3, 0.3))
        ancl2.add_widget(btn2)

        box = BoxLayout()
        box.add_widget(ancl)
        box.add_widget(ancl2)

        return box


if __name__ == "__main__":
    app1 = AnchorLayoutDemoApp()
    app1.run()
