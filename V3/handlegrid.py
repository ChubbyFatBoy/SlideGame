import pyglet, resources, handleplayer, math, creep
from pyglet.window import key
from creep import check_bounds

thrust = 300.0
rotate_speed = 200.0
key_handler = key.KeyStateHandler()

def loadgrid(width, height, batch=None, group=None):
	global grid, cbatch, cgroup 
	grid = []
	cbatch = batch
	cgroup = group
	cwidth = width
	cheight = height
	c = 0
	while True:
		hip = pyglet.sprite.Sprite(img=resources.grid, x=-2000+c, y=0, batch=batch, group=group)
		hip.velocity_x = 0
		grid.append(hip)
		c += 2000
		if c > 8000:
			break
	return grid

def update(dt):
	global grid, bt
	bt = dt
	if key_handler[key.LEFT]:
		handleplayer.player.rotation -= rotate_speed * dt
	if key_handler[key.RIGHT]:
		handleplayer.player.rotation += rotate_speed * dt
	if key_handler[key.UP]:
		angle_radians = -math.radians(handleplayer.player.rotation)
		force_x = -math.cos(angle_radians) * thrust * dt
		force_y = math.sin(angle_radians) * thrust * dt
		for j in range(5):
			grid[j].velocity_x += force_x
			if grid[j].velocity_x >= 0:
				grid[j].velocity_x = 0
			grid[j].x += grid[j].velocity_x * dt
			if j == 1 and grid[0].x < -2000:
				for i in range(2):
					grid[i].x += 2000
		handleplayer.player.velocity_y += force_y
		handleplayer.player.y += handleplayer.player.velocity_y * dt
		if handleplayer.player.velocity_y > 100 and handleplayer.player.velocity_y < -100:
			handleplayer.player.velocity_y = 50
		for j in range(10):
			creep.creeps[j].x += grid[0].velocity_x * dt
		check_bounds(handleplayer.player)
		