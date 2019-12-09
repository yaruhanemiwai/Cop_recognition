#!/usr/bin/env python
# -- coding: utf-8 -- 

import os,sys,cv2
sys.path.insert(0,os.path.join('/home/es1video4/caffe','python'))
sys.path.append('/home/es1video4/workspace/iwamine/src/')
import caffe
import numpy as np

MODEL_FILE="./deploy.prototxt"
CATEGORY_FILE="label.txt"

folder_data = "./val/"

def main():

    pycaffe_dir = os.path.dirname(__file__)
    images_dim = "60,60"        
    raw_scale = 1.0    
    image_dims = [int(s) for s in images_dim.split(',')]
    img_dir = []

    caffe.set_mode_gpu()
    
    txt = open("result.txt",mode = "a")
    
    for iii in os.listdir(folder_data):
        for iv in os.listdir(folder_data + str(iii)):
            img_dir.append(str(iii) + "/" +str(iv))
    
    for ii in range(1,101):    
        PRETRAINED_MODEL_FILE="./result/model_iter_" + str(ii*1000) + ".caffemodel"
        
        classifier = caffe.Classifier(MODEL_FILE, PRETRAINED_MODEL_FILE,image_dims=image_dims, #03
        #mean=mean,input_scale=input_scale, 
        raw_scale=raw_scale,#channel_swap=channel_swap
        )
        txt.write("\niter_" + str(ii*1000) + "\n")
           
        for v in img_dir:
            input_file = folder_data + str(v)

            scores = Classify(input_file,classifier)
            prediction = zip(scores[0].tolist(), numpy.loadtxt(CATEGORY_FILE, str, delimiter="\t"))
            prediction.sort(cmp=lambda x, y: cmp(x[0], y[0]), reverse=True)
            
            txt.write(str(v) + " " + str(prediction[0]) + "\n")
            
    txt.close()

def Classify(img_file,classifier):

    inputs = cv2.imread(img_file,0)
    inputs = (inputs*1.0/255).astype(np.float32)
    inputs = inputs[:,:,np.newaxis]
    predictions = make_model.Classify(inputs,classifier)
    return predictions

if __name__ == '__main__':
    main()

#python classify_new.py --raw_scale 255 ../101_ObjectCategories/airplanes/image_0001.jpg
