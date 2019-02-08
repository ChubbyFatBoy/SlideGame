from pyglet.window import Window
from pyglet.text import Label
import koumpi, resources, pyglet

options = {}

def reslabel(option, width, height, batch):
	global opt
	opt = option
	if opt == 0:
		label = Label(text="1024x768", font_name='Comic Sans', font_size=18, x=width/2, y=height/2, anchor_x='center', anchor_y='center', batch=batch)
		opt = 1
		return label
	if opt == 1:
		label = Label(text="800x600", font_name='Comic Sans', font_size=18, x=width/2, y=height/2, anchor_x='center', anchor_y='center', batch=batch)
		opt = 0
		return label

def loadres():
	global options
	with open("../config/config.txt") as f:
		for line in f:
			(key, val) = line.split()
			options[str(key)] = val
	return options

def changeres1():
	global menu
	options = open("../config/config.txt", "w")
	options.write("option 2\nwidth 1024\nheight 768")
	for j in range(5):
		menu[j].delete()
	menu = create(1024, 768, cbatch)

def changeres2():
	global menu
	options = open("../config/config.txt", "w")
	options.write("option 1\nwidth 800\nheight 600")
	for j in range(5):
		menu[j].delete()
	menu = create(800, 600, cbatch)

def create(width, height, batch):
	global menu, cwidth, cheight, cbatch
	cwidth = width
	cheight = height
	cbatch = batch
	res_label = reslabel(0, width, height, batch)
	apply_button = koumpi.buttoncreate(width*2/5, height*1/10, resources.apply_button, batch=batch)
	back_button = koumpi.buttoncreate(width*3/5, height*1/10, resources.back_button, batch=batch)
	left_res  = koumpi.buttoncreate(width*1/5, height/2, resources.left_button, batch=batch)
	right_res = koumpi.buttoncreate(width*4/5, height/2, resources.right_button, batch=batch)
	menu = [res_label, apply_button, back_button, left_res, right_res]
	if width == 1024:
		for j in range(5):
			menu[j].scale = 0.5
	elif width == 800:
		for j in range(5):
			menu[j].scale = 0.4
	return menu

def press(x, y, button):
	global menu
	for n in range(5):
		if button == pyglet.window.mouse.LEFT:
			if n != 0:			
				if x > menu[n].x - menu[n].width/2 and x < menu[n].x + menu[n].width/2:
					if y > menu[n].y - menu[n].width/2 and y < menu[n].y + menu[n].height/2:
						menu[n].image = resources.option_press
						if n == 3:
							menu[n].image = resources.left_press
						elif n == 4:
							menu[n].image = resources.right_press

def release(x, y, button):
	global menu
	for n in range(5):
		if button == pyglet.window.mouse.LEFT:
			if n != 0:
				if x > menu[n].x - menu[n].width/2 and x < menu[n].x + menu[n].width/2:
					if y > menu[n].y - menu[n].height/2 and y < menu[n].y + menu[n].height/2:
						if n == 1:
							menu[n].image = resources.apply_hover
							return 0
						elif n == 2:
							menu[n].image = resources.back_hover
							return 1
						elif n == 3:
							menu[n].image =resources.left_hover
							menu[0].delete()
							menu[0] = reslabel(1, cwidth, cheight, cbatch)
						elif n == 4:
							menu[n].image = resources.right_hover
							menu[0].delete()
							menu[0] = reslabel(0, cwidth, cheight, cbatch)
def motion(x, y):
	global menu
	for n in range(5):
		if n != 0:			
			if x > menu[n].x - menu[n].width/2 and x < menu[n].x + menu[n].width/2:
				if y > menu[n].y - menu[n].height/2 and y < menu[n].y + menu[n].height/2:
					if n == 1:
						menu[n].image = resources.apply_hover
					elif n == 2:
						menu[n].image = resources.back_hover
					elif n == 3:
						menu[n].image =resources.left_hover
					elif n == 4:
						menu[n].image = resources.right_hover
				else:
					if n == 1:
						menu[n].image = resources.apply_button
					elif n == 2:
						menu[n].image = resources.back_button
					elif n == 3:
						menu[n].image =resources.left_button
					elif n == 4:
						menu[n].image = resources.right_button
			else:
				if n == 1:
					menu[n].image = resources.apply_button
				elif n == 2:
					menu[n].image = resources.back_button
				elif n == 3:
					menu[n].image =resources.left_button
				elif n == 4:
					menu[n].image = resources.right_button