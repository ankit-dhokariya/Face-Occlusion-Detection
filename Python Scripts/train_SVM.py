# USAGE
# python train_SVM.py --training training

# import packages
from pyimagesearch.localbinarypatterns import LocalBinaryPatterns
from sklearn.svm import LinearSVC
import pickle
from imutils import paths
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--training", required=True,
	help="path to the training images")
args = vars(ap.parse_args())

# initialize the local binary patterns descriptor along with
# the data and label lists
desc = LocalBinaryPatterns(24, 8)
data = []
labels = []

print("[INFO] Labeling Images...")
# loop over the training images
for imagePath in paths.list_images(args["training"]):
	# load the image, convert it to grayscale, and describe it
	image = cv2.imread(imagePath,0)
	#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	hist = desc.describe(image)
	# extract the label from the image path, then update the
	# label and data lists
	# label = imagePath.split("\\")[1]
	labels.append(imagePath.split("\\")[1])
	data.append(hist)

print("[INFO] Images Labeled...")
#data = data.reshape(-1,1)
#labels = labels.reshape(-1,1)
# train a Linear SVM on the data
model = LinearSVC(C=100.0, random_state=42, max_iter=5000)
print("[INFO] SVM loaded...")
print("[INFO] Model fitting...")
model.fit(data, labels)
print("[INFO] Model fitted...")
print("[INFO] Saving Model...")
pickle.dump(model, open("detection_model_hybriddata_24_8", 'wb'))
print("[INFO] Model saved...")

# print("[INFO] Loading Model...")
# model = loaded_model = pickle.load(open("detection_model", 'rb'))
# print("[INFO] Model Loaded...")

# loop over the testing images
# for imagePath in paths.list_images(args["testing"]):
	# load the image, convert it to grayscale, describe it,
	# and classify it
# 	image = cv2.imread(imagePath)
# 	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 	hist = desc.describe(gray)
# 	hist.reshape(1, -1)
# 	prediction = model.predict([hist])[0]
# 	print(prediction)

	# display the image and the prediction
# 	cv2.putText(image, prediction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
# 		1.0, (0, 0, 255), 3)
# 	cv2.imshow("Image", image)
# 	cv2.waitKey(0)