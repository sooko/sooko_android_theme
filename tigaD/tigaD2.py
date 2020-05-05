
from kivy.config import Config
Config.set('graphics', 'height',  770)
Config.set('graphics', 'width',370)
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy3dgui.layout3d import Layout3D,Node
from kivy.properties import NumericProperty,ListProperty
from kivy.animation import Animation
from kivy.clock import Clock
Builder.load_file("kv/tigaD2.kv")
class Td(Layout3D):
    pass
class Tl(Layout3D):
    pass
class NodeX(Node):
    pass
class NodeY(Node):
    pass
class TigaD(FloatLayout):
    pitch=NumericProperty(0)
    tp0=0
    tp1=0
    panjang=NumericProperty(1)
    lebar=NumericProperty(1)
    pos_axis_z=NumericProperty(0)
    pos_axis_x=NumericProperty(0)
    pos_axis_y=NumericProperty(0)
    def __init__(self, **kwargs):
        super(TigaD,self).__init__(**kwargs)
        # Clock.schedule_once(self.delay,1)
    def start_anim(self):
        pass
    # def stop_anim(self):
    #     self.anim.stop(self)
    def delay(self,dt):
        self.panjang=self.width
        self.lebar=self.height
    def on_touch_move(self, touch):
        # if touch.pos[0]<self.tp0:
        #     self.yaw-=1
        #     self.tp0=touch.pos[0]
        # if touch.pos[0]>self.tp0:
        #     self.yaw+=1
        #     self.tp0=touch.pos[0]
        if touch.pos[1]<self.tp1:
            self.pitch+=1
            self.tp1=touch.pos[1]
        if touch.pos[1]>self.tp1:
            self.pitch-=1
            self.tp1=touch.pos[1]
        # print(self.pitch)
        return super(TigaD,self).on_touch_move(touch)
from kivy.app import App
class Tracer(App):
    def build(self):
        return TigaD()
if __name__=="__main__":
    Tracer().run()
    
