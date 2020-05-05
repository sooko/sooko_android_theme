from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.properties import StringProperty,NumericProperty,ListProperty,BooleanProperty
from kivy.clock import Clock
Builder.load_file("kv/chart3d.kv")
from kivy.uix.widget import Widget
class Black(Widget):
    pass
class LinePlot(Widget):
    points=ListProperty([])
    x_point=NumericProperty(0)
    y_point=NumericProperty(0)
    width_area=NumericProperty(0)
    height_area=NumericProperty(0)
    geserkiri=NumericProperty(0)
    max_x=NumericProperty(100)
    max_y=NumericProperty(100)
    realtime=BooleanProperty(0)
    def __init__(self, **kwargs):
        super(LinePlot,self).__init__(**kwargs)
    def on_parent(self,*args):
        Clock.schedule_once(self.delay,.5)
        self.width_area=self.width
        self.height_area=self.height
        self.x_point=self.x
        self.y_point=self.y
    def delay(self,dt):
        self.x_point=self.x
        self.y_point=self.y
        self.width_area=self.width
        self.height_area=self.height
        self.points=[(self.x_point,self.y_point)]
    def on_size(self,*args):
        self.x_point=self.x
        self.y_point=self.y
        self.width_area=self.width
        self.height_area=self.height
    def on_pos(self,*args):
        self.x_point=self.x
        self.y_point=self.y
        self.width_area=self.width
        self.height_area=self.height
    def draw_line(self,xy,laju_x):
        a=self.x_point+self.width/self.max_x*xy[0]
        b=self.y_point+self.height/self.max_y*xy[1]
        self.points.append((a,b))
        print(len(self.points))
        if xy[0]>self.max_x:
            self.geserkiri-=self.width/self.max_x/laju_x
            self.points.remove(self.points[0])
class Chart3d(FloatLayout):
    count=NumericProperty(0)
    laju_x=NumericProperty(1)
    def __init__(self,*args, **kwargs):
        super(Chart3d,self).__init__(*args,**kwargs)
        Clock.schedule_once(self.delay,1)
    def delay(self,dt):
        Clock.schedule_interval(self.timer,.1)
    def timer(self,dt):
        self.count+=self.laju_x
        self.rl.draw_line([self.count,self.sld.value],self.laju_x)
        
class C(App):
    def build(self):
        return Chart3d()
if __name__=="__main__":
    C().run()

