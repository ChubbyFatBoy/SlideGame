import pyglet

def center_image(image):
	image.anchor_x = image.width/2
	image.anchor_y = image.height/2

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

# start screen
	# button images
start_button = pyglet.resource.image("start.png")
start_motion = pyglet.resource.image("start_motion.png")
options_button = pyglet.resource.image("options.png")
options_motion = pyglet.resource.image("options_motion.png")
exit_button = pyglet.resource.image("exit.png")
exit_motion = pyglet.resource.image("exit_motion.png")
	# center images
center_image(start_button)
center_image(options_button)
center_image(exit_button)
center_image(start_motion)
center_image(options_motion)
center_image(exit_motion)

# options screen
	# button images
apply_button = pyglet.resource.image("apply_button.png")
apply_motion = pyglet.resource.image("apply_hover.png")
back_button = pyglet.resource.image("back_button.png")
back_motion = pyglet.resource.image("back_hover.png")
right_button = pyglet.resource.image("right_button.png")
right_motion = pyglet.resource.image("right_hover.png")
right_press = pyglet.resource.image("right_press.png")
left_button = pyglet.resource.image("left_button.png")
left_motion = pyglet.resource.image("left_hover.png")
left_press = pyglet.resource.image("left_press.png")
	# center images
center_image(apply_button)
center_image(apply_motion)
center_image(left_button)
center_image(left_motion)
center_image(left_press)
center_image(right_button)
center_image(right_motion)
center_image(right_press)
center_image(back_button)
center_image(back_motion)

# global
	# button images
press_button = pyglet.resource.image("press_button.png")
option_press = pyglet.resource.image("apply_press.png")
	# center images
center_image(press_button)
center_image(option_press)

# game screen
	# images
health_bar = pyglet.resource.image("health_bar.png")
creep_image = pyglet.resource.image("creep.png")
player_image = pyglet.resource.image("player.png")
game_over = pyglet.resource.image("game_over.png")
grid = pyglet.resource.image("grid.png")
player = pyglet.resource.image("player.png")
	# center images
center_image(creep_image)
center_image(player_image)
center_image(game_over)

# game/pause
	# button images
pause_menu = pyglet.resource.image("pause_menu.png")
resume_button = pyglet.resource.image("resume_button.png")
resume_motion = pyglet.resource.image("resume_motion.png")
menu_button = pyglet.resource.image("menu_button.png")
menu_motion = pyglet.resource.image("menu_motion.png")
restart_button = pyglet.resource.image("restart_button.png")
restart_motion = pyglet.resource.image("restart_motion.png")
	# center images
center_image(pause_menu)
center_image(resume_button)
center_image(resume_motion)
center_image(menu_button)
center_image(menu_motion)
center_image(restart_button)
center_image(restart_motion)









grid.anchor_y = grid.height*2/3