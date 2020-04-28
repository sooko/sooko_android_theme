from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.behaviors.touchripple import  TouchRippleButtonBehavior
from kivy.uix.label import Label
Config.set('graphics', 'height',770)
Config.set('graphics', 'width',  370)
from kivy.lang import Builder
Builder.load_file("kv/navleft.kv")
class AccountBar(BoxLayout):
    pass
class Btn(TouchRippleButtonBehavior,Label):
    pass
class ItemButton(FloatLayout):
    pass
class NavLeft(FloatLayout):
    def __init__(self, **kwargs):
        super(NavLeft,self).__init__(**kwargs)
    def select(self,text):
        # print(text)
        pass



