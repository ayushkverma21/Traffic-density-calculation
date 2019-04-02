import cv2
s = input("give figure")

def click(n=0):
	camera = cv2.VideoCapture(0)
	return_value,image = camera.read()
	image = cv2.resize(image,(480,320), interpolation = cv2.INTER_CUBIC)
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	
	edges = cv2.Canny(image,100,200)
	
	cv2.imwrite('test.jpg',image)
	
	camera.release()	
	return(edges);


def car_count():
	ing = cv2.imread(s+".jpg")
	g = cv2.resize(ing,(640,480), interpolation = cv2.INTER_CUBIC)
	blurred = cv2.pyrMeanShiftFiltering(g,50,60)
	gra = cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
	edge = cv2.Canny(gra,100,200)
	cv2.imshow('hj',edge)
	cv2.waitKey(3000)
	ret , thresh = cv2.threshold(edge,127,255,cv2.THRESH_BINARY)
	contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	print(len(contours))
	cv2.drawContours(ing,contours,-1,(0,0,255),5)
	cv2.namedWindow('display',cv2.WINDOW_NORMAL)
	cv2.imshow('display',ing)
	cv2.waitKey()
	#cv2.imshow("a",edge)
	#cv2.waitKey(3000)
	#cv2.windowDestroy("a")
	edge = list(edge)
	file = open("m.txt","w")
	n=0
	k=0
	for i in edge:
		edge[n] = list(i)
		file.write(str(edge[n])+"\n")
		
		for t in edge[n]:
			if t == 255:
				k+=1
		n+=1
	return(k)
	file.close()
	
car_count()


	

