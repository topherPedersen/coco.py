import coco
set = coco.set
busywork = coco.busywork

set(15, 15, "white")

# Run Main Game Loop
run = True
while run == True:
	# busywork() function simply adds some work for the
	# computer to do in order to avoid the dreaded "pinwheel".
	# When ready, replace this function with your game logic.
	busywork() 
