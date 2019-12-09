#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import os
import numpy as np
import sys
import copy
   
def videotoframe(file_name,count):

    file_name = str(file_name)
    ii = copy.copy(file_name[:2])
    print(file_name)
    video = cv2.VideoCapture("./movie_1/" + file_name)
    frame_count = int(video.get(7))
    
    for i in range(frame_count):
               
        _, frame = video.read()
        
        if ii == "HL":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.resize(frame[:,20:140],(60,60),interpolation = cv2.INTER_NEAREST)
            cv2.imwrite("./img/0/" + str(int(i + count)) + ".bmp", frame)
        elif ii =="HR":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.resize(frame[:,20:140],(60,60),interpolation = cv2.INTER_NEAREST)
            cv2.imwrite("./img/1/" + str(int(i + count)) + ".bmp", frame)
        elif ii =="CL":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.resize(frame[:,20:140],(60,60),interpolation = cv2.INTER_NEAREST)
            cv2.imwrite("./img/2/" + str(int(i + count)) + ".bmp", frame)
        elif ii == "CR":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.resize(frame[:,20:140],(60,60),interpolation = cv2.INTER_NEAREST)
            cv2.imwrite("./img/3/" + str(int(i + count)) + ".bmp", frame)
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.resize(frame[:,20:140],(60,60),interpolation = cv2.INTER_NEAREST)
            cv2.imwrite("./img/4/" + str(int(i + count)) + ".bmp", frame)
        
    video.release()
            
    return frame_count

def main():

    video_list = os.listdir("./movie_1/")
    count = np.zeros(5)
    count[4] = 612
    
    for i in video_list:
        
        video_name = copy.copy(i)
        
        if video_name[:2] == "HL":
            ii = count[0]
            counter = videotoframe(i,ii)
            count[0] += counter
        elif video_name[:2] == "HR":
            ii = count[1]
            counter = videotoframe(i,ii)
            count[1] += counter
        elif video_name[:2] == "CL":
            ii = count[2]
            counter = videotoframe(i,ii)
            count[2] += counter
        elif video_name[:2] == "CR":
            ii = count[3]
            counter = videotoframe(i,ii)
            count[3] += counter
        else:
            ii = count[4]
            counter = videotoframe(i,ii)            
            count[4] += counter
                    
if __name__ == '__main__':
    main()  
