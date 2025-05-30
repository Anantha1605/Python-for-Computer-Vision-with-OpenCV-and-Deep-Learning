import os
import cv2
import matplotlib.pyplot as plt

file_path = r"C:\Users\Manan\OneDrive\Desktop\Computer-Vision-with-Python\DATA\rainbow.jpg"

# Check if file exists
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    exit()

# Load the image
img = cv2.imread(file_path)
if img is None:
    print("Error: Could not load image. Check file format or corruption.")
    exit()

# Convert to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img, cmap='gray')
plt.title("Grayscale Image")
plt.show()

# Apply thresholding
ret1, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret2, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret3, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

# Display thresholded images
plt.imshow(thresh1, cmap='gray')
plt.title("Binary Threshold")
plt.show()

plt.imshow(thresh2, cmap='gray')
plt.title("Binary Inverse Threshold")
plt.show()

plt.imshow(thresh3, cmap='gray')
plt.title("Truncate Threshold")
plt.show()
