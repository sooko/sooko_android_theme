from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from tigaD2 import TigaD
Builder.load_string("""
<Ml>:
    GridLayout:
        id:gd
        cols:2

""")
from kivy.clock import Clock
import time
class Ml(FloatLayout):
    def __init__(self, **kwargs):
        super(Ml,self).__init__(**kwargs)
        Clock.schedule_once(self.delay,1)
    def delay(self,dt):
        self.ids["gd"].add_widget(TigaD())
        # time.sleep(1)
        Clock.schedule_once(self.delay1,1)
    def delay1(self,dt):
        self.ids["gd"].add_widget(TigaD())
        




class Ap(App):
    def build(self):
        return Ml()

if __name__=="__main__":
    Ap().run()