from google.colab.patches import cv2_imshow
import cv2
import numpy as np

# Load the image
image = cv2.imread('path/of/your/picture')

# Convert the image from BGR to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define range for red color in HSV
lower_red1 = np.array([0,120,70])
upper_red1 = np.array([10,255,255])
lower_red2 = np.array([170,120,70])
upper_red2 = np.array([180,255,255])

# Threshold the HSV image to get only red colors
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

# Bitwise-OR mask and original image
mask_combined = cv2.bitwise_or(mask1, mask2)
result_image = cv2.bitwise_and(image, image, mask=mask_combined)

cv2_imshow(result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()