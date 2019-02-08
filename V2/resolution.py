
options = {}

def loadres():
	global options
	with open("../config/config.txt") as f:
		for line in f:
			(key, val) = line.split()
			options[str(key)] = val
	return options

def changeres1():
	global options
	options = open("../config/config.txt", "w")
	options.write("width 1024 \n height 768")

def changeres2():
	global options
	options = open("../config/config.txt", "w")
	options.write("width 800 \n height 600")