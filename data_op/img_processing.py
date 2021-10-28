import time

import openslide
from PIL import Image

import basic_op.file_operation as fop

Image.MAX_IMAGE_PIXELS = None


# 压缩病理切片（w，h参数分别表示长宽的压缩比）
def compress(ori_path, des_path, w, h):
    start_time = time.time()
    print("\tcompress:" + str(time.asctime(time.localtime(time.time()))))
    file_name = fop.get_filename(ori_path)
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
        slide.close()
    print("\tcompress complete:" + str(time.asctime(time.localtime(time.time()))))
    return start_time, file_nums


# 裁剪病理切片，size为需要裁剪的小正方形边长
def crop(ori_path, des_path, size):
    print("\tcrop:" + str(time.asctime(time.localtime(time.time()))))
    # file_path为新文件目录表
    files = fop.get_file_absolute_path(ori_path)
    file_path = fop.generate_paths(ori_path, des_path)
    file_name = fop.get_filename(ori_path)
    # 裁剪每个单独的图并存放到对应的目录下
    for i in range(len(files)):
        img = Image.open(files[i])
        for row in range(1, 11):
            for column in range(1, 11):
                box = ((row - 1) * 1024, (column - 1) * 1024, row * 1024, column * 1024)  # (left, upper, right, lower)
                cropped = img.crop(box)
                cropped.save(file_path[i] + "/" + file_name[i] + "&" + str(row) + "_" + str(column) + ".png")
    print("\tcrop complete:" + str(time.asctime(time.localtime(time.time()))))


# 拼接病理切片
def stitch(ori_path, des_path):
    print("\tstitch:" + str(time.asctime(time.localtime(time.time()))))
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
    print("\tstitch complete:" + str(time.asctime(time.localtime(time.time()))))
    return time.time()


# 图片尺寸归一化，size表示目标尺寸的正方形边长
def normalize_size(ori_path, des_path, size):
    print("\tnormalize_size:" + str(time.asctime(time.localtime(time.time()))))
    files = fop.get_file_absolute_path(ori_path)
    file_name = fop.get_filename(ori_path)
    fop.generate_path(des_path)
    for i in range(len(files)):
        image = Image.open(files[i])
        resized_img = image.resize((size, size))
        resized_img.save(des_path + "/" + file_name[i] + '.png')
    print("\tnormalize_size complete:" + str(time.asctime(time.localtime(time.time()))))


# 病理图片颜色归一化（待定）
def color_normalization():
    print("\tcolor_normalization:" + str(time.asctime(time.localtime(time.time()))))

    print("\tcolor_normalization complete:" + str(time.asctime(time.localtime(time.time()))))
