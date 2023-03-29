# Spot the difference game data

### Sinh viên: Nguyễn Văn Dũng

### MSSV: 20020192

Source code: https://github.com/nvdung1607/spot_difference_game_data

Hình ảnh output, input tại foder: **Image**

# Task 1: Make “spot the difference” game data

## Level 1: Vẽ hình tròn ngẫu nhiên

### Mô tả:

- Vẽ ngẫu nhiên 1 hình tròn nhỏ tại vị trí ngẫu nhiên trong ảnh
- Màu sắc hình tròn tương đồng với màu sắc xung quanh chấm tròn

*Example 1: (input bên trái, output bên phải)*

![Untitled](readme_img/Untitled.png)

*Sử dụng task 2 để khoanh phần khác biệt*

![Untitled](readme_img/Untitled%201.png)

*Example 2:(input bên trái, output bên phải)*                                            

![Untitled](readme_img/Untitled%202.png)

*Sử dụng task 2 để khoanh phần khác biệt*

![Untitled](readme_img/Untitled%203.png)

*Example 3 (input bên trái, output bên phải):*                                    

![Untitled](readme_img/Untitled%204.png)

*Sử dụng task 2 để khoanh phần khác biệt*

![Untitled](readme_img/Untitled%205.png)

### Cách thực hiện:

Import thư viện:

```python
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
from PIL import Image
import os
```

Hiển thị hộp thoại chọn hình ảnh, đọc hình ảnh vào chương trình

```python
# Tạo một cửa sổ tkinter
root = Tk()

# Ẩn cửa sổ tkinter
root.withdraw()

# Hiển thị hộp thoại mở tệp tin
file_path = askopenfilename(filetypes=[("Image files", ".jpg;.jpeg;*.png")])

# Kiểm tra xem người dùng có chọn ảnh hay không
if file_path:
    # Đọc ảnh từ đường dẫn được chọn
    img_origin = cv2.imread(file_path)
    img = img_origin.copy()
```

Chọn vị trí ngẫu nhiên để vẽ hình tròn

```python
		#chọn vị trí vẽ hình tròn
    height, width = img.shape[:2]
    x = np.random.randint(8, width-8)
    y = np.random.randint(8, height-8)
```

Chọn màu của chấm tròn, lấy trung bình màu xung quanh

```python
		#Chọn màu hình tròn bằng cách lấy màu trung bình quanh vị trí
    roi = img[y-8:y+8, x-8:x+8]
    avg_color = np.mean(roi, axis=(0, 1))
    
    #Cộng thêm màu đề tránh trường hợp vẽ trùng với màu nền
    avg_color_1 = avg_color + [20, 20, 20]
```

Vẽ hình tròn lên ảnh và hiện thị ảnh lên màn hình (Cả ảnh gốc và ảnh đã chuyển đổi)

```python
		#Vẽ hình tròn
    # cv2.circle(img, (x, y), 8, [255, 255, 255], -1)
    cv2.circle(img, (x, y), 8, avg_color_1, -1)
    
    #Hiển thị hình ảnh
    result = np.hstack((img_origin, img))
    # cv2.imshow("Image", img_origin)
    # cv2.imshow("Image", img)
    cv2.imshow("Image", result)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

Xuất hình ảnh tại thư mục chứa hình ảnh gốc

```python
		#Xuất hình ảnh
    # Lấy tên file và đường dẫn đến thư mục chứa file
    file_name = os.path.basename(file_path)
    file_dir = os.path.dirname(file_path)
    
    # Tạo tên file đầu ra theo cú pháp "ten_file_lv1out.jpg"
    file_name_out = file_name.split(".")[0] + "_lv1out.png"
    
    # Tạo đường dẫn đến file đầu ra
    file_path_out = os.path.join(file_dir, file_name_out)
    
    # Lưu ảnh đầu ra
    cv2.imwrite(file_path_out, img)
```

## Level 2: Đổi màu đối tượng ngẫu nhiên trong ảnh

### Mô tả:

- Sử dụng **cv2.cvtColor, cv2.threshold** để chuyển đổi thành ảnh nhị phân
- Sử dụng **cv2.findContours** để tìm những đối tượng liên thông trong ảnh
- Lấy ngẫu nhiên 1 đối tượng liên thông trong các contour, có diện tích từ 300 đến 1000 (Để đối tượng được đổi màu dễ phát hiện)
- Đổi màu màu đối tượng đó bằng màu trung bình của xung quanh.

*Example 1 (input bên trái, output bên phải):*                                  

![Untitled](readme_img/Untitled%206.png)

*Sử dụng task 2 để khoanh phần khác biệt*

![Untitled](readme_img/Untitled%207.png)

*Example 2(input bên trái, output bên phải):*                                

![Untitled](readme_img/Untitled%208.png)

*Sử dụng task 2 để khoanh phần khác biệt*

![Untitled](readme_img/Untitled%209.png)

*Example 3 (input bên trái, output bên phải):*

![Untitled](readme_img/Untitled%2010.png)

*Sử dụng task 2 để khoanh phần khác biệt*                                   

![Untitled](readme_img/Untitled%2011.png)

### Cách thực hiện:

Import thư viện: 

```python
import cv2
import numpy as np
import random
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
```

Hiển thị hộp thoại chọn hình ảnh, đọc hình ảnh vào chương trình

```python
# Tạo một cửa sổ tkinter
root = Tk()

# Ẩn cửa sổ tkinter
root.withdraw()

# Hiển thị hộp thoại mở tệp tin
file_path = askopenfilename(filetypes=[("Image files", ".jpg;.jpeg;*.png")])

# Kiểm tra xem người dùng có chọn ảnh hay không
if file_path:
    # Đọc ảnh từ đường dẫn được chọn
    img_origin = cv2.imread(file_path)
    img = img_origin.copy()
```

Sủ dụng ****cv2.cvtColor, cv2.threshold**** chuyển ảnh thành nhị phân

```python
		# Chuyển đổi sang ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Áp dụng bộ lọc canny để phát hiện cạnh
    edges = cv2.Canny(img, 50, 130)

    # Áp dụng phương pháp threshold để chuyển đổi sang ảnh nhị phân
    # _, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
```

Sử dụng **cv2.findContours** để tìm đối tượng liên thông trong ảnh

```python
		# Áp dụng hàm tìm contour để tìm các đối tượng liên thông trong ảnh
    # contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
```

Chọn ngẫu nhiên đối tượng liên thông có diện tích từ 300 đến 100

```python
# Lưu các contour có diện tích 300 đến 100 vào danh sách objects
    objects = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 300 and area < 1000:
            objects.append(contour)

    # Nếu không tìm thấy đối tượng nào có diện tích lớn hơn 300, thoát khỏi chương trình
    if not objects:
        exit()

    # Chọn ngẫu nhiên một đối tượng từ danh sách objects
    selected_contour = random.choice(objects)
```

Đổi màu đối tượng đó

```python
		#Đổi màu bằng màu trung bình
    mean_bgr = cv2.mean(selected_contour)
    cv2.drawContours(img, [selected_contour],-1, mean_bgr, -2)
```

Hiển thị kết quả lên màn hình

```python
		#Hiển thị hình ảnh
    result = np.hstack((img_origin, img))
    # cv2.imshow("Image", img_origin)
    # cv2.imshow("Image", img)
    cv2.imshow("Image", result)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

Xuất hình ảnh tại thư mục chứa hình ảnh gốc

```python
		#Xuất hình ảnh
    # Lấy tên file và đường dẫn đến thư mục chứa file
    file_name = os.path.basename(file_path)
    file_dir = os.path.dirname(file_path)
    
    # Tạo tên file đầu ra theo cú pháp "ten_file_lv1out.jpg"
    file_name_out = file_name.split(".")[0] + "_lv2out.png"
    
    # Tạo đường dẫn đến file đầu ra
    file_path_out = os.path.join(file_dir, file_name_out)
    
    # Lưu ảnh đầu ra
    cv2.imwrite(file_path_out, img)
```

## Level 3: Đổi vị trí của đối tượng

### Mô tả:

- Sử dụng **cv2.cvtColor, cv2.threshold** để chuyển đổi thành ảnh nhị phân
- Sử dụng **cv2.findContours** để tìm những đối tượng liên thông trong ảnh
- Lấy ngẫu nhiên 1 đối tượng liên thông trong các contour, có diện tích từ 300 đến 1000 (Để đối tượng được đổi màu dễ phát hiện)
- Chọn vị trí ngẫu nhiên trong ảnh
- Copy đối tượng đến vị trí ngẫu nhiên đó

*Example 1 (input bên trái, output bên phải):*                                            

![Untitled](readme_img/Untitled%2012.png)

*Sử dụng task 2 để khoanh phần khác biệt*

![Untitled](readme_img/Untitled%2013.png)

*Example 2 (input bên trái, output bên phải):*

![Untitled](readme_img/Untitled%2014.png)

*Sử dụng task 2 để khoanh phần khác biệt*                  

![Untitled](readme_img/Untitled%2015.png)

*Example 3 (input bên trái, output bên phải):*

![Untitled](readme_img/Untitled%2016.png)

*Sử dụng task 2 để khoanh phần khác biệt*

![Untitled](readme_img/Untitled%2017.png)

### Cách thực hiện:

Import thư viện: 

```python
import cv2
import numpy as np
import random
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
```

Hiển thị hộp thoại chọn hình ảnh, đọc hình ảnh vào chương trình

```python
# Tạo một cửa sổ tkinter
root = Tk()

# Ẩn cửa sổ tkinter
root.withdraw()

# Hiển thị hộp thoại mở tệp tin
file_path = askopenfilename(filetypes=[("Image files", ".jpg;.jpeg;*.png")])

# Kiểm tra xem người dùng có chọn ảnh hay không
if file_path:
    # Đọc ảnh từ đường dẫn được chọn
    img_origin = cv2.imread(file_path)
    img = img_origin.copy()
```

Sủ dụng ****cv2.cvtColor, cv2.threshold**** chuyển ảnh thành nhị phân

```python
		# Chuyển đổi sang ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Áp dụng bộ lọc canny để phát hiện cạnh
    edges = cv2.Canny(img, 50, 130)

    # Áp dụng phương pháp threshold để chuyển đổi sang ảnh nhị phân
    # _, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
```

Sử dụng **cv2.findContours** để tìm đối tượng liên thông trong ảnh

```python
		# Áp dụng hàm tìm contour để tìm các đối tượng liên thông trong ảnh
    # contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
```

Chọn ngẫu nhiên đối tượng liên thông có diện tích từ 300 đến 100

```python
# Lưu các contour có diện tích 300 đến 100 vào danh sách objects
    objects = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 300 and area < 1000:
            objects.append(contour)

    # Nếu không tìm thấy đối tượng nào có diện tích lớn hơn 300, thoát khỏi chương trình
    if not objects:
        exit()

    # Chọn ngẫu nhiên một đối tượng từ danh sách objects
    selected_contour = random.choice(objects)
```

Tìm vị trí ngẫu nhiên trong ảnh

```python
		# Tìm vị trí ngẫu nhiên trong ảnh mà không giao với bất kỳ cạnh nào
    rows, cols = img.shape[:2]
    mask = np.zeros((rows, cols), dtype=np.uint8)
    cv2.drawContours(mask, [selected_contour], -1, 255, -1)
    rand_x, rand_y = None, None
    while rand_x is None or mask[rand_x, rand_y] == 255:
        rand_x = np.random.randint(0, rows)
        rand_y = np.random.randint(0, cols)
```

Copy đối tượng đến vị trí ngẫu nhiên đó

```python
		# Copy đối tượng được chọn đến vị trí ngẫu nhiên tìm được
    mask = np.zeros((rows, cols), dtype=np.uint8)
    cv2.drawContours(mask, [selected_contour], -1, 255, -1)
    x, y, w, h = cv2.boundingRect(selected_contour)
    roi = img[y:y+h, x:x+w]
    mask_roi = mask[y:y+h, x:x+w]
    masked_img = cv2.bitwise_and(roi, roi, mask=mask_roi)
    new_x = rand_x - w // 2
    new_y = rand_y - h // 2
    for i in range(new_x, new_x + masked_img.shape[0]):
        for j in range(new_y, new_y + masked_img.shape[1]):
            if i >= 0 and i < rows and j >= 0 and j < cols and mask_roi[i - new_x, j - new_y] != 0:
                img[i, j] = masked_img[i - new_x, j - new_y]
```

Hiển thị kết quả lên màn hình

```python
		#Hiển thị hình ảnh
    result = np.hstack((img_origin, img))
    # cv2.imshow("Image", img_origin)
    # cv2.imshow("Image", img)
    cv2.imshow("Image", result)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

Xuất hình ảnh vào thực mục chứa ảnh gốc

```python
		#Xuất hình ảnh
    # Lấy tên file và đường dẫn đến thư mục chứa file
    file_name = os.path.basename(file_path)
    file_dir = os.path.dirname(file_path)
    
    # Tạo tên file đầu ra theo cú pháp "ten_file_lv1out.jpg"
    file_name_out = file_name.split(".")[0] + "_lv3out.png"
    
    # Tạo đường dẫn đến file đầu ra
    file_path_out = os.path.join(file_dir, file_name_out)
    
    # Lưu ảnh đầu ra
    cv2.imwrite(file_path_out, img)
```

# Task 2: Solve game in task 1

### Mô tả:

- Đọc vào 2 ảnh bao gồm ảnh gốc và ảnh đã chuyển đổi của task 1 ( có thể sử dụng bất kì ảnh nào có cùng kích thước, chương trình sẽ tìm ra mọi sự khác biệt)
- Chuyển 2 ảnh đầu vào thành ảnh xám bằng **cv2.cvtColor**
- Sử dung **cv2.absdiff** để tìm điểm khác biệt
- Sử dụng **cv2.threshold** để chuyển ảnh nhị phân
- Sử dụng **np.ones** để làm rõ phần khác biệt
- Sử dụng **cv2.findContours** để tìm các đối tượng liên thông từ dilate
- Vẽ hình chữ nhật bao quanh các đối tượng liên thông đó
- In kết quả ra màn hình

Example 1: 

![Untitled](readme_img/Untitled%201.png)

![Untitled](readme_img/Untitled%207.png)

![Untitled](readme_img/Untitled%2015.png)

### Cách thực hiện

Import thư viện:

```python
import cv2
import imutils 
import numpy as np
```

Load 2 ảnh cần so sánh (cần chủ động thay đổi đường dẫn trong code)

```python
#Load the image
img1 = cv2.imread(r'image\img_data_3.png')
img1 = cv2.resize(img1, (600, 600))
img2 = cv2.imread(r'image\img_data_3_lv3out.png')
img2 = cv2.resize(img2, (600, 600))
```

Chuyển thành ảnh xám, tìm điểm khác biệt

```python
#Grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#find the difference
diff = cv2.absdiff(gray1, gray2)
# cv2.imshow('diff(img1, img2)', diff)
```

Xử lý làm to, rõ phần khác biệt

```python
#Apply threshold
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# cv2.imshow('Threshold', thresh)

#Dilation
kernel = np.ones((5,5), np.uint8)
dilate = np.ones(thresh, kernel, iterations=2)
# cv2.imshow('Dilation', dilate)
```

Tìm các phần liên thông

```python
#Find contours
contours = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
```

Vẽ hình chữ nhật màu đỏ xung quanh các phần liên thông đó

```python
#Loop over each contour
for contour in contours:
    if cv2.contourArea(contour) > 100:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img1, (x, y), (x+w, y+h), (0,0,255), 2)
        cv2.rectangle(img2, (x, y), (x+w, y+h), (0,0,255), 2)
```

Hiển thị kết quả lên màn hình

```python
#show final images
x = np.zeros((600, 10, 3), np.uint8)
result = np.hstack((img1, img2))
cv2.imshow("diffences", kernel)

# cv2.imshow('Original Img', img1)
# cv2.imshow('Edited Img', img2)

cv2.waitKey(0)
cv2.destroyAllWindows
```