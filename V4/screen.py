import pyglet, resources, create_window
from pyglet.sprite import Sprite
from pyglet.text import Label
from create_window import scale_menu

whereami = 0
option = 0
label = None

def active_screen(width, height, batch=None, back=None, front=None):
	# Handles which screen is to be loaded depending on the value of whereami
	if whereami == 0:
		active_screen = main_menu(width, height, batch, back, front)
	elif whereami == 1:
		active_screen = options_menu(width, height, batch, back, front)
	elif whereami == 2:
		active_screen= pause_menu(width, height, batch, back, front)
	return active_screen

def main_menu(width, height, batch=None, back=None, front=None):
	# Loads button sprites used in main menu
	start_button = Sprite(img=resources.start_button, x=width/2, y=height*3/4, batch=batch, group=front)
	option_button = Sprite(img=resources.options_button, x=width/2, y=height*2/4, batch=batch, group=front)
	exit_button = Sprite(img=resources.exit_button, x=width/2, y=height*1/4, batch=batch, group=front)
	menu = [start_button, option_button, exit_button]
	scale_menu(menu, width)
	return menu

def options_menu(width, height, batch=None, back=None, front=None):
	# Loads buttons sprites and the label showing resolution in options menu
	global label
	apply_button = Sprite(img=resources.apply_button, x=width*2/5, y=height*1/10, batch=batch, group=front)
	back_button = Sprite(img=resources.back_button, x=width*3/5, y=height*1/10, batch=batch, group=front)
	left_res = Sprite(img=resources.left_button, x=width*1/5, y=height/2, batch=batch, group=front)
	right_res = Sprite(img=resources.right_button, x=width*4/5, y=height/2, batch=batch, group=front)
	label = Label(font_name='Comic Sans', 
		 font_size=18, x=width/2, y=height/2, anchor_x='center', anchor_y='center', batch=batch)
	# Loads the text of the label
	reslabel(0)
	menu = [apply_button, back_button, left_res, right_res]
	scale_menu(menu, width)
	return menu

def pause_menu(width, height, batch=None, back=None, front=None):
	#loads pause menu, background and button sprites
	background = Sprite(img=resources.pause_menu, x=width/2, y=height/2, batch=batch, group=back)
	resume_button = Sprite(img=resources.resume_button, x=width/2, y=height*6/10, batch=batch, group=front)
	restart_button = Sprite(img=resources.restart_button, x=width/2, y=height*5/10, batch=batch, group=front)
	menu_button = Sprite(img=resources.menu_button, x=width/2, y=height*4/10, batch=batch, group=front)
	menu = [resume_button, restart_button, menu_button, background]
	scale_menu(menu, width)
	return menu

def reslabel(num):
	# changes the resolution label text according to options given,
	# by left right arrow in options menu
	global option, label
	if num == 1 and option != 2:
		option += 1
	elif num == -1 and option != 0:
		option -=1
	else:
		if option == 2:
			option = 0
		else:
			option = 2
	if option == 0:
		label.text = "800x600"
	elif option == 1:
		label.text = "1024x768"
	elif option == 2:
		label.text = "1280x1024"