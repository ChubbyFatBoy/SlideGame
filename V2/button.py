
from pyglet.sprite import Sprite
from pyglet.window import key
from pyglet.window import mouse
import resources

class Button():
	def __init__(self, button_x, button_y, batch=None):
		self.x = button_x
		self.y = button_y
		self.batch = batch
		self.button = Sprite( img=resources.button_image, x=self.x, y=self.y, batch=self.batch)
		self.key_handler = key.KeyStateHandler()
		self.event_handlers = [self, self.key_handler]

	def update(self, dt):
		if self.key_handler[key.LEFT]:
			print (True)
