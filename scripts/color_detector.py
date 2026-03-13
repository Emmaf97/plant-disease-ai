import cv2
import numpy as np

## Convert BGR → HSV color space for better color analysis:
image = cv2.imread('leaf1.jpg')  # reads in BGR format

image = cv2.resize(image, (224, 224))

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define HSV ranges
green_lower = np.array([35, 40, 40])
green_upper = np.array([85, 255, 255])

brown_lower = np.array([10, 50, 20])
brown_upper = np.array([30, 255, 200])

black_lower = np.array([0, 0, 0])
black_upper = np.array([180, 255, 50])

## Count pixels of each color
green_mask = cv2.inRange(hsv, green_lower, green_upper)
brown_mask = cv2.inRange(hsv, brown_lower, brown_upper)
black_mask = cv2.inRange(hsv, black_lower, black_upper)

green_count = np.sum(green_mask > 0)
brown_count = np.sum(brown_mask > 0)
black_count = np.sum(black_mask > 0)

## result is determined on count result.
if green_count > brown_count and green_count > black_count:
    result = "Healthy"
elif brown_count > green_count and brown_count > black_count:
    result = "disease or pest"
else: 
    result = "Disease/Dead"
print(result)