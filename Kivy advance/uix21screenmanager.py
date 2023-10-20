from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import time
import random

# BoxLayout = BoxLayout()
# FadeTransition = FadeTransition()


class Firstscreen(Screen):
    pass


class Secondscreen(Screen):
    pass


class ColourScreen(Screen):
    colour = ListProperty([1., 0., 0., 1.])


class Myscreenmanager(ScreenManager):
    def new_colour_screen(self):
        name = str(time.time())
        s = ColourScreen(name=name,
                         colour=[random.random() for _ in range(3)]+[1])
        self.add_widget(s)
        self.current = name


# to use fade transition importing into it
rootwidget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition 
Myscreenmanager:
    transition: FadeTransition()
    Firstscreen:
    Secondscreen:
<Firstscreen>:
    name:'first'
    BoxLayout:
        orientation:'vertical'
        Label:
            text:'first screen!'
            font_size:30
        Image:
            source:'onepiece.jpg'
            allow_stretch:False
            keep_ratio:False
        BoxLayout:
            Button:
                text:'goto second screen'
                font_size:30
                on_release: app.root.current = 'second'
        
            Button:
                text:'goto random screen'
                font_size:30
                on_release: app.root.new_colour_screen()

<Secondscreen>:
    name:'second'
    BoxLayout:
        orientation:'vertical'
        Label:
            text:'second screen!'
            font_size:30
        Image:
            source:'jesko.jpg'
            allow_stretch:False
            keep_ratio:False
        BoxLayout:
            Button:
                text:'goto first screen'
                font_size:30
                on_release: app.root.current = 'first'
        
            Button:
                text:'goto random screen'
                font_size:30
                on_release: app.root.new_colour_screen()

<ColourScreen>:
    BoxLayout:
        orientation:'vertical'
        Label:
            text:'colour {:.2},{:.2},{:.2} screen'.format(*root.colour[:3])
            font_size:30
        Widget:
            canvas:
                Color:
                    rgba: root.colour
                Ellipse:
                    pos: self.pos
                    size: self.size
        BoxLayout:
            Button:
                text:'goto first screen'
                font_size:30
                on_release: app.root.current = 'first'
        
            Button:
                text:'goto second screen'
                font_size:30
                on_release: app.root.new_colour_screen()
''')


class screenManagerApp(App):
    def build(self):
        return rootwidget


screenManagerApp().run()
