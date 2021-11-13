import glob
import json
import os
import time

import numpy as np

import basic_op.file as fop
import basic_op.log as log


def magnify(ori_path, des_path, ratio):
    print("\tseg_magnify:" + str(time.asctime(time.localtime(time.time()))))
    log.log_line()
    start = log.log_time("\tseg_magnify:")
    if not os.path.exists(des_path):
        os.makedirs(des_path)
    files = fop.get_file_absolute_path(ori_path)
    for i in range(len(files)):
        file_name = fop.get_filename(ori_path)
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
    files = fop.get_file_absolute_path(ori_path)
    file_name = fop.get_filename(ori_path)
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


