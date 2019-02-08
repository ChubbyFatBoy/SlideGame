import configparser
from pyglet.window import Window


def create_window(width, height):
	# Creates window based on width and height given
	window = Window(width=width, height=height, resizable=True)
	return window

def apply_resolution(text):
	# When apply button is pressed in options menu applies changes to configuration.ini
	# according to the text showing resolution
	config = configparser.ConfigParser()
	if text == '800x600':
		config['window']= {'option': '0', 'width': '800', 'height': '600'}
	elif text == '1024x768':
		config['window']= {'option': '1', 'width': '1024', 'height': '768'}
	elif text == '1280x1024':
		config['window']= {'option': '0', 'width': '1280', 'height': '1024'}
	with open('configuration.ini', 'w') as configfile:
		config.write(configfile)

def window_load():
	# Reads width and height from configuration.ini and returns
	# them for use in width and height
	config = configparser.ConfigParser()
	config.read('configuration.ini')
	width = int(config['window']['width'])
	height = int(config['window']['height'])
	return width, height

def scale_menu(menu, width):
	# Depending on the resolution it scales menu objects to fit on screen
	for j in menu:
		if width == 800:
			j.scale = 0.4
		elif width == 1024:
			j.scale = 0.5
		else:
			j.scale = 0.6

def scale_game(menu, width):
	# Depending on the resolution it scales game objects to fit on screen
	for j in menu:
		if width == 800:
			j.scale = 0.8
		elif width == 1024:
			j.scale = 0.9
		else:
			j.scale = 1