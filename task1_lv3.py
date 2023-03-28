#Chọn những vùng liên thông trong ảnh (sử dụng contour)
#Lấy ngẫu nhiên 1 đối tượng từ contours
#Đổi vị trí ngẫu nhiên cho đối tượng đó

import cv2
import numpy as np
import random
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

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
        
    # Chuyển đổi sang ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Áp dụng bộ lọc canny để phát hiện cạnh
    edges = cv2.Canny(img, 50, 130)

    # Áp dụng phương pháp threshold để chuyển đổi sang ảnh nhị phân
    # _, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]

    # Áp dụng hàm tìm contour để tìm các đối tượng liên thông trong ảnh
    # contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Lưu các contour có diện tích lớn hơn 300 vào danh sách objects
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

    # Tìm vị trí ngẫu nhiên trong ảnh mà không giao với bất kỳ cạnh nào
    rows, cols = img.shape[:2]
    mask = np.zeros((rows, cols), dtype=np.uint8)
    cv2.drawContours(mask, [selected_contour], -1, 255, -1)
    rand_x, rand_y = None, None
    while rand_x is None or mask[rand_x, rand_y] == 255:
        rand_x = np.random.randint(0, rows)
        rand_y = np.random.randint(0, cols)

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


    #Hiển thị hình ảnh
    result = np.hstack((img_origin, img))
    # cv2.imshow("Image", img_origin)
    # cv2.imshow("Image", img)
    cv2.imshow("Image", result)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
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