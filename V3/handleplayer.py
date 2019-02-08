import pyglet, resources, math
from pyglet.window import key
from creep import check_bounds

thrust = 300.0
rotate_speed = 200.0
key_handler = key.KeyStateHandler()

def loadplayer(height, batch=None, group=None):
	global player
	player = pyglet.sprite.Sprite(img=resources.player_image, x=300, y=height/2, batch=batch, group=group)
	player.velocity_y = 0
	player.rotation = 0
	return player