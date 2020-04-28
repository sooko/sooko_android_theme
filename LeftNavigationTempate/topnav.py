from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.behaviors.touchripple import  TouchRippleButtonBehavior
from kivy.uix.label import Label
Builder.load_file("kv/topnav.kv")
class TopNav(BoxLayout):
    def __init__(self, **kwargs):
        self.register_event_type("on_menu_press")
        super(TopNav,self).__init__(**kwargs)
    def press_menu(self):
        self.dispatch("on_menu_press")
    def on_menu_press(self):
        pass


class Btn(TouchRippleButtonBehavior,Label):
    pass
class BtnImg(TouchRippleButtonBehavior,Image):
    pass
