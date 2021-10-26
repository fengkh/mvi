import time

import openslide
from PIL import Image

import basic_op.file_operation as fop

Image.MAX_IMAGE_PIXELS = None


# 压缩病理切片（w，h参数分别表示长宽的压缩比）
def compress(ori_path, des_path, w, h):
    print("\t开始压缩文件:" + str(time.asctime(time.localtime(time.time()))))
    list_name = []
    file_name = fop.no_tail(ori_path)
    fop.listdir(ori_path, list_name)
    fop.mkdir(des_path)
    file_nums = len(list_name)
    for i in range(file_nums):
        image_path = list_name[i]
        slide = openslide.open_slide(image_path)
        [W, H] = slide.level_dimensions[0]
        # print(file_name[i] + '----', W, H)
        save_img = slide.get_thumbnail((W / w, H / h))
        save_path = des_path + "/" + file_name[i] + '.png'
        save_img.save(save_path)
        slide.close()
    print("\t图片压缩完成:" + str(time.asctime(time.localtime(time.time()))))
