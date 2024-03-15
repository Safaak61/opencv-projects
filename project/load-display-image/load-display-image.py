import cv2
img = cv2.imread("photo_2024-03-14_10-08-39.jpg")
print(f"Yükseklik {img.shape[0]}   Genişlik = {img.shape[1]}")
timg = cv2.putText(img, "Harry Potter", (195,340), 0, 2, (0,0,0), 4, 0)
s = 0.5 # ölçekleme
rimg = cv2.resize(timg, (int(s*img.shape[1]), int(s*img.shape[0])), 0)
cv2.imshow("HarryPotter", rimg)
cv2.waitKey(0)
cv2.imwrite("HarryPotter.jpg", timg, [cv2.IMWRITE_JPEG_QUALITY,50])
