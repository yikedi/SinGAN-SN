# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 21:44:28 2019

@author: douglas
"""

from PIL import Image

import os
import numpy as np


def resize_all(scale,mode):
    
    dir_name = 'C:/Users/douglas/Desktop/temp_picture/'+ mode + '/' + scale + '/'
    out_dir = 'C:/Users/douglas/Desktop/resize/' + mode + '/' + scale + '/'
    resize_ratio = 0.5
    for file_name in os.listdir(dir_name):
        file_name_1 = os.path.abspath(dir_name + file_name)
        image = Image.open(file_name_1)
        shape = image.size
        w = int(shape[0] * resize_ratio)
        h = int(shape[1] * resize_ratio)
        image_resize = image.resize(size = (w,h))
        dst = os.path.abspath(out_dir + file_name)
        image_resize.save(dst,format='PNG')
        
def get_samples_from_dir(dir_name,image_list):
    
    files = os.listdir(dir_name)
    index = np.random.choice(49,10,replace = False)
    for j in index:
        image = Image.open(dir_name + '/' + files[j])
        image_list.append(image)
    
    return image_list

image_list = []
output_folder = 'C:/Users/douglas/Desktop/syde671/SinGAN-master/SinGAN-master/Output/RandomSamples/' 
image_folders = ['balloons','cars','mountains','starry_night','zebra']
gen_start_scale = 'gen_start_scale=1'
sn = '_1'

for i in range(len(image_folders)):
    image_folder = image_folders[i] + sn + '/'
    dir_name = output_folder + image_folder + gen_start_scale
    get_samples_from_dir(dir_name,image_list)

dst_dir = 'C:/Users/douglas/Desktop/syde671/SinGAN-master/SinGAN-master/SIFID/SIFID_images/fake_sn_scale_1/'
for i in range(len(image_list)):
    image = image_list[i]
    image.save(dst_dir + str(i) + '.png')
    

    
real_image_dir = 'C:/Users/douglas/Desktop/syde671/SinGAN-master/SinGAN-master/Input/Images/'
dst_dir_real = 'C:/Users/douglas/Desktop/syde671/SinGAN-master/SinGAN-master/SIFID/SIFID_images/real1/'
count = 0
for file_name in image_folders:
    image = Image.open(real_image_dir + file_name + '.png')
    for i in range(10):
        image.save(dst_dir_real + str(count)+'.png')
        count = count + 1
    
image_list[0].show()


    