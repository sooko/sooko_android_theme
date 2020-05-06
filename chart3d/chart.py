from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.properties import StringProperty,NumericProperty,ListProperty,BooleanProperty,ObjectProperty,DictProperty
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color,Line,Rotate,Translate,PopMatrix,PushMatrix,Rectangle
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from plot import Plot
Builder.load_file("kv/chart.kv")
class Label_x(Label):
    pass
class Label_y(Label):
    pass
class Mayor_x(Widget):
    pass
class Mayor_y(Widget):
    pass
class Black(Widget):
    def __init__(self, **kwargs):
        super(Black,self).__init__(**kwargs)
class Chart(FloatLayout):
    cols=NumericProperty(1)
    major_x=NumericProperty(10)
    major_y=NumericProperty(10)
    max_x  =NumericProperty(100)
    max_y  =NumericProperty(100)
    rp=ObjectProperty(None)
    plt=ObjectProperty(None)
    rpl=ObjectProperty(None)
    rply=ObjectProperty(None)
    def __init__(self, **kwargs):
        super(Chart,self).__init__(**kwargs)
        self.plt=self.ids["plt"]
        self.rpl=self.ids["root_plot_label_x"]
        self.rply=self.ids["root_plot_label_y"]
        

    def change_size(self):
        self.a=Mayor_x
        self.b=Mayor_y
        self.rp=self.ids["root_plot"]
        self.rp.clear_widgets()
        self.rpl.clear_widgets()
        self.rply.clear_widgets()
        for i in range(self.major_x):
            self.rp.add_widget(self.a(pos=(self.rp.width/self.major_x*i+self.rp.x , self.rp.y)))
            self.rpl.add_widget(Label_x(text=str((i*self.max_x)+self.max_x)))
        for i in range(self.major_y):
            self.rp.add_widget(self.b(pos=(self.rp.x , self.rp.height/self.major_y*i+self.rp.y)))
            self.rply.add_widget(Label_y(text=str(self.max_x-(i*self.major_y))))
    def on_touch_down(self, touch):
        self.plt.red.points=[self.plt.x,self.plt.y,self.plt.width+self.plt.x,self.plt.height+self.plt.y]
        return super(Chart,self).on_touch_down(touch)

class My(App):
    def build(self):
        return Chart()
if __name__=="__main__":
    My().run()
