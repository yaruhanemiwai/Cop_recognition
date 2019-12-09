#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import glob
import cv2

import h5py
from PIL import Image
import sys,os
import copy
import random
import shutil
   
def main():
    #Setting
    num = 4000
    size_input = 60
    size_label = 1    
    data_dir = "./train/"
    img_dir = []
    count = 0
    data = np.zeros([size_input,size_input,1,num],dtype = np.float32)
    label = np.zeros([size_label,size_label,1,num],dtype = np.uint8)
    
    for iii in os.listdir(data_dir):
        for iv in os.listdir(data_dir + str(iii)):
            img_dir.append(str(iii) + "/" +str(iv))         
    random.shuffle(img_dir) 
    
    path_txt = open(data_dir +  "path_train.txt",mode = "a")
    f = data_dir + './train.h5'
    outfh = h5py.File(f,"w")  
    
    for i in img_dir:              
            img = cv2.imread(data_dir + i,0)
            data[:,:,0,count] = (img*1.0/255).astype(np.float32)
            label[0,0,0,count] = i[0]
            print(str(count) + " " + i[0] + " " + i)
            count += 1          
            
    outfh.create_dataset('data',data = data.transpose(3,2,0,1))
    outfh.create_dataset('label',data = label.transpose(3,2,0,1))
    outfh.flush()
    outfh.close()  
    path_txt.write(f+"\n")
    path_txt.close()     

if __name__ == '__main__':
    main()
