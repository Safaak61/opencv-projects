# OpenCV PROJECTS
## load-display-image
Bu egzersizde <b>OpenCV</b> kütüphanesinin <b>imread()</b>, <b>putText()</b>, <b>resize()</b>, <b>imshow()</b> ve <b>imwrite()</b> fonksiyonlarını kullanacağız. Resim yüklemek için kullandığımız fonksiyon olan <b>imread()</b>, argüman (yani giriş) olarak uzantısıyla beraber resim/fotoğraf ismi kabul ediyor. Yani fonksiyona <i>string</i> veri tipinde resmin uzantılı ismini giriş olarak veriyoruz. Mesela burada fotoğrafımızın ismi <b>IMG_20210616_202539.jpg</b> olduğundan <b>imread('IMG_20210616_202539.jpg')</b> şeklinde fonksiyonu çağırdığımızda resmi bizim ismini verdiğimiz değişkene atıyor. Bu arada gözden kaçırmayın, bütün fonksiyonları her zaman <b>cv2</b> anahtar kelimemizin sonuna <b>nokta</b> koyup çağırıyoruz, çünkü <b>cv2</b> yazdığımız kodda <b>OpenCV</b> kütüphanesini temsil ediyor. Zaten bu yüzden her kodumuzun başında <b>import cv2</b> diye bir komutla <b>OpenCV</b>'yi aktif hale getirmiş oluyoruz. Sonuç olarak, eğer <b>IMG_20210616_202539.jpg</b> isimli bir fotoğrafı OpenCV'de <b>resim</b> isminde bir değişkene atamak istiyorsak, o zaman aşağıdaki kodu koşturmalıyız.

```
import cv2
img = cv2.imread("photo_2024-03-14_10-08-39.jpg")
print(f"Yükseklik {img.shape[0]}   Genişlik = {img.shape[1]}")
timg = cv2.putText(img, "HarryPotter", (175,300), 0, 2, (255,0,0), 4, 0)
s = 0.5 # ölçekleme
rimg = cv2.resize(timg, (int(s*img.shape[1]), int(s*img.shape[0])), 0)
cv2.imshow("HarryPotter", rimg)
cv2.waitKey(0)
cv2.imwrite("HarryPotter.jpg", timg, [cv2.IMWRITE_JPEG_QUALITY,50])
```

<img src="project/load-display-image/HarryPottr.jpg" alt="Safa Ak Harry Potter" width="500" height=auto>