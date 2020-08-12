## import library
import cv2
import math

## load image
image_path = "angle2.jpg"


## Read image
img = cv2.imread(image_path)
pointslist = []

## create function(mouse points) 
def mousePoint(event , x , y , flag , params):
    if event == cv2.EVENT_FLAG_LBUTTON:
        size = len(pointslist)
        if size != 0 and size % 3 != 0:
            cv2.line(img , tuple(pointslist[round((size - 1)/3)*3]), (x,y) , (255,0,0) , 2)
        cv2.circle(img , (x,y) , 5 , (255,0,0) , cv2.FILLED )
        pointslist.append([x,y])
        

def gradient(p1 ,p2):
    ## m1 and m2 are slope (i.e = y2-y1 / x2 - x1)
    return abs(p2[1] - p1[1] ) / (p2[0] - p1[0] )


def getAngle(pointslist):
    ## angle formula (tan@ = |(m1-m2) / (1 + m1*m2)|
    p1 , p2 , p3 = pointslist[-3:]
    m1 = gradient(p1,p2)
    m2 = gradient(p1,p3)
    angR = math.atan((m2-m1) /  (1 + (m2*m1)))
    angD = round(math.degrees(angR))
    
    # put text angle
    cv2.putText(img , str(angD) , (p1[0] - 50, p1[1] ) , cv2.FONT_HERSHEY_COMPLEX ,0.6, (0,0,255),2)
    
     
while True:

    ## create func angle
    if len(pointslist) % 3 == 0 and len(pointslist) != 0:
        getAngle(pointslist)

    cv2.imshow("Image" , img )
    cv2.setMouseCallback("Image" , mousePoint)
    if cv2.waitKey(1) & 0xFF == ord("q"):  #earse the points
        pointslist = []
        img = cv2.imread(image_path)

    if cv2.waitKey(1) & 0xFF == ord("e"):  #break the prog
        break




