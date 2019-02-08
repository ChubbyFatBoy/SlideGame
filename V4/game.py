import pyglet, resources, screen, load, interaction, math
from pyglet.window import key
from create_window import create_window, window_load, apply_resolution, scale_menu, scale_game
from screen import active_screen
from main_menu import on_release, on_press, on_motion
from time import sleep

main_batch = pyglet.graphics.Batch()

# 4 groups of layers for menu and game to distinct background from the rest of the sprites
background =pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)
front = pyglet.graphics.OrderedGroup(2)
further_front = pyglet.graphics.OrderedGroup(3)

# calls create_window.window_load to load configuration options for width and height and 
# then loads and uses them to load the rest of the sprites
width, height = window_load()
window = create_window(width, height)
active_screen = screen.active_screen(width, height, main_batch, background, foreground)

# scales sprites depending on the window size
game_over = None
scale_menu(active_screen, width)
game_objects = []
creeps = []
player_health = []
window.push_handlers(interaction.key_handler)
counter = 0
score_count = 0
game_timer = 0

# used to clear screen active screen
def clear_screen():
	# clears menu sprites or items set in screen.
	for j in range(len(active_screen)):
		active_screen.pop()
	if screen.label != None:
		screen.label.delete()
	if load.player_health != []:
		for j in range(len(load.player_health)):
			load.player_health.pop()
	if load.score != None:
		load.score.delete()
	if game_over != None:
		game_over.delete()

@window.event
def on_mouse_press(x, y, button, modifiers):
	# Checks which object on screen is pressed with the mouse and changes sprite to press if it's button
	on_press(x, y, button, modifiers, active_screen)

@window.event
def on_mouse_release(x, y, button, modifiers):
	# checks which button was pressed hence released, changes sprite if button and interacts with buttons
	global active_screen, width, height, window
	if on_release(x, y, button, modifiers, active_screen) == 0:
		# back button was pressed in option menu, clears screen and loads main menu
		screen.whereami = 0
		clear_screen()
		active_screen = screen.active_screen(width, height, main_batch, background, foreground)
	elif on_release(x, y, button, modifiers, active_screen) == 1:
		# options button was pressed in main menu, clears screen and loads options menu
		screen.whereami = 1
		clear_screen()
		active_screen = screen.active_screen(width, height, main_batch, background, foreground)
	elif on_release(x, y, button, modifiers, active_screen) == 2:
		# start button was pressed in main menu, clears screen and loads objects used in the game
		screen.whereami = 10
		clear_screen()
		reset()
	elif on_release(x, y, button, modifiers, active_screen) == 3:
		# apply button was pressed in options menu, applies changes according to the text_label shown
		apply_resolution(screen.label.text)
		width, height =window_load()
		window.set_size(width, height)
		clear_screen()
		active_screen = screen.active_screen(width, height, main_batch, background, foreground)
	elif on_release(x, y, button, modifiers, active_screen) == 4:
		# left arrow button pressed in options menu, changes text label for resolution accordingly
		screen.reslabel(-1)
	elif on_release(x, y, button, modifiers, active_screen) == 5:
		# right arrow button pressed in options menu, changes text label for resolution accordingly
		screen.reslabel(1)
	elif on_release(x, y, button, modifiers, active_screen) == 6:
		# resume button was pressed in pause menu, closes menu and resumes game
		interaction.call = False
		screen.whereami = 3
		clear_screen()
	elif on_release(x, y, button, modifiers, active_screen) == 7:
		# restart button was pressed in pause menu, closes menu and restarts game and resets lives to 3
		interaction.call = False
		screen.whereami = 3
		clear_screen()
		reset()
	elif on_release(x, y, button, modifiers, active_screen) == 8:
		# menu button was pressed in pause menu, clears objects on screen and loads main menu
		for j in range(len(game_objects)):
			game_objects.pop()
		for j in range(len(interaction.creeps_1)):
			interaction.creeps_1.pop()
		interaction.call = False
		screen.whereami = 0
		clear_screen()
		active_screen = screen.active_screen(width, height, main_batch, background, foreground)

@window.event
def on_mouse_motion(x, y, dx, dy):
	# changes button sprites to match mouse movements over buttons
	on_motion(x, y, active_screen)

def reset():
	# resets game, not lives
	global game_objects, creeps
	player, creeps, grid = load.load(width, height, main_batch, foreground, background)
	game_objects = [player] + [grid] + creeps
	scale_game(game_objects, width)


def update(dt):
	# updates frames accordingly
	global counter, game_over, game_objects, active_screen, score_count, game_timer
	for j in range(len(game_objects)):
		if j == 0:
			if interaction.handle_calls(width, height, game_objects[1], game_objects[0], creeps, dt) == 0:
				# ENTER Button was pressed pauses game
				interaction.call = True
				screen.whereami = 2
				active_screen = screen.active_screen(width, height, main_batch, front, further_front)
			elif interaction.handle_calls(width, height, game_objects[1], game_objects[0], creeps, dt) == 1:
				# colision between player and creep was detected, player loses life and resets to starting position
				if load.player_health != []:
					load.player_health.pop()
					load.score.delete()
					if len(load.player_health) == 0:
						interaction.score =0
					reset()
		load.score.text = "score: " + str(interaction.score)
	
			
						
@window.event
def on_draw():
	# draws stuff on window
	window.clear()
	main_batch.draw()

if __name__ == "__main__":
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1/60.0)
    
    # Tell pyglet to do its thing
    pyglet.app.run()