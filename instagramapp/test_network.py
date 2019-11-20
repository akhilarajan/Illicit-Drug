# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2
# load the image
##image = cv2.imread("281.jpg")
##image = cv2.imread("bb.jpg")
image = cv2.imread("d5.jpg")
##image = cv2.imread("n7.jpg")
orig = image.copy()

# pre-process the image for classification
image = cv2.resize(image, (100, 100))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)
# load the trained convolutional neural network
print("[INFO] loading network...")
model = load_model("model")

#classify the input image
##print("image[0]",image[0])
(notdrug, drug) = model.predict(image)[0]
# build the label
print ("drug",drug)
print ("notdrug",notdrug)

label = "Drug" if drug > notdrug else "Not Drug"
proba = drug if drug > notdrug else notdrug
print ("label-----------",label)
label = "{}: {:.2f}%".format(label, proba * 100)

# draw the label on the image
output = imutils.resize(orig, width=400)
cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,	0.7, (0, 255, 0), 2)

# show the output image
cv2.imshow("Output", output)
cv2.waitKey(0)
