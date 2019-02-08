import pyglet, resources, math
from pyglet.window import key

thrust = 300.0
rotate_speed = 200.0
key_handler = key.KeyStateHandler()

def loadplayer(height, batch=None):
	player = pyglet.sprite.Sprite(img=resources.player_image, x=0, y=height/2, batch=batch)
	player.velocity_x = 0
	player.velocity_y = 0
	player.rotation = 0
	return player

def update(dt):
	if key_handler[key.LEFT]:
		player.rotation -= rotate_speed * dt
	if key_handler[key.RIGHT]:
		player.rotation += rotate_speed * dt
	if key_handler[key.UP]:
		angle_radians = -math.radians(rotation)
		force_x = math.cos(angle_radians) * thrust * dt
		force_y = math.sin(angle_radians) * thrust * dt
		player.velocity_x += force_x
		if player.velocity_x > 100:
			player.velocity_x = 100
		player.velocity_y += force_y
		if player.velocity_y > 100:
			player.velocity_y = 100