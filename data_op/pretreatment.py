import time

import openslide
from PIL import Image

import basic_op.file_operation as fop

Image.MAX_IMAGE_PIXELS = None


# 压缩病理切片（w，h参数分别表示长宽的压缩比）
def compress(ori_path, des_path, w, h):
    print("\tcompress:" + str(time.asctime(time.localtime(time.time()))))
    file_name = fop.get_filename(ori_path)
    list_name = fop.get_absolute_path(ori_path)
    fop.generate_path(des_path)
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
    print("\tcompress complete:" + str(time.asctime(time.localtime(time.time()))))


# 裁剪病理切片
def cut(ori_path, des_path, size):
    print("\tcut:" + str(time.asctime(time.localtime(time.time()))))
    # file_path为新文件目录表
    file_path = fop.generate_paths(ori_path, des_path)
    for i in range(len(ori_path)):
        img = Image.open("./data/cut/thor.jpg")
        print(img.size)
        cropped = img.crop((0, 0, 512, 128))  # (left, upper, right, lower)
        cropped.save("./data/cut/pil_cut_thor.jpg")
    print("\tcut complete:" + str(time.asctime(time.localtime(time.time()))))


# 病理图片颜色归一化（待定）
def color_normalization():
    print("\tcolor_normalization:" + str(time.asctime(time.localtime(time.time()))))

    print("\tcolor_normalization complete:" + str(time.asctime(time.localtime(time.time()))))
