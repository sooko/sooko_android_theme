from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.properties import StringProperty,NumericProperty,ListProperty,BooleanProperty,ObjectProperty,DictProperty
from kivy.clock import Clock
Builder.load_file("kv/plot.kv")
from kivy.uix.widget import Widget
from kivy.graphics import Color,Line,Rotate,Translate,PopMatrix,PushMatrix
from kivy.metrics import sp,dp
class Plot(Widget):
    red         =ObjectProperty(None)
    yellow      =ObjectProperty(None)
    blue        =ObjectProperty(None)
    pink        =ObjectProperty(None)
    orange      =ObjectProperty(None)
    grey        =ObjectProperty(None)
    white       =ObjectProperty(None)
    purple      =ObjectProperty(None)
    aqua        =ObjectProperty(None)
    navy        =ObjectProperty(None)
    coral       =ObjectProperty(None)
    maroon      =ObjectProperty(None)
    teal        =ObjectProperty(None)
    violet      =ObjectProperty(None)
    amber       =ObjectProperty(None)
    cagak       =ObjectProperty(None)
    tebal       =NumericProperty(2)
    max_xx      =NumericProperty(100)
    max_yy      =NumericProperty(100)
    min_xx      =NumericProperty(0)
    min_yy      =NumericProperty(0)
    major_xx    =ObjectProperty(None)
    major_yy    =ObjectProperty(None)    
    jal=[50,50,60,60]
    def __init__(self, **kwargs):
        super(Plot,self).__init__(**kwargs)
        with self.canvas.before:
            self.pushmatrix=PushMatrix()
            self.translate=Translate(x=0,y=0,z=0)
            self.r      =Color(rgba=(1,0,0,1))
            self.red    =Line(points=[],width=self.tebal)
            self.g      =Color(rgba=(0,1,0,1))
            self.green  =Line(points=[],width=self.tebal)
            self.b      =Color(rgba=(0,0,1,1))
            self.blue   =Line(points=[],width=self.tebal)
            self.yel    =Color(rgba=(1,1,0,1))
            self.yellow =Line(points=[],width=self.tebal)
            self.m      =Color(rgba=(.5,0,0,1))
            self.maroon =Line(points=[],width=self.tebal)
            self.pur    =Color(rgba=(1,0,1,1))
            self.purple =Line(points=[],width=self.tebal)
            self.p      =Color(rgba=(1,.4,.7,1))
            self.pink   =Line(points=[],width=self.tebal)
            self.a      =Color(rgba=(0,1,1,1))
            self.aqua   =Line(points=[],width=self.tebal)
            self.na     =Color(rgba=(0,0,.5,1))
            self.navy   =Line(points=[],width=self.tebal)
            self.tea    =Color(rgba=(0,.5,.5,1))
            self.teal   =Line(points=[],width=self.tebal)
            self.vio    =Color(rgba=(1,.5,1,1))
            self.violet =Line(points=[],width=self.tebal)
            self.amb    =Color(rgba=(1,.5,.2,1))
            self.amber  =Line(points=[],width=self.tebal)
            self.gr     =Color(rgba=(103/255, 128/255, 159/255, 1))
            self.grey   =Line(points=[],width=self.tebal)
            self.putih  =Color(rgba=(1,1,1,1))
            self.white  =Line(points=[],width=self.tebal)
        with self.canvas.after:
            self.popmatrix=PopMatrix()
            self.cag        =Color(rgba=(1,1,1,1))          
            self.cagak      =Line(points=[],width=sp(1.5))
    def on_size(self,*args):
        self.cagak.points=[self.x,self.y,self.x,self.height+self.y,
                           self.x,self.y,self.width+self.x,self.y]
    def on_pos(self,*args):
        print(self.pos)
        self.cagak.points=[self.x,self.y,self.x,self.height+self.y,
                           self.x,self.y,self.width+self.x,self.y]
    def set_configure(self,max_xx,max_yy,tt):
        pass
    def draw_Plot(self,xx,yy,times):
        pass
