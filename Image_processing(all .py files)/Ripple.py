import numpy as np
import matplotlib.pyplot as plt
import cv2
import math

def Ripple(img,tx,ty,ax,ay):
    out = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)
    img_h,img_w = img.shape[:2]
    out_h,out_w = out.shape[:2]
    for i in range(img_h):
        for j in range(img_w):
            x = int(j+(ax*math.sin((2*np.pi*i)/tx)))
            y = int(i+(ay*math.sin((2*np.pi*j)/ty)))
            if 0<=x<img_w and 0<=y<img_h:
                out[i][j] = img[y][x]
    return out
img = cv2.imread(r"C:\Users\WIN\Desktop\image_lab\lab5b\Picture2.png")
out = Ripple(img,tx=30,ty=20,ax=10,ay=10)

plt.figure()
plt.imshow(img[:,:,::-1],'gray')
plt.title('Input')
plt.figure()
plt.imshow(out[:,:,::-1])
plt.title('Output')