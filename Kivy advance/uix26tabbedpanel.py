from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout


class Tab(TabbedPanel):
    pass


class uix26TabbedPanelApp(App):
    def build(self):
        return Tab()


uix26TabbedPanelApp().run()
