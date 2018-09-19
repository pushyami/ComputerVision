import cv2
capture = cv2.VideoCapture(file_name)
success,frame = capture.read()
count = 0
while success:
	success,frame = capture.read()
	cv2.imwrite("./pics/sample_Frame%d.jpg" % count, frame)
	if cv2.waitKey(1) == 27:
		break
	count = count +1
