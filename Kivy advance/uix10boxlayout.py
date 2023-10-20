from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from time import sleep


class Mainmenu(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'

        btn = Button(text="Start")
        btn.bind(on_release=self.trigger)
        self.add_widget(btn)

        self.MyList = ('My', 'first', 'Progress', 'Bar',
                       'five', 'six', 'seven', 'eight')
        self.i = 0
        self.pb = ProgressBar(max=len(self.MyList), value=0)
        self.add_widget(self.pb)

    def trigger(self, *args):
        self.i = 0
        self.pb.value = 0

        Clock.schedule_interval(self.heavyfunc, 0.1)

    def heavyfunc(self, dt):
        sleep(.5)
        print(self.MyList[self.i])
        self.i += 1
        self.pb.value += 1

        if self.i >= len(self.MyList):
            Clock.unschedule(self.heavyfunc)
            print('unscheduled')


class testApp(App):
    def build(self):
        return Mainmenu()


root = testApp()
root.run()
