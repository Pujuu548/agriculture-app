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
        
        self.add_widget(Image(source="login page.png"))
        self.size_hint=(0.4,0.3)
        self.pos_hint={ "center_x": 0.5, "center_y":0.5}
        self.add_widget(Label(text="UserName",
                              font_size=20,
                              color="#00FFCE"))
        self.name = TextInput(multiline = False,padding_y=(20,20))
        self.add_widget(self.name)
        
        self.add_widget(Label(text="Password",
                              font_size=20,
                              color="#00FFCE"
                              ))
        self.Password=TextInput(multiline=False)
        self.add_widget(self.Password)
        
        
        
        #create a submit button
       
        self.submit = Button(text ="Submit",font_size=32,color="white",background_color="#00FFCE")
        #bind button
        self.submit.bind(on_press=self.Press)
        self.add_widget(self.submit)
        
        
    def Press(self,instance):
        name=self.name.text
        Password=self.Password.text
        
        self.add_widget(Label(text=f'WELCOME{name}!!!')) 
    
        
       
     
        
        
       
            
        
        


class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()