import time

import color_transfer
import matplotlib as plt
import numpy as np
import openslide
from PIL import Image
from sklearn import preprocessing

import basic_op.file_operation as fop
import basic_op.log_operation as log

Image.MAX_IMAGE_PIXELS = None


# 压缩病理切片（w，h参数分别表示长宽的压缩比）
def compress(ori_path, des_path, w, h):
    start_time = time.time()
    # print("\tcompress:" + str(time.asctime(time.localtime(time.time()))))
    log.log_time("\tcompress:")
    file_name = fop.get_filename(ori_path)
    log.log_data(file_name)
    log.log_data("Total:" + str(len(file_name)))
    list_name = fop.get_file_absolute_path(ori_path)
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
        save_img.close()
        slide.close()
    # print("\tcompress complete:" + str(time.asctime(time.localtime(time.time()))))
    log.log_time("\tcompress complete:")


# 裁剪病理切片，size为需要裁剪的小正方形边长
def crop(ori_path, des_path, size):
    # print("\tcrop:" + str(time.asctime(time.localtime(time.time()))))
    log.log_time("\tcrop:")
    # file_path为新文件目录表
    files = fop.get_file_absolute_path(ori_path)
    file_path = fop.generate_paths(ori_path, des_path)
    file_name = fop.get_filename(ori_path)
    # 裁剪每个单独的图并存放到对应的目录下
    for i in range(len(files)):
        # img = np.array(Image.open(files[i]))
        # for row in range(1, 11):
        #     for column in range(1, 11):
        #         crop = img[(row - 1) * 1024:row * 1024, (column - 1) * 1024:column * 1024:]
        #         plt.imsave(file_path[i] + "/" + file_name[i] + "&" + str(row) + "_" + str(column) + ".png", crop)
        img = Image.open(files[i])
        result = []
        for row in range(1, 11):
            for column in range(1, 11):
                box = ((row - 1) * 1024, (column - 1) * 1024, row * 1024, column * 1024)  # (left, upper, right, lower)
                cropped = img.crop(box)
                result.append(cropped)
                # cropped.save(file_path[i] + "/" + file_name[i] + "&" + str(row) + "_" + str(column) + ".png")
        row, column = (1, 1)
        for j in range(100):
            if column == 11:
                row += 1
                column = 0
            result[j].save(file_path[i] + "/" + file_name[i] + "&" + str(row) + "_" + str(column) + ".png")
            column += 1
    # print("\tcrop complete:" + str(time.asctime(time.localtime(time.time()))))
    log.log_time("\tcrop complete:")


# 拼接病理切片
def stitch(ori_path, des_path):
    # print("\tstitch:" + str(time.asctime(time.localtime(time.time()))))
    log.log_time("\tstitch:")
    file_path = fop.get_file_absolute_path(ori_path)
    fop.generate_path(des_path)
    for i in range(len(file_path)):
        file_name = fop.get_filename(file_path[i])
        image = Image.new("RGB", (10240, 10240))
        for j in range(len(file_name)):
            row = int(file_name[j].split("&", 1)[1].split("_", 1)[0])
            column = int(file_name[j].split("&", 1)[1].split("_", 1)[1])
            img = Image.open(file_path[i] + "/" + file_name[j] + ".png")
            box = ((row - 1) * 1024, (column - 1) * 1024, row * 1024, column * 1024)
            image.paste(img, box)
        image.save(des_path + "/" + file_name[i].split("&", 1)[0] + ".png")
    # print("\tstitch complete:" + str(time.asctime(time.localtime(time.time()))))
    log.log_time("\tstitch complete:")


# 图片尺寸归一化，size表示目标尺寸的正方形边长
def normalize_size(ori_path, des_path, size):
    # print("\tnormalize_size:" + str(time.asctime(time.localtime(time.time()))))
    log.log_time("\tnormalize_size:")
    files = fop.get_file_absolute_path(ori_path)
    file_name = fop.get_filename(ori_path)
    fop.generate_path(des_path)
    for i in range(len(files)):
        image = Image.open(files[i])
        resized_img = image.resize((size, size))
        resized_img.save(des_path + "/" + file_name[i] + '.png')
    # print("\tnormalize_size complete:" + str(time.asctime(time.localtime(time.time()))))
    log.log_time("\tnormalize_size complete:")


# 病理图片颜色归一化（待定）
def normalize_color(ori_path, des_path, standard_path):
    print("\tcolor_normalization:" + str(time.asctime(time.localtime(time.time()))))
    log.log_time("\tnormalize_color:")
    standard = np.array(Image.open(standard_path))
    fop.generate_path(des_path)
    file_path = fop.get_file_absolute_path(ori_path)
    file_name = fop.get_filename(ori_path)
    for i in range(len(file_path)):
        img = np.array(Image.open(file_path[i]))
        img = Image.fromarray(color_transfer(standard, img))
        img.save(des_path + "/" + file_name[i] + ".png")
    print("\tcolor_normalization complete:" + str(time.asctime(time.localtime(time.time()))))
    log.log_time("\tnormalize_color complete:")
