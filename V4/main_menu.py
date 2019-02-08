import resources, screen
from pyglet.window import mouse
from pyglet.app import exit
from create_window import window_load

def on_press(x, y, button, modifiers, active_screen):
	if button == mouse.LEFT:
		if screen.whereami == 1:
			j = mousecheck(x, y, active_screen)
			if j == 0:
				active_screen[j].image = resources.option_press
			if j == 1:
				active_screen[j].image = resources.option_press
			if j == 2:
				active_screen[j].image = resources.left_press
			if j == 3:
				active_screen[j].image = resources.right_press
		if screen.whereami == 0:
			j = mousecheck(x, y, active_screen)
			if j == 0:
				change_image(active_screen[j], resources.press_button)
			elif j == 1:
				change_image(active_screen[j], resources.press_button)
			elif j == 2:
				change_image(active_screen[j], resources.press_button)
		if screen.whereami == 2:
			if range(len(active_screen)) == 4:
				active_screen.pop()
			j = mousecheck(x, y, active_screen)
			if j == 0:
				active_screen[j].image = resources.option_press
			elif j == 1:
				active_screen[j].image = resources.option_press
			elif j == 2:
				active_screen[j].image = resources.option_press


def on_release(x, y, button, modifiers, active_screen):
	if button == mouse.LEFT:
		if screen.whereami == 1:
			j = mousecheck(x, y, active_screen)
			if j == 0:
				active_screen[j].image = resources.apply_button
				return 3
			if j == 1:
				active_screen[j].image = resources.back_button
				return 0
			if j == 2:
				active_screen[j].image = resources.left_button
				return 4
			if j == 3:
				active_screen[j].image = resources.right_button
				return 5
		if screen.whereami == 0:
			j = mousecheck(x, y, active_screen)
			if j == 0:
				active_screen[j].image = resources.start_button
				return 2
			elif j == 1:
				active_screen[j].image = resources.options_button
				return 1
			elif j == 2:
				active_screen[j].image = resources.exit_button
				exit()
		if screen.whereami == 2:
			if range(len(active_screen)) == 4:
				active_screen.pop()
			j = mousecheck(x, y, active_screen)
			if j == 0:
				active_screen[j].image = resources.resume_button
				return 6
			elif j == 1:
				active_screen[j].image = resources.restart_button
				return 7
			elif j == 2:
				active_screen[j].image = resources.menu_button
				return 8

def on_motion(x, y, active_screen):
	if screen.whereami == 1:
		j = mousecheck(x, y, active_screen)
		if j == 0:
			change_image(active_screen[j], resources.apply_motion)
		elif j == 1:
			change_image(active_screen[j], resources.back_motion)
		elif j == 2:
			change_image(active_screen[j], resources.left_motion)
		elif j == 3:
			change_image(active_screen[j], resources.right_motion)
		else:
			change_image(active_screen[0], resources.apply_button)
			change_image(active_screen[1], resources.back_button)
			change_image(active_screen[2], resources.left_button)
			change_image(active_screen[3], resources.right_button)
	if screen.whereami == 0:
		j = mousecheck(x, y, active_screen)
		if j == 0:
			change_image(active_screen[j], resources.start_motion)
		elif j == 1:
			change_image(active_screen[j], resources.options_motion)
		elif j == 2:
			change_image(active_screen[j], resources. exit_motion)
		else:
			change_image(active_screen[0], resources.start_button)
			change_image(active_screen[1], resources.options_button)
			change_image(active_screen[2], resources.exit_button)
	if screen.whereami == 2:
		if range(len(active_screen)) == 4:
			active_screen.pop()
		j = mousecheck(x, y, active_screen)
		if j == 0:
			active_screen[j].image = resources.resume_motion
		elif j == 1:
			active_screen[j].image = resources.restart_motion
		elif j == 2:
			active_screen[j].image = resources.menu_motion
		else:
			change_image(active_screen[0], resources.resume_button)
			change_image(active_screen[1], resources.restart_button)
			change_image(active_screen[2], resources.menu_button)



def mousecheck(x, y, current_screen):
	for j in range(len(current_screen)):
		if x > current_screen[j].x - current_screen[j].width/2 and x < current_screen[j].x + current_screen[j].width/2:
			if y > current_screen[j].y - current_screen[j].height/2 and y < current_screen[j].y + current_screen[j].height/2:
				return j

def change_image(koumpi, image):
	koumpi.image = image