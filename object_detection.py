import io
import os
from google.cloud import vision    # Google Cloud client library


def find_objects():
	vision_client = vision.Client()       # create a client
	file_name = 'test2.jpg'               # image file to be read
	
	file_to_check = io.open(file_name, 'rb')     # open the file
	matter_in_image = file_to_check.read()       # extract matter inside it
	image = vision_client.image(content=matter_in_image)  

	objects = image.detect_labels()              # finding the objects

	print('Objects detected are like this :')

	for ob in objects:                            # printing of objects
		print(ob.description)


if __name__ == '__main__':
	find_objects()                # calling the main function for finding labels
