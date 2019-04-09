from PIL import Image
import cv2

vidcap = cv2.VideoCapture('voetbaltest.mp4')
success = True;
count = 0

imagesarray = list()

while success and count < 1200:
	
	success,cv2_im = vidcap.read()
	#print('Read a new frame: ', success)

	

	if (count > 300 and count < 400): 
		
		cv2.imwrite("./frames/frame%d.jpg" % count, cv2_im)     # save frame as JPEG file      
		cv2_impil = cv2.cvtColor(cv2_im,cv2.COLOR_BGR2RGB)
		pil_im = Image.fromarray(cv2_impil)
		imagesarray.append(pil_im)
	#if (count > 400):
		
	
	count += 1;
	#pil_im.show()
	
	

imagesarray[0].show()