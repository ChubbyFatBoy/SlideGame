import pyglet, creep, random, resources

def loadcreeps(num, width, height, batch=None, group=None):
	global creeps
	creeps = []
	for n in range(num):
		while True:
			x = random.randint(0, width)
			y = random.randint(0, height)
			creep = pyglet.sprite.Sprite(img=resources.creep_image, x=x, y=y, batch=batch, group=group)
			creep.velocity_x = random.randint(-10, 10)
			creep.velocity_y = random.randint(-10, 10)
			creep.counter = 0
			creeps.append(creep)
			break
	return creeps

def check_bounds(obj):
		min_x = 0
		min_y = 0
		max_x = 1024
		max_y = 768
		if obj.x < min_x or obj.x > max_x:
			obj.velocity_x = - obj.velocity_x
		if obj.y < min_y or obj.y > max_y:
			obj.velocity_y = - obj.velocity_y

def behavior(obj):
	if obj.counter > 1000:
		if 0 == random.randint(0, 2000):
			obj.velocity_x = random.randint(-10, 10)		
			obj.velocity_y = random.randint(-10, 10)
			obj.counter = 0
			if 0 == random.randint(0, 5):
				obj.velocity_x = 0
				obj.velocity_y = 0		
	else:	
		obj.counter += 1


def update(dt):
	global creeps
	for j in range(10):
		creeps[j].x += creeps[j].velocity_x * dt
		creeps[j].y += creeps[j].velocity_y * dt
		check_bounds(creeps[j])
		behavior(creeps[j])
