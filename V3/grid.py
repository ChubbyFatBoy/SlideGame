import pyglet, resources, player
from pyglet.window import key

thrust = 300.0
rotate_speed = 200.0
key_handler = key.KeyStateHandler()

def loadgrid(width, height, batch=None, group=None):
	global grid
	grid = pyglet.sprite.Sprite(img=resources.grid, x=width/2, y=height/2, batch=batch, group=group)
	grid.velocity_x = 0
	return grid

def update(dt):
	if key_handler[key.LEFT]:
		handleplayer.player.rotation -= rotate_speed * dt
	if key_handler[key.RIGHT]:
		handleplayer.player.rotation += rotate_speed * dt
	if key_handler[key.UP]:
		angle_radians = -math.radians(player.rotation)
		force_x = math.cos(angle_radians) * thrust * dt
		force_y = math.sin(angle_radians) * thrust * dt
		handleplayer.player.velocity_x += force_x
		if grid.velocity_x > 100:
			grid.velocity_x = 100
		player.velocity_y += force_y
		if handleplayer.player.velocity_y > 100:
			handleplayer.player.velocity_y = 100
		handleplayer.player.y += player.velocity_y * dt