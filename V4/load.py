from pyglet.sprite import Sprite
from create_window import scale_game, scale_menu
import resources, random, pyglet

score = None
player_health = []

def load(width, height, batch=None, front=None, back=None):
	global score, player_health
	player = Sprite(img=resources.player_image, x=width*1/3, y=height/2, batch=batch, group=front)
	player.velocity_y = 0
	player.velocity_x = 0
	player.rotation = 0
	creeps = loadcreeps(10, batch, front)
	grid = Sprite(img=resources.grid, x=-1000, y=width/2, batch=batch, group=back)
	grid.velocity_x = 0
	grid.velocity_y = 0
	score = pyglet.text.Label(text='0', font_name='Comic Sans', 
		 font_size=50, x=20, y=20, batch=batch, group=front)
	if player_health == []:
		player_health = load_health(width, height, batch, front, back)
	return player, creeps, grid

def loadcreeps(num, batch=None, group=None):
	global creeps
	creeps = []
	for n in range(num):
		while True:
			x = random.randint(1000, 3000)
			y = random.randint(400, 500)
			creep = Sprite(img=resources.creep_image, x=x, y=y, batch=batch, group=group)
			creep.velocity_x = random.randint(-5, 5)
			creep.velocity_y = random.randint(-5, 5)
			creeps.append(creep)
			break
	return creeps

def load_health(width, height, batch=None, front=None, back=None):
	global player_health
	poop = 0
	health =Sprite(img=resources.health_bar, x=width, y=height)
	player_health.append(health)
	for j in range(3):
		poop += width/10
		health = Sprite(img=resources.health_bar, x=width*30/50 + poop, y=height*45/50, batch=batch, group=front)
		player_health.append(health)
	scale_menu(player_health, width)
	return player_health