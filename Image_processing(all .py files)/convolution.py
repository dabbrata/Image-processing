# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 00:00:20 2023

@author: WIN
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2

def FlipKernel(kernel):
    k_h,k_w = kernel.shape
    k = np.zeros_like(kernel)
    for i in range(k_h):
        for j in range(k_w):
            k[i][j] = kernel[k_h-i-1][k_w-j-1]
    return k

def Convolution(img,kernel):
    kernel = FlipKernel(kernel)
    k_h,k_w = kernel.shape
    res = np.zeros_like(img)
    padded_img = np.pad(img,(k_h//2,k_w//2),mode='constant')
    p_h,p_w = padded_img.shape
    i_h,i_w = img.shape
    for i in range(i_h):
        for j in range(i_w):
            neighbour = padded_img[i:i+k_h,j:j+k_w]
            result = neighbour*kernel
            summ = np.sum(result)
            res[i][j] = summ
    return res
            
#convolution with (1,1) position kernel
def Convolution2(img,kernel):
    kernel = FlipKernel(kernel)
    k_h,k_w = kernel.shape
    res = np.zeros_like(img)
    padded_img = cv2.copyMakeBorder(img, top=1, bottom=k_h-2, left=1, right=k_w-2, borderType=None)
    p_h,p_w = padded_img.shape
    i_h,i_w = img.shape
    for i in range(p_h-k_h+1):
        for j in range(p_w-k_w+1):
            neighbour = padded_img[i:i+k_h,j:j+k_w]
            result = neighbour*kernel
            summ = np.sum(result)
            res[i][j] = summ
    return res
            


img = cv2.imread(r"C:\Users\WIN\Desktop\image_lab\Lena.jpg",0)
plt.figure()
plt.imshow(img,'gray')


kernel = np.array(([-2,0,-1,0,0],
                   [0,-2,-1,0,0],
                   [-1,-1,1,1,1],
                   [0,0,1,2,0],
                   [0,0,1,0,2])).astype(np.uint8)
k2=np.ones((9,9))/81
output = Convolution(img, k2)
plt.figure()
plt.imshow(output,'gray')
plt.show()

print(img.shape)
print(output.shape)
