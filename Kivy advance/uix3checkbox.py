from kivy.app import App
from kivy.uix.checkbox import CheckBox


class SimpleApp(App):
    def build(self):
        def on_checkbox_active(checkbox, value):
            if value:
                print("The checkbox", checkbox, "is active")
            else:
                print("The checkbox", checkbox, "is inactive")

        checkbox = CheckBox()
        checkbox.bind(active=on_checkbox_active)
        return checkbox


if __name__ == "__main__":
    SimpleApp().run()
