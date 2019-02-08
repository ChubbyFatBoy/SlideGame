import pyglet, resolution, button, resources
from pyglet.window import key
from pyglet.window import mouse
from button import Button
import io

width = int(resolution.loadres()['width'])
height = int(resolution.loadres()['height'])
window = pyglet.window.Window(width=width, height=height, resizable= True)

x=200
y=200
main_batch = pyglet.graphics.Batch()
testbutton = button.Button(x, y, main_batch)

game_objects = [testbutton]

window.push_handlers(testbutton.key_handler)

@window.event
def on_draw():
	window.clear()
	main_batch.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    global width
    if x < testbutton.x + 80 and x > testbutton.x:
    	if y < testbutton.y + 20 and y > testbutton.y:
            if width == 1024:
                window = pyglet.window.Window(width=800, height=600)
                resolution.changeres2()
                width = 800
            elif width == 800:
                window = pyglet.window.Window(width=1024, height=768)
                resolution.changeres1()
                width = 1024


def update(dt):
    for obj in game_objects:
        obj.update(dt) 

if __name__ == "__main__":
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1/120.0)
    
    # Tell pyglet to do its thing
    pyglet.app.run()
