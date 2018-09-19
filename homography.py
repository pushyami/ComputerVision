import cv2
import numpy as np
import math

#Homography computation
def Homography(points_src,points_dest):
	A = np.asarray([[points_src[0][0],points_src[0][1],1,0,0,0,(-1*points_src[0][0]*points_dest[0][0]),(-1*points_src[0][1]*points_dest[0][0])],
				[0,0,0,points_src[0][0],points_src[0][1],1,(-1*points_src[0][0]*points_dest[0][1]),(-1*points_src[0][1]*points_dest[0][1])],
				[points_src[1][0],points_src[1][1],1,0,0,0,(-1*points_src[1][0]*points_dest[1][0]),(-1*points_src[1][1]*points_dest[1][0])],
				[0,0,0,points_src[1][0],points_src[1][1],1,(-1*points_src[1][0]*points_dest[1][1]),(-1*points_src[1][1]*points_dest[1][1])],
				[points_src[2][0],points_src[2][1],1,0,0,0,(-1*points_src[2][0]*points_dest[2][0]),(-1*points_src[2][1]*points_dest[2][0])],
				[0,0,0,points_src[2][0],points_src[2][1],1,(-1*points_src[2][0]*points_dest[2][1]),(-1*points_src[2][1]*points_dest[2][1])],
				 [points_src[3][0],points_src[3][1],1,0,0,0,(-1*points_src[3][0]*points_dest[3][0]),(-1*points_src[3][1]*points_dest[3][0])],
				 [0,0,0,points_src[3][0],points_src[3][1],1,(-1*points_src[3][0]*points_dest[3][1]),(-1*points_src[3][1]*points_dest[3][1])]])
	b = np.reshape(points_dest,(8,1))
	h=np.dot(np.linalg.pinv(A),b)
	h = np.append(h,1)
	h = np.reshape(h,(3,3))
	return h

#replacing image
def mapping(src_img,dest_img,points_src,Homography):
	tmp=np.zeros((src_img.shape[0],src_img.shape[1]))
	pts = np.array([[points_src[0][1],points_src[0][0]],[points_src[1][1],points_src[1][0]],[points_src[3][1],points_src[3][0]],[points_src[2][1],points_src[2][0]]])
	cv2.fillPoly(tmp,[pts],(255,255,255))
	for i in range(0,(src_img.shape[0]-1)):
		for j in range(0,(src_img.shape[1]-1)):
			if tmp[i,j]==255:
				point = np.array([i,j,1])
				new_coord = np.array(np.dot(Homography,point))
				new_coord = new_coord/new_coord[2]
				if (new_coord[0]>0) and (new_coord[0]< dest_img.shape[0])and (new_coord[1]>0) and (new_coord[1]<dest_img.shape[1]):
					src_img[i][j]=dest_img[int(math.floor(new_coord[0])),int(math.floor(new_coord[1]))]
				else:
					continue
	return src_img
#replacing image while making background dark
def mapping_no_bg(src_img,dest_img,points_src,Homography):
	tmp=np.zeros((src_img.shape[0],src_img.shape[1]))
	pts = np.array([[points_src[0][1],points_src[0][0]],[points_src[1][1],points_src[1][0]],[points_src[3][1],points_src[3][0]],[points_src[2][1],points_src[2][0]]])
	cv2.fillPoly(tmp,[pts],(255,255,255))
	for i in range(0,(src_img.shape[0]-1)):
		for j in range(0,(src_img.shape[1]-1)):
			if tmp[i,j]==255:
				point = np.array([i,j,1])
				new_coord = np.array(np.dot(Homography,point))
				new_coord = new_coord/new_coord[2]
				if (new_coord[0]>0) and (new_coord[0]< dest_img.shape[0])and (new_coord[1]>0) and (new_coord[1]<dest_img.shape[1]):
					src_img[i][j]=dest_img[int(math.floor(new_coord[0])),int(math.floor(new_coord[1]))]
				else:
					src_img[i][j]=0
	return src_img

#TASK1 IMAGES
#img1 = cv2.imread("./PicsHw2/1.jpg")
#img2 = cv2.imread("./PicsHw2/2.jpg")
#img3 = cv2.imread("./PicsHw2/3.jpg")
#img4 = cv2.imread("./PicsHw2/Jackie.jpg")

#TASK1 COORDINATES
#pts_a=np.array([[154,1518],[710,2943],[2250,1485],[2046,3003]])
#pts_b=np.array([[314,1315],[605,3014],[2013,1298],[1898,3031]])
#pts_c=np.array([[721,913],[374,2805],[2090,886],[2222,2849]])
#pts_d=np.array([[0,0],[0,1275],[719,0],[719,1275]])


#TASK 1(a) -  (1) - 1a-1d Homography
#H1=Homography(pts_a,pts_d)
#output1=mapping(img1,img4,pts_a,H1)
#cv2.imwrite("output21.jpg",output1)

#TASK 1(a) - (2) - 1b-1d Homography
#H2=Homography(pts_b,pts_d)
#output2=mapping(img2,img4,pts_b,H2)
#cv2.imwrite("output22.jpg",output2)

#TASK 1(a) - (3) - 1c-1d Homography
#H3=Homography(pts_c,pts_d)
#output3=mapping(img3,img4,pts_c,H3)
#cv2.imwrite("output23.jpg",output3)

#TASK 1(b) 1a-1c Homography
#pts =np.array([[0,0],[img3.shape[0],0],[0,img3.shape[1]],[img3.shape[0],img3.shape[1]]])
#H4 = Homography(pts_b,pts_a)
#H5 = Homography(pts_c,pts_b)
#H = np.dot(H5,H4)
#output4 = mapping_no_bg(img3,img1,pts,H)
#cv2.imwrite("output24.jpg",output4)

#TASK3 IMAGES
img1 = cv2.imread("2a.JPG")
img2 = cv2.imread("2b.JPG")
img3 = cv2.imread("2c.JPG")
img4 = cv2.imread("einstein.jpg")
img5 = cv2.imread("../IMG_3458.JPG")

#TASK3 COORDINATES
pts_a=np.array([[539,1502],[759,2470],[1535,1496],[1535,2459]])
pts_b=np.array([[853,963],[869,1892],[1491,963],[1491,1887]])
pts_b2=np.array([[1331,2585],[1331,3190],[1832,2585],[1832,3190]])
pts_c=np.array([[880,627],[820,1315],[1485,616],[1507,1309]])
pts_d=np.array([[0,0],[0,1260],[1599,0],[1599,1260]])
pts_e=np.array([[0,0],[0,3024],[3446,0],[3446,3024]])


#TASK 3 Experiment
H=Homography(pts_b,pts_d)
output=mapping(img2,img4,pts_b,H)
H=Homography(pts_b2,pts_e)
output=mapping(output,img5,pts_b2,H)

cv2.imwrite("output.jpg",output)

#TASK 2(a) - (3) 2c-2d Homography
#H3=Homography(pts_c,pts_d)
#output3=mapping(img3,img4,pts_c,H3)
#cv2.imwrite("output23.jpg",output3)

#TASK 2(B) - 1a-1c Homography
#pts =np.array([[0,0],[img3.shape[0],0],[0,img3.shape[1]],[img3.shape[0],img3.shape[1]]])
#H4 = Homography(pts_b,pts_a)
#H5 = Homography(pts_c,pts_b)
#H = np.dot(H5,H4)
#output4 = mapping_no_bg(img3,img1,pts,H)
#cv2.imwrite("output24.jpg",output4)


