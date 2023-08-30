from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2 as cv
from pygame import mixer
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import datetime

cred = credentials.Certificate("dlc-code-9bc2f-firebase-adminsdk-azjf3-ea4cce41e8.json")
firebase_admin.initialize_app(cred, {'databaseURL': "https://dlc-code-9bc2f-default-rtdb.asia-southeast1.firebasedatabase.app/"})


mixer.init()
sound = mixer.Sound('sound.wav')


def eye_aspect_ratio(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	_eye_aspect_ratio = (A + B) / (2.0 * C)
	return _eye_aspect_ratio
	
thresh = 0.23
iteration_no = 30
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
cap=cv.VideoCapture(0)
# f = open("data_storage.txt", "w")
flag=0
indiicator=30
while True:
	ret, frame=cap.read()
	frame = imutils.resize(frame, width=900)
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	subjects = detect(gray, 0)
	for subject in subjects:
		shape = predict(gray, subject)
		shape = face_utils.shape_to_np(shape)


		leftEye = shape[lStart:lEnd]
		rightEye = shape[rStart:rEnd]
		le_eye_aspect_ratio = eye_aspect_ratio(leftEye)
		ri_eye_aspect_ratio = eye_aspect_ratio(rightEye)
		_eye_aspect_ratio = (le_eye_aspect_ratio + ri_eye_aspect_ratio) / 2.0
		le_hull = cv.convexHull(leftEye)
		re_hull = cv.convexHull(rightEye)

		# cv.rectangle(frame, [le_hull] ,-1, (0, 255, 0), 1)
		# cv.rectangle(frame, [re_hull] ,-1, (0, 255, 0), 1)


		cv.drawContours(frame, [le_hull], -1, (0, 255, 0), 1)
		cv.drawContours(frame, [re_hull], -1, (0, 255, 0), 1)
		print(_eye_aspect_ratio)

		if _eye_aspect_ratio > thresh:
			flag += 1
			# print (flag)
			if flag >= iteration_no:
				cv.putText(frame, 
				"***********************!!ALERT!!***********************",
				(10, 30),
					cv.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)


					# cv.putText(frame, "ALERT!!", (10, 30),
					# cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)


				cv.putText(frame, 
				"***********************!!ALERT!!***********************",
				 (10,615),
					cv.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
				
				sound.play()
				person = 0
			if indiicator == 30:
				x = datetime.datetime.now()
				z = x.strftime("%m/%d/%Y, %H:%M:%S")

				# f = open("data_storage.txt", "a")
				# f.write("Alert!! person is consicious",x "\n")
				# f.close()
				# f = open("data_storage.txt", "r")
				# print(f.read())

				ref = db.reference("py/")
				# ref.push().set({
				ref.set({
						'bed_no_1': {
							"patient":"awake",
							"time" : str(z)
						}
				})
				indiicator=0

		else:
			flag = 0
	cv.imshow("Frame", frame)
	key = cv.waitKey(1) 
	if key == ord(" "):
		break  
	# else:
	# 	continue
cv.destroyAllWindows()
cap.release() 