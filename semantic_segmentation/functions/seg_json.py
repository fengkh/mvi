import json
import time

import os
import json
import cv2
import matplotlib.pyplot as plt
import numpy as np
import system_operation.file as fop
import system_operation.log as log
from PIL import Image


def magnify(ori_path, des_path, ratio):
    print("\tseg_magnify:" + str(time.asctime(time.localtime(time.time()))))
    log.log_line()
    start = log.log_time("\tseg_magnify:")
    if not os.path.exists(des_path):
        os.makedirs(des_path)
    files = fop.get_files_ab_path(ori_path)
    for i in range(len(files)):
        file_name = fop.get_just_filename(ori_path)
        json_file = os.path.join(ori_path, file_name[i] + '.json')
        save_to = open(os.path.join(des_path, file_name[i] + '.json'), 'w')
        with open(json_file, 'rb') as f:
            anno = json.load(f)
            for shape in anno["shapes"]:
                points = shape["points"]
                points = (np.array(points) * ratio).astype(int).tolist()
                shape["points"] = points
            json.dump(anno, save_to, indent=4)
    print("\tseg_magnify complete:" + str(time.asctime(time.localtime(time.time()))))
    end = log.log_time("\n\tseg_magnify complete:")
    log.log_speed(start, end, len(files))
    log.log_line()


# 删除json文件中imagedata内容并将size改为10240
def json_content(ori_path, des_path):
    print("\tjson_content:" + str(time.asctime(time.localtime(time.time()))))
    log.log_line()
    start = log.log_time("\tjson_content:")
    files = fop.get_files_ab_path(ori_path)
    file_name = fop.get_just_filename(ori_path)
    for i in range(len(files)):
        save = des_path + "/" + file_name[i] + ".json"
        with open(files[i], "rb") as fp:
            anno = json.load(fp)
            anno['imageData'] = ""
            anno['imageWidth'] = "10240"
            anno['imageHeight'] = '10240'
            json.dump(anno, open(save, "w"), indent=4)
    print("\tjson_content complete:" + str(time.asctime(time.localtime(time.time()))))
    end = log.log_time("\n\tjson_content complete:")
    log.log_speed(start, end, len(files))
    log.log_line()


def generate_dataset(ori_path, des_path):
    log.log_line()
    start = log.log_time("\tgenerate_dataset:")
    fop.generate_path(des_path + "/label")
    fop.generate_path(des_path + "/image")
    file_names = fop.get_just_filename(ori_path)
    for i in range(len(file_names)):
        father_path = ori_path + "/" + file_names[i]
        img = Image.open(father_path + "/img.png")
        label = Image.open(father_path + "/label.png")
        img.save(des_path + "/image/" + file_names[i] + ".png")
        label.save(des_path + "/label/" + file_names[i] + ".png")
    end = log.log_time("\n\tgenerate_dataset complete:")
    log.log_speed(start, end, len(file_names))
    log.log_line()


def img_24to8():
    bacepath = "D:\code_python/unet-master\data\membrane/train\image"
    savepath = 'D:\_mvi/test'

    f_n = os.listdir(bacepath)

    for n in f_n:
        imdir = bacepath + "/" + n
        img = cv2.imread(imdir)
        # print(imdir)
        cropped = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(savepath + "/" + n, cropped)  # NOT CAHNGE THE TYPE


def generate_mask(ori_path, des_path):
    json_files = fop.get_files_ab_path(ori_path + "/json")
    png_files = fop.get_files_ab_path(ori_path + "/png")
    file_name = fop.get_just_filename(ori_path + "/png")
    # print(file_name)
    # print(json_files)
    tmp = {}
    for i in range(len(json_files)):
        with open(json_files[i], "r") as f:
            tmp = f.read()
        tmp = json.loads(tmp)
        points = []
        for j in range(len(tmp["shapes"])):
            if tmp["shapes"][j]["label"] == '2':
                for k in range(len(tmp["shapes"][j]["points"])):
                    points.append(tmp["shapes"][j]["points"][k])
        points = np.array(points, np.int32)
        if len(points) is not 0:
            img = cv2.imread(png_files[i])
            # BGR->RGB
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # box = tmp["shapes"][1]["points"]
            # box = np.array(box, np.int32)
            mask = np.zeros_like(img)
            # cv2.rectangle(img, (box[0][0], box[0][1]), (box[1][0], box[1][1]), (125, 125, 125), 2)
            # cv2.polylines(img, [points], 1, (0,0,255))
            cv2.fillPoly(mask, [points], (255, 255, 255))
            img_add = cv2.addWeighted(mask, 0.3, img, 0.7, 0)
            cv2.imwrite(des_path + "/label_2/" + file_name[i] + "_json.png", mask)


generate_mask("D:\seg","D:\seg/test")