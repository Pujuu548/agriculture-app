import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

class  MyGridLayout(GridLayout):
       
    
    def __init__(self,**kwargs):
        super(MyGridLayout,self).__init__(**kwargs)
        self.cols = 1
       
        self.add_widget(Image(source="about.jpeg"))
        self.add_widget(Label(text="Agriculture is the most significant source of income for the central and state\n governments. \nThe government of the country has substantial revenue from rising land revenue. \nAlso, the movement of agricultural goods helps generate revenue for the Indian\n railways, which helps the government in revenue generation.\nThe study has found that incorrect and inappropriate application of \nfertilisers by farmers to gain bumper yield leads to the deterioration of soil,\n resulting in lower production. This creates a long-term impact in national \nfood security.\nso here we are helping you to get proper information of the fertilizers\n and manures for farming",
                             
                              font_size=20,
                              color="#00FFCE"
                              ))
class MyApp(App):
        def build(self):
          return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()