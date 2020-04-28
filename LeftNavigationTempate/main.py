from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('graphics', 'height',770)
Config.set('graphics', 'width',  370)
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.lang import Builder
Builder.load_file("kv/ml.kv")
from kivy.app import App
from kivy.lang import Builder
from topnav import TopNav
from navleft import NavLeft
class Ml(FloatLayout):
    def __init__(self, **kwargs):
        super(Ml,self).__init__(**kwargs)
        self.navleft.select=self.on_select
    def on_select(self,dt):
        self.sm.current=dt
class MqttClient(App):
    def build(self):
        return Ml()
 
if __name__=="__main__":
    MqttClient().run()