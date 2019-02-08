import pyglet

def center_image(image):
	image.anchor_x = image.width/2
	image.anchor_y = image.height/2

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

button_image = pyglet.resource.image("testbutton.png")
downbutton_image = pyglet.resource.image("testbutton2.png")