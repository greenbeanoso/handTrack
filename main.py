import cv2
import numpy as np

# 讀取圖像，並檢查是否成功讀取
INimg = cv2.imread('test.jpg')
if INimg is None:
    print("圖像讀取失敗，請確認檔案路徑是否正確。")
else:
    print("圖像成功讀取！")

# 將圖像進行縮放
INimg = cv2.resize(INimg, (0, 0), fx=0.2, fy=0.2)
def DoSubdivs(img,num):
    w = img.shape[1]
    h = img.shape[0]
    Wsize = w / num
    Hsize = h / num
    
def brighten(Aimg,Bimg):
     # 將圖像轉為 int32，防止溢出
    Aimg = Aimg.astype(np.int32)
    Bimg = Bimg.astype(np.int32)

    # 所有通道一起加，然後進行範圍限制
    Aimg += Bimg
    Aimg = np.clip(Aimg, 0, 255)

    # 最後轉回 uint8
    return Aimg.astype(np.uint8)
def Update(img, br, bb, bg, cA, cB,subdivs):
    img_copy = img.copy()

    # 調整顏色通道，使用滑桿返回的值作為比例
    img_copy[:, :, 0] = np.clip(img_copy[:, :, 0] * (1 - bb / 255), 0, 255)  # 藍色通道
    img_copy[:, :, 1] = np.clip(img_copy[:, :, 1] * (1 - bg / 255), 0, 255)  # 綠色通道
    img_copy[:, :, 2] = np.clip(img_copy[:, :, 2] * (1 - br / 255), 0, 255)  # 紅色通道

    # 執行 Canny 邊緣檢測
    edges = cv2.Canny(img_copy, cA, cB)
    
    # 將單通道的 Canny 邊緣圖轉為三通道，以便與原圖像疊加
    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # 顯示結果圖像
    cv2.imshow('canny', edges)
    cv2.imshow('rgb+canny', brighten(img_copy, edges_colored))
    cv2.imshow('original+canny', brighten(img, edges_colored))
    cv2.imshow('subdivs', DoSubdivs(img,subdivs))
def TrackUpdate(val):
    br = cv2.getTrackbarPos('R', 'trackbar')
    bg = cv2.getTrackbarPos('G', 'trackbar')
    bb = cv2.getTrackbarPos('B', 'trackbar')
    cA = cv2.getTrackbarPos('CannyA', 'trackbar')
    cB = cv2.getTrackbarPos('CannyB', 'trackbar')
    subdivs = cv2.getTrackbarPos('subdivs', 'trackbar')
    Update(INimg, br, bb, bg,cA,cB,subdivs)
# 創建一個視窗
cv2.namedWindow('trackbar')

cv2.createTrackbar('R', 'trackbar', 0, 255, TrackUpdate)
cv2.createTrackbar('G', 'trackbar', 0, 255, TrackUpdate)
cv2.createTrackbar('B', 'trackbar', 0, 255, TrackUpdate)
cv2.createTrackbar('CannyA', 'trackbar', 50, 500, TrackUpdate)
cv2.createTrackbar('CannyB', 'trackbar', 50, 500, TrackUpdate)
cv2.createTrackbar('subdivs', 'trackbar', 5, 10, TrackUpdate)
# 等待用戶按下 'r' 鍵來退出
while True:
    key = cv2.waitKey(0) & 0xFF
    if key == ord('k'):  # 如果按下的是 'q' 鍵
        break
    

# 銷毀所有視窗
cv2.destroyAllWindows()

# def RigTracker(img):
#     img_copy[:, :,  0] = 
