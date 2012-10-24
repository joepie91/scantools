import sane, os

scanner = None

def init(**kwargs):
	global scanner
	
	sane.init()
	
	devices = {}
	i = 0
	
	print "Available devices:"
	
	for device in sane.get_devices():
		devices[i] = device[0]
		print "%d. [%s] %s %s" % (i, device[3], device[1], device[2])
		i += 1
	
	choice = int(raw_input("[?] What device would you like to use?  "))
	
	try:
		scanner = sane.open(devices[choice])
	except KeyError, e:
		print "You did not input a valid device ID."
		exit(1)
	
	resolution = raw_input("[?] Scan resolution (DPI)? [default: 300]  ")
	if resolution == "":
		scanner.resolution = 300
	else:
		scanner.resolution = int(resolution)
		
	
	width = raw_input("[?] Width (mm)? [default: 214]  ")
	if width == "":
		scanner.br_x = 214
	else:
		scanner.br_x = int(width)
		
	height = raw_input("[?] Height (mm)? [default: 295]  ")
	if height == "":
		scanner.br_y = 295
	else:
		scanner.br_y = int(height)
		
	scanner.tl_x = 0
	scanner.tl_y = 0
	
def scan(projectname, num, **kwargs):
	pil_image = scanner.scan()
	pil_image.save("%s/%s.png" % (projectname, "{0:04d}".format(num)))
