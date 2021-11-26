from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
Window.size=(560,800)   #---For Windows---
#Window.size=(720,1440)  
#Window.size=(720,1280)
del_mode = 1
minus = 1
mode = 1
sign = ["+","-","*","/","%","."]
Builder_string = '''
ScreenManager:
    Main:
<Main>:
    name : 'Calculator'
	BoxLayout:
		orientation:"vertical"
		size:root.width,root.height
		MDToolbar:
			title : 'CALCULATOR'
			font_style: 'H2'
			specific_text_color:1,1,1,1
		
		MDTextField:
			id: val1
			#hint_text: " Made in Python"
			mode: "rectangle"
			text : "  Made By : Tejinder Singh "
			halign : "right"
			font_size:26
			readonly : "True"
			size_hint:(1,.1)		
		
		TextInput:
			#hint_text: " Made By : Tejinder Singh(1917642), BTECH CSE - 2019"
			#mode: "rectangle"
			id: val
			text : "0"
			halign : "right"
			font_size:80
			readonly : "True"
			size_hint:(1,.2)
			
			
			
		GridLayout:
			cols:4
			rows:5
			
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:40
				text:"C"
				on_press: app.clear()
				md_bg_color : (0,1,0,.5)
				text_color: (1,1,1,1)
			
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:40
				text:"+/-"
				on_press: app.plusminus()
				md_bg_color : (1,1,1,.28)
				text_color: (1,1,1,1)
			
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:40
				text:"%"
				on_press: app.rem()
				md_bg_color : (1,1,1,.28)
				text_color: (1,1,1,1)
				
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:36
				text:"DEL"
				on_press: app.delete()
				md_bg_color : (1,1,1,.28)
				text_color: (1,1,1,1)
		
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:36
				text:"7"
				on_press: app.seven()
				text_color: (1,1,1,1)
				
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:36
				text:"8"
				on_press: app.eight()
				text_color: (1,1,1,1)
				
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:36
				text:"9"
				on_press: app.nine()
				text_color: (1,1,1,1)
				
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:40
				text:"/"
				on_press: app.div()
				md_bg_color : (1,1,1,.28)
				text_color: (1,1,1,1)
					
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:36
				text:"4"
				on_press: app.four() 
				text_color: (1,1,1,1)
				
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:36
				text:"5"
				on_press: app.five()
				text_color: (1,1,1,1)
				
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:36
				text:"6"
				on_press: app.six()
				text_color: (1,1,1,1)
			
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:40
				text:"*"
				on_press: app.mult()
				md_bg_color : (1,1,1,.28)
				text_color: (1,1,1,1)
					
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:36
				text:"1"
				on_press: app.one()
				text_color: (1,1,1,1)
				
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:36
				text:"2"
				on_press: app.two()
				text_color: (1,1,1,1)
				
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:36
				text:"3"
				on_press: app.three()
				text_color: (1,1,1,1)
			
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:40
				text:"-"
				on_press: app.sub()
				md_bg_color : (1,1,1,.28)
				text_color: (1,1,1,1)
					
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:36
				text:"0"
				on_press: app.zero()
				text_color: (1,1,1,1)
				
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:40
				text:"."
				on_press: app.dot()
				text_color: (1,1,1,1)
				
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:44
				text:"="
				on_press: app.equal()
				md_bg_color : (.9,.5,0,1)
				text_color: (1,1,1,1)
				
			MDRectangleFlatButton:
				size_hint:(.2,.2)
				font_size:40
				text:"+"
				on_press: app.add()
				md_bg_color : (1,1,1,.28)
				text_color: (1,1,1,1)
		
		

'''

class Main(Screen):
	pass
	
sm=ScreenManager()
sm.add_widget(Main(name='Calculator'))

class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.help_string = Builder.load_string(Builder_string)
		self.title = 'Calculator'
		return self.help_string
	
	def zero(self):
		global mode 
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		if string == "0" or mode == 0 :
			mode = 1
			self.help_string.get_screen('Calculator').ids.val.text = "0"
			self.help_string.get_screen('Calculator').ids.val1.text = "  Made By : Tejinder Singh "
		else :
			self.help_string.get_screen('Calculator').ids.val.text += "0"
		
	
	def one(self):
		global mode 
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		if string == "0" or mode == 0 :
			mode = 1
			self.help_string.get_screen('Calculator').ids.val.text = "1"
			self.help_string.get_screen('Calculator').ids.val1.text = "  Made By : Tejinder Singh "
		else :
			self.help_string.get_screen('Calculator').ids.val.text += "1"
	
	def two(self):
		global mode 
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		if string == "0" or mode == 0 :
			mode = 1
			self.help_string.get_screen('Calculator').ids.val.text = "2"
			self.help_string.get_screen('Calculator').ids.val1.text = "  Made By : Tejinder Singh "
		else :
			self.help_string.get_screen('Calculator').ids.val.text += "2"
	
	def three(self):
		global mode 
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		if string == "0" or mode == 0 :
			mode = 1
			self.help_string.get_screen('Calculator').ids.val.text = "3"
			self.help_string.get_screen('Calculator').ids.val1.text = "  Made By : Tejinder Singh "
		else :
			self.help_string.get_screen('Calculator').ids.val.text += "3"
	
	def four(self):
		global mode 
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		if string == "0" or mode == 0 :
			mode = 1
			self.help_string.get_screen('Calculator').ids.val.text = "4"
			self.help_string.get_screen('Calculator').ids.val1.text = "  Made By : Tejinder Singh "
		else :
			self.help_string.get_screen('Calculator').ids.val.text += "4"
	
	def five(self):
		global mode 
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		if string == "0" or mode == 0 :
			mode = 1
			self.help_string.get_screen('Calculator').ids.val.text = "5"
			self.help_string.get_screen('Calculator').ids.val1.text = "  Made By : Tejinder Singh "
		else :
			self.help_string.get_screen('Calculator').ids.val.text += "5"
	
	def six(self):
		global mode 
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		if string == "0" or mode == 0 :
			mode = 1
			self.help_string.get_screen('Calculator').ids.val.text = "6"
			self.help_string.get_screen('Calculator').ids.val1.text = "  Made By : Tejinder Singh "
		else :
			self.help_string.get_screen('Calculator').ids.val.text += "6"
	
	def seven(self):
		global mode 
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		if string == "0" or mode == 0 :
			mode = 1
			self.help_string.get_screen('Calculator').ids.val.text = "7"
			self.help_string.get_screen('Calculator').ids.val1.text = "  Made By : Tejinder Singh "
		else :
			self.help_string.get_screen('Calculator').ids.val.text += "7"
			self.help_string.get_screen('Calculator').ids.val1.text = "  Made By : Tejinder Singh "
	
	def eight(self):
		global mode 
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		if string == "0" or mode == 0 :
			mode = 1
			self.help_string.get_screen('Calculator').ids.val.text = "8"
			self.help_string.get_screen('Calculator').ids.val1.text = "  Made By : Tejinder Singh "
		else :
			self.help_string.get_screen('Calculator').ids.val.text += "8"
	
	def nine(self):
		global mode 
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		if string == "0" or mode == 0 :
			mode = 1
			self.help_string.get_screen('Calculator').ids.val.text = "9"
			self.help_string.get_screen('Calculator').ids.val1.text = "  Made By : Tejinder Singh "
		else :
			self.help_string.get_screen('Calculator').ids.val.text += "9"
		
	def add(self):
		global mode
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		length = len(string)
		a = string[length-1:length]
		if a not in sign :
			self.help_string.get_screen('Calculator').ids.val.text += "+"
			mode = 1
	
	def sub(self):
		global mode
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		length = len(string)
		a = string[length-1:length]
		if a not in sign :
			self.help_string.get_screen('Calculator').ids.val.text += "-"
			mode = 1
	
	def mult(self):
		global mode
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		length = len(string)
		a = string[length-1:length]
		if a not in sign :
			self.help_string.get_screen('Calculator').ids.val.text += "*"
			mode = 1
	
	def div(self):
		global mode
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		length = len(string)
		a = string[length-1:length]
		if a not in sign :
			self.help_string.get_screen('Calculator').ids.val.text += "/"
			mode = 1
	
	def rem(self):
		global mode
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		length = len(string)
		a = string[length-1:length]
		if a not in sign :
			self.help_string.get_screen('Calculator').ids.val.text += "%"
			mode = 1
	
	def dot(self):
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		length = len(string)
		a = string[length-1:length]
		if a not in sign :
			self.help_string.get_screen('Calculator').ids.val.text += "."
	
	def plusminus(self):
		global minus
		if minus == 1:
			string = str(self.help_string.get_screen('Calculator').ids.val.text)
			if string == "0" :
				self.help_string.get_screen('Calculator').ids.val.text = "-"
				minus = 0
			else :
				self.help_string.get_screen('Calculator').ids.val.text = "-" + self.help_string.get_screen('Calculator').ids.val.text
				minus = 0
	
	def clear(self):
		self.help_string.get_screen('Calculator').ids.val.text = "0"
		self.help_string.get_screen('Calculator').ids.val1.text = "  Made By : Tejinder Singh "
		
	def delete(self):
		global del_mode
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		length = len(string)
		if del_mode == 1 :
			self.help_string.get_screen('Calculator').ids.val.text = string[0:length-1]
		else :
			global mode 
			string0 = str(self.help_string.get_screen('Calculator').ids.val1.text)
			length1 = len(string0) 
			if string0 != "  Made By : Tejinder Singh " :
				mode = 1
				del_mode = 1
				self.help_string.get_screen('Calculator').ids.val.text = string0[0:length1-1] 
		if self.help_string.get_screen('Calculator').ids.val.text == "" :
			self.help_string.get_screen('Calculator').ids.val.text = "0"
			self.help_string.get_screen('Calculator').ids.val1.text = "  Made By : Tejinder Singh "

	def equal(self):
		string = str(self.help_string.get_screen('Calculator').ids.val.text)
		length = len(string)
		a = string[length-1:length]
		if a not in sign :
			global del_mode
			global mode 
			mode = 0
			del_mode = 0
			string = str(self.help_string.get_screen('Calculator').ids.val.text)
			result = eval(string)
			self.help_string.get_screen('Calculator').ids.val.text = str(round(result,2))
			self.help_string.get_screen('Calculator').ids.val1.text = string + "="
					
		b = self.help_string.get_screen('Calculator').ids.val.text[0:1]
		if b != "-" :
			global minus
			minus = 1		
		
MainApp().run()
#---MADE BY :  TEJINDER SINGH,BTECH-CSE 2019,1917642---

#---PCTE Institute of Engineering and Technology---

