import random, math, load, resources
from pyglet.sprite import Sprite
from pyglet.window import key

thrust = 50.0
key_handler = key.KeyStateHandler()
counter = 0
call = False
creeps_1 = []
score = 0

def handle_calls(width, height, grid, player, creeps, dt):
	if call:
		player_behavior(width, height, grid, player, creeps, 0)
	elif not call:
		if player_behavior(width, height, grid, player, creeps, dt) == 1:
			return 1
	if key_handler[key.ENTER]:		
		return 0

def creep_behavior(j, grid, dt):
	global counter
	if call:
		j.velocity_x = 0
		j.velocity_y = 0
		j.x += j.velocity_x 
		j.y += j.velocity_y 
	elif not call:
		if counter == 0:
			if 0 == random.randint(0, 100):
				j.velocity_x = random.randint(-50, 50) * dt	
				j.velocity_y = random.randint(-50, 50) * dt
				if 0 == random.randint(0, 1):
					j.velocity_x = 0
					j.velocity_y = 0
			j.x += j.velocity_x
			j.y += j.velocity_y
		elif coutner == random.randint(500, 1000):
			counter = 0
		else:
			counter += 1
	check_bounds(j, grid)

def player_behavior(width, height, grid, player, creeps, dt):
	global creeps_1, score
	creeps_1 = creeps
	for j in creeps_1:
		creep_behavior(j, grid, dt)
	force_x = thrust * dt
	force_y = thrust * dt
	if key_handler[key.LEFT]:
		player.velocity_x -= -force_x
	if key_handler[key.RIGHT]:
		player.velocity_x -= force_x
	if key_handler[key.UP]:
		player.velocity_y -= force_y
	if key_handler[key.DOWN]:
		player.velocity_y -= -force_y
	if player.velocity_x < -300:
		player.velocity_x = -300
	if player.velocity_y < -300:
		player.velocity_y = -300
	if player.velocity_x > 0:
		grid.x += 0
	else:
		grid.x += player.velocity_x * dt
	player.x -= player.velocity_x*1/4 * dt
	player.y -= player.velocity_y * dt
	if player.x > width*3/5:
		player.x = width*3/5
	elif player.x < 20:
		player.x = 21
		player.velocity_x = 0
	if grid.x < -grid.width/2:
		grid.x += grid.width/2
	elif grid.x > 500:
		grid.x -= 500
	for j in range(len(creeps)):
		if player.velocity_x > 0:
			creeps[j].x += 0
		else:
			creeps[j].x += player.velocity_x * dt
		if creeps[j].x < 0:
			creeps[j].x = random.randint(2000, 4000)
			creeps[j].y = random.randint(grid.y - grid.y/2 + 50, grid.y/2 + grid.height -50)
			creeps[j].velocity_x = 0
			creeps[j].velocity_y = 0
			score += 1
		if math.fabs(math.fabs(player.x) - math.fabs(creeps[j].x)) < player.width:
			if math.fabs(math.fabs(player.y) - math.fabs(creeps[j].y)) < player.height:
				return 1	
	check_bounds(player, grid)

def check_bounds(j, grid):
		min_x = 0
		min_y = grid.y - grid.height/2 - 50
		max_y = grid.y + grid.height/4
		if j.x < min_x:
			j.velocity_x = - j.velocity_x
		if j.y < min_y or j.y > max_y:
			if j.y < min_y:
				j.y = min_y + 1
			elif j.y > max_y:
				j.y = max_y - 1
			j.velocity_y = - j.velocity_y