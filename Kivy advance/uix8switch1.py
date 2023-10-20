import kivy
from kivy.app import App
from kivy.uix.switch import Switch
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class SimpleSwitch(GridLayout):
    def __init__(self, **kwargs):
        super(SimpleSwitch, self).__init__(**kwargs)

        self.cols = 2
        self.add_widget(Label(text="Switch"))
        self.setting_sample = Switch(active=False)
        self.add_widget(self.setting_sample)
        self.setting_sample.bind(active=self.switch_callback)

    def switch_callback(self, switchObject, switchValue):
        if (switchValue):
            print('Switch is ON:):):)')
        else:
            print('Switch is OFF:(:(:(')


class SwitchApp(App):
    def build(self):
        return SimpleSwitch()


if __name__ == "__main__":
    root = SwitchApp()
    root.run()
