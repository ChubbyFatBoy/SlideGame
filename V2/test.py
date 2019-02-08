import pyglet

def window():
	window = pyglet.window.Window(300, 200)
	return window

window = window()

@window.event
def on_draw():
	window.clear()

pyglet.app.run()