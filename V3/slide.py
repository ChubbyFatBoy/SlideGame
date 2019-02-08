import pyglet, koumpi, resources, options, creep, handleplayer, handlegrid
from time import sleep

#window creation
width = int(options.loadres()['width'])
height = int(options.loadres()['height'])
window = pyglet.window.Window(width=width, height=height)

#variable
main_batch = pyglet.graphics.Batch()
batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)
koumpia= koumpi.create(window.width, window.height, main_batch)
menuflag = 0
creeps = []

#Window events
@window.event
def on_mouse_press(x, y, button, modifiers):
	global koumpia, menuflag, grid
	#checks in which template is in
	if menuflag == 0:
		#loads up main menu template and checks which button was pressed if any
		koumpia = koumpi.press(x, y, button)
	elif menuflag ==1:
		#loads up options menu template and checks which button was pressed if any
		koumpia == options.press(x, y, button)

		
@window.event
def on_mouse_release(x, y, button, modifiers):
	global koumpia, menuflag, width, window, creeps, grid, player
	#checks in which template is in
	if menuflag ==0:
		#loads up main menu template and checks which button was released, selected if any
		koumpia = koumpi.release(x, y, button)
		#checks if play button was released, selected
		if koumpi.release(x, y, button) == 0:
			for j in range(3):
				koumpi.menu[j].delete()
			menuflag = 2
			grid = handlegrid.loadgrid(width, height, main_batch, background)
			player = handleplayer.loadplayer(height, main_batch, foreground)
			creeps = creep.loadcreeps(10, width, height, main_batch, foreground)
		#checks if options button was released, selected
		elif koumpi.release(x, y, button) == 1:
			#clears main menu template and loads up options template
			for j in range(3):
				koumpi.menu[j].delete()
			menuflag = 1
			koumpia = options.create(window.width, window.height, main_batch)
	elif menuflag ==1:
		#loads up options menu template and checks which button was released, selected if any
		koumpia == options.release(x, y, button)
		if options.release(x, y, button) == 0:
			#if apply button was pressed changes resolution and size of sprites
			if x < options.menu[1].x + options.menu[1].width and x > options.menu[1].x - options.menu[1].width:
				if y < options.menu[1].y + options.menu[1].height and y > options.menu[1].y - options.menu[1].height:
					if width == 800 and options.opt == 1:
						window.set_size(1024, 768)
						options.changeres1()
						width = 1024
					elif width == 1024 and options.opt == 0:
						window.set_size(800, 600)
						options.changeres2()
						width = 800
		elif options.release(x, y, button) == 1:
			#if back button was pressed clears options menu and loads up main menu
			for j in range(5):
				options.menu[j].delete()
			koumpia = koumpi.create(window.width, window.height, main_batch)
			menuflag = 0


window.push_handlers(handlegrid.key_handler)

@window.event
def on_mouse_motion(x, y, dx, dy):
	global koumpia
	#checks if mouse hovers over any button on the sceen and changes the sprite respondingly
	if menuflag ==0:
		koumpia = koumpi.motion(x, y)
	elif menuflag ==1:
		koumpia == options.motion(x, y)


@window.event
def on_draw():
	#draws main batch
	window.clear()
	main_batch.draw()

def update(dt):
	for obj in creeps:
		creep.update(dt)
	handlegrid.update(dt)


if __name__ == "__main__":
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1/120.0)
    
    # Tell pyglet to do its thing
    pyglet.app.run()
