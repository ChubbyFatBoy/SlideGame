import pyglet, resources
from time import sleep

def create(width, height, batch=None):
	global menu
	start = buttoncreate( width/2-97, height*3/4, resources.start_button, batch=batch)
	options = buttoncreate(width/2-97, height*2/4, resources.options_button, batch=batch)
	exit = buttoncreate(width/2-97, height*1/4, resources.exit_button, batch=batch)
	menu = [start, options, exit]
	if width == 1024:
		for j in range(3):
			menu[j].scale = 0.5
	elif width == 800:
		for j in range(3):
			menu[j].scale = 0.4
	return menu

def buttoncreate(x, y, image, batch=None):
	koumpi = pyglet.sprite.Sprite(img=image, x=x , y=y, batch=batch)
	koumpi.scale =0.5
	return koumpi
	
def press(x, y, button):
	global menu
	for n in range(3):
		if button == pyglet.window.mouse.LEFT:
			if x > menu[n].x and x < menu[n].x + menu[n].width:
				if y > menu[n].y and y < menu[n].y + menu[n].height:
					menu[n].image = resources.press_button

def release(x, y, button):
	global menu
	for n in range(3):
		if button == pyglet.window.mouse.LEFT:
			if x > menu[n].x and x < menu[n].x + menu[n].width:
				if y > menu[n].y and y < menu[n].y + menu[n].height:
					if n == 0:
						menu[n].image = resources.start_motion
						return 0
					elif n == 1:
						menu[n].image = resources.options_motion
						return 1
					elif n == 2:
						menu[n].image = resources.exit_motion
						pyglet.app.exit()

def motion(x, y):
	global menu
	for n in range(3):
		if x > menu[n].x and x < menu[n].x + menu[n].width:
			if y > menu[n].y and y < menu[n].y + menu[n].height:
				if n == 0:
					menu[n].image = resources.start_motion
				elif n == 1:
					menu[n].image = resources.options_motion
				elif n == 2:
					menu[n].image = resources.exit_motion
			else:
				if n == 0:
					menu[n].image = resources.start_button
				elif n == 1:
					menu[n].image = resources.options_button
				elif n == 2:
					menu[n].image = resources.exit_button
		else:
			if n == 0:
				menu[n].image = resources.start_button
			elif n == 1:
				menu[n].image = resources.options_button
			elif n == 2:
				menu[n].image = resources.exit_button