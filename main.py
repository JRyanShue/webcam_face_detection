import cv2

################
faceDetectionCascade = cv2.CascadeClassifier("C:/Users/jryan/PycharmProjects/license_plate_scanner/venv/Lib/site-packages/cv2"
                                    "/data/haarcascade_frontalface_default.xml")
minArea = 200
color = (255, 0, 255)
count = 0
################

# video capture from default (0) webcam
cap = cv2.VideoCapture(0)
# define width (id 3) as 640
cap.set(3, 640)
# define height (id 4) as 640
cap.set(4, 480)
# define brightness (id 10)
cap.set(10, 100)

# go through frames one by one
while True:
    # save img in variable, see if successfully done
    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # finds faces on gray image
    faces = faceDetectionCascade.detectMultiScale(imgGray, 1.1, 10)  # image, scale factor, min neighbors

    # get and draw bounding boxes
    for (x, y, w, h) in faces:
        # filter
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, "Face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            # region of interest
            imgRoi = img[y:y + h, x:x + w]
            cv2.imshow("Face", imgRoi)

    cv2.imshow("Live stream", img)

    # if q pressed, breaks and closes video

    # save ROI image
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Resources/Scans/Face_"+str(count)+".jpg", imgRoi)
        # saved feedback
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1
