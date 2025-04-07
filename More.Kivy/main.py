'''from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Bokita pasion')
    
if __name__ == '__main__':
    MyApp().run()
    '''

'''from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MyApp(MDApp):
    def build(self):
        return MDLabel(text="Auronplay",
    halign="center")

if __name__ =='__main__':
    MyApp().run()
    '''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.label = Label(text="Hola miundo")
        self.add_widget(self.label)
        btn = Button(text="Cambiar hola fiugi")
        btn.bind(on_press=self.change_text)
        self.add_widget(btn)

    def change_text(self, instance):
        self.label.text = "Has precionado el boton"

class TestApp(App):
    def build(self):
        return MyBoxLayout()
    
TestApp().run()

