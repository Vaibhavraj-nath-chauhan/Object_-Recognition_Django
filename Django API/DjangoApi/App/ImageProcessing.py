import cv2
image = cv2.imread("image5.jpg")
text = "This is Vaibhav"
x = 150
y = 100
text_image = cv2.putText(image,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,255))
text_image_rect = cv2.rectangle(text_image,(200,70),(400,300),(0,255,0),2)


while True:
    cv2.imshow("this is my image",image)   #title and img data
    if cv2.waitKey(1)==ord("q"): # help to set image delay 
        break 


 