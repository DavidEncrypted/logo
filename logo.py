from PIL import Image
import cv2

vidcap = cv2.VideoCapture('testvideo.mkv')
success,image = vidcap.read()
count = 0

imagesarray = list()

while success and count < 400:
  
	cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
	success,cv2_im = vidcap.read()
	#print('Read a new frame: ', success)

	cv2_im = cv2.cvtColor(cv2_im,cv2.COLOR_BGR2RGB)
	pil_im = Image.fromarray(cv2_im)
	#pil_im.show()
	imagesarray.append(imagesarray)
	count += 1
	if (count % 100 == 0): 
		print(count)
		pil_im.show()

imagesarray[10].show()