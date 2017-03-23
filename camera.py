import pygame.camera
import pygame.image
import time

pygame.camera.init()       
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()                            # start the camera
#img = cam.get_image()

i = 0
while(1):
	img = cam.get_image()           # to get image from started web camers
	#pygame.image.save(img, "photo"+str(i)+".bmp")
	time.sleep(3)                   # to make sleep thing for scheduled camera clicks
	print "hey "
	i = i + 1
	if(i==5):
		break
	

pygame.camera.quit()                   # off the camera

