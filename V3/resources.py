import pyglet

def center_image(image):
	image.anchor_x = image.width/2
	image.anchor_y = image.height/2

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

start_button = pyglet.resource.image("start.png")
start_motion = pyglet.resource.image("start_motion.png")
press_button = pyglet.resource.image("press_button.png")
options_button = pyglet.resource.image("options.png")
options_motion = pyglet.resource.image("options_motion.png")
exit_button = pyglet.resource.image("exit.png")
exit_motion = pyglet.resource.image("exit_motion.png")
grid = pyglet.resource.image("grid.png")
player = pyglet.resource.image("player.png")
apply_button = pyglet.resource.image("apply_button.png")
option_press = pyglet.resource.image("apply_press.png")
apply_hover = pyglet.resource.image("apply_hover.png")
back_button = pyglet.resource.image("back_button.png")
back_hover = pyglet.resource.image("back_hover.png")
right_button = pyglet.resource.image("right_button.png")
right_hover = pyglet.resource.image("right_hover.png")
right_press = pyglet.resource.image("right_press.png")
left_button = pyglet.resource.image("left_button.png")
left_hover = pyglet.resource.image("left_hover.png")
left_press = pyglet.resource.image("left_press.png")

creep_image = pyglet.resource.image("creep.png")
player_image = pyglet.resource.image("player.png")

center_image(creep_image)
center_image(apply_button)
center_image(apply_hover)
center_image(option_press)
center_image(back_button)
center_image(back_hover)
center_image(right_button)
center_image(right_hover)
center_image(right_press)
center_image(left_button)
center_image(left_hover)
center_image(left_press)
center_image(player_image)