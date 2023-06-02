import cv2
import pytesseract

image = cv2.imread('tets-1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = 255 - cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Blur and perform text extraction(you can use raw image)
thresh = cv2.GaussianBlur(thresh, (3,3), 0)
data = pytesseract.image_to_string(thresh, lang='eng+ben', config='--psm 6')
print(data)
# f = open('path_to_desktop/file.txt', 'w')
with open('beng.txt', 'w') as f:
    f.writelines(data)