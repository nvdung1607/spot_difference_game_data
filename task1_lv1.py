#Vẽ hình tròn với bán kính bằng 8px, 
# vị trí ngẫu nhiên
# màu trung bình tại vị trí đó

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
from PIL import Image
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
    
    #chọn vị trí vẽ hình tròn
    height, width = img.shape[:2]
    x = np.random.randint(8, width-8)
    y = np.random.randint(8, height-8)

    #Chọn màu hình tròn bằng cách lấy màu trung bình quanh vị trí
    roi = img[y-8:y+8, x-8:x+8]
    avg_color = np.mean(roi, axis=(0, 1))
    
    #Cộng thêm màu đề tránh trường hợp vẽ trùng với màu nền
    avg_color_1 = avg_color + [20, 20, 20]

    print(avg_color, ' ', avg_color_1, ' ', x,' ', y)

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
    