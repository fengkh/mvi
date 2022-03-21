import random
import time
import os
from color_transfer import color_transfer
import numpy as np
import openslide
from PIL import Image
# import file as fop
import system_operation.file as fop
import system_operation.log as log

Image.MAX_IMAGE_PIXELS = None


# 根据txt文件筛选出目标文件,记得把txt文件放到同一个目录下
def get_txt_file(txt_path, ori_path):
    # log.log_line()
    # start = log.log_time("\tCompress One:")
    my_list = []
    with open(txt_path + "/file_path.txt", "r") as f:
        line = f.readline()
        while line:
            my_list.append(txt_path + "/" + line.strip("\n") + ".mrxs")
            line = f.readline()
        f.close()
    # print(my_list)
    for i in range(len(my_list)):
        if os.path.exists(my_list[i]):
            compress_one(my_list[i], ori_path, 7, 7)
        else:
            with open(ori_path + "\lost.txt", "a+") as lost:
                lost.write(my_list[i].split("/")[-1] + "\n")
                lost.close()
    # log.log_line()


def compress_one(ori_path, des_path, w, h):
    file_name = ori_path.split("/")[-1]
    save_path = des_path + "/" + file_name.split(".")[0] + ".png"
    if not os.path.exists(save_path):
        slide = openslide.open_slide(ori_path)
        [W, H] = slide.level_dimensions[0]
        # print(file_name[i] + '----', W, H)
        save_img = slide.get_thumbnail((W / w, H / h))
        save_img = save_img.resize((10240, 10240))
        save_img.save(save_path)
        print("write:" + save_path)
        save_img.close()
        slide.close()
    else:
        print("exist-\n")
    # print("\tcompress complete:" + str(time.asctime(time.localtime(time.time()))))
    # end = log.log_time("\n\tCompress complete:")


# 压缩病理切片（w，h参数分别表示长宽的压缩比）
def compress(ori_path, des_path, w, h):
    start_time = time.time()
    # print("\tcompress:" + str(time.asctime(time.localtime(time.time()))))
    log.log_line()
    start = log.log_time("\tCompress:")
    file_name = fop.get_just_filename(ori_path)
    list_name = fop.get_files_ab_path(ori_path)
    fop.generate_path(des_path)
    file_nums = len(file_name)
    log.log_data("Total numbers:" + str(len(file_name)), 0)
    for i in range(file_nums):
        image_path = list_name[i]
        slide = openslide.open_slide(image_path)
        [W, H] = slide.level_dimensions[0]
        # print(file_name[i] + '----', W, H)
        save_img = slide.get_thumbnail((W / w, H / h))
        save_path = des_path + "/" + file_name[i].rstrip() + '.png'
        save_img.save(save_path)
        save_img.close()
        slide.close()
        if (i + 1) % 15 == 0 or i == 0:
            log.log_data("Finished " + str(i) + " :" + file_name[i], -1)
        else:
            log.log_data(str(i) + ":" + file_name[i], 1)
    # print("\tcompress complete:" + str(time.asctime(time.localtime(time.time()))))
    end = log.log_time("\n\tCompress complete:")
    log.log_speed(start, end, len(file_name))
    log.log_line()


# 裁剪病理切片，size为需要裁剪的小正方形边长
def crop(ori_path, des_path, size):
    # print("\tcrop:" + str(time.asctime(time.localtime(time.time()))))
    log.log_line()
    start = log.log_time("\tcrop:")
    # file_path为新文件目录表
    files = fop.get_files_ab_path(ori_path)
    file_path = fop.generate_paths(ori_path, des_path)
    file_name = fop.get_just_filename(ori_path)
    log.log_data("Total numbers:" + str(len(file_name)), 0)
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
                column = 1
            result[j].save(
                file_path[i].rstrip() + "/" + file_name[i].rstrip() + "~" + str(row) + "_" + str(column) + ".png")
            column += 1
        if (i + 1) % 15 == 0 or i == 0:
            log.log_data("Finished " + str(i) + " :" + file_name[i], -1)
        else:
            log.log_data(str(i) + ":" + file_name[i], 1)
    # print("\tcrop complete:" + str(time.asctime(time.localtime(time.time()))))
    end = log.log_time("\n\tcrop complete:")
    log.log_speed(start, end, len(file_name))
    log.log_line()


# 拼接病理切片
def stitch(ori_path, des_path):
    # print("\tstitch:" + str(time.asctime(time.localtime(time.time()))))
    log.log_line()
    start = log.log_time("\tstitch:")
    file_path = fop.get_files_ab_path(ori_path)
    fop.generate_path(des_path)
    log.log_data("Total numbers:" + str(len(file_path)), 0)
    for i in range(len(file_path)):
        # print(file_path)
        file_name = fop.get_just_filename(file_path[i])
        image = Image.new("RGB", (10240, 10240))
        for j in range(len(file_name)):
            row = int(file_name[j].split("&", 1)[1].split("_", 1)[0])
            column = int(file_name[j].split("&", 1)[1].split("_", 1)[1])
            img = Image.open(file_path[i] + "/" + file_name[j] + ".png")
            box = ((row - 1) * 1024, (column - 1) * 1024, row * 1024, column * 1024)
            image.paste(img, box)
        image.save(des_path + "/" + file_name[i].split("&", 1)[0] + ".png")
        if (i + 1) % 15 == 0 or i == 0:
            log.log_data("Finished " + str(i) + " :" + file_name[i], -1)
        else:
            log.log_data(str(i) + ":" + file_name[i], 1)
    # print("\tstitch complete:" + str(time.asctime(time.localtime(time.time()))))
    end = log.log_time("\n\tstitch complete:")
    log.log_speed(start, end, len(file_name))
    log.log_line()


# 图片尺寸归一化，size表示目标尺寸的正方形边长
def normalize_size(ori_path, des_path, size):
    # print("\tnormalize_size:" + str(time.asctime(time.localtime(time.time()))))
    log.log_line()
    start = log.log_time("\tnormalize_size:")
    files = fop.get_files_ab_path(ori_path)
    file_name = fop.get_just_filename(ori_path)
    fop.generate_path(des_path)
    log.log_data("Total numbers:" + str(len(file_name)), 0)
    for i in range(len(files)):
        image = Image.open(files[i])
        resized_img = image.resize((size, size))
        resized_img.save(des_path + "/" + file_name[i].rstrip() + '.png')
        if (i + 1) % 15 == 0 or i == 0:
            log.log_data("Finished " + str(i) + " :" + file_name[i], -1)
        else:
            log.log_data(str(i) + ":" + file_name[i], 1)
    # print("\tnormalize_size complete:" + str(time.asctime(time.localtime(time.time()))))
    end = log.log_time("\n\tnormalize_size complete:")
    log.log_speed(start, end, len(file_name))
    log.log_line()


# 病理图片颜色归一化（待定）
def normalize_color(ori_path, des_path, standard_path):
    print("\tcolor_normalization:" + str(time.asctime(time.localtime(time.time()))))
    log.log_line()
    start = log.log_time("\tnormalize_color:")
    standard = np.array(Image.open(standard_path))
    fop.generate_path(des_path)
    file_path = fop.get_files_ab_path(ori_path)
    file_name = fop.get_just_filename(ori_path)
    log.log_data("Total numbers:" + str(len(file_name)), 0)
    for i in range(len(file_path)):
        img = np.array(Image.open(file_path[i]))
        img = Image.fromarray(color_transfer(standard, img))
        img.save(des_path + "/" + file_name[i].rstrip() + ".png")
        if (i + 1) % 15 == 0 or i == 0:
            log.log_data("Finished " + str(i) + " :" + file_name[i], -1)
        else:
            log.log_data(str(i) + ":" + file_name[i], 1)
    print("\tcolor_normalization complete:" + str(time.asctime(time.localtime(time.time()))))
    end = log.log_time("\n\tnormalize_color complete:")
    log.log_speed(start, end, len(file_name))
    log.log_line()


def create_txts():
    path = "E:\code_python\datasets\coco\images"
    name = fop.get_files_ab_path(path)
    train_box = []
    test_box = []
    val_box = []
    for i in range(len(name)):
        while True:
            rand = random.random()
            if len(train_box) <= 244 and rand > 0.5:
                train_box.append(name[i])
                break
            elif len(test_box) <= 80 and rand < 0.2:
                test_box.append(name[i])
                break
            elif len(val_box) <= 80:
                val_box.append(name[i])
                break
    with open("E:\code_python\datasets\coco/train.txt", "w") as file:
        for i in range(len(train_box)):
            file.write(train_box[i] + "\n")
        file.close()
    with open("E:\code_python\datasets\coco/test.txt", "w") as file:
        for i in range(len(test_box)):
            file.write(test_box[i] + "\n")
        file.close()
    with open("E:\code_python\datasets\coco/val.txt", "w") as file:
        for i in range(len(val_box)):
            file.write(val_box[i] + "\n")
        file.close()


if __name__ == '__main__':
    # create_txts()
    # normalize_size("E:\_mvidata\T&N\TN\compress_约512", "E:\_mvidata\T&N\TN/512", 512)
    # compress("E:\_mvidata\T&N\TN/10240", "E:\_mvidata\T&N\TN/512", 20, 20)
    # ori = input("请输入数据所在文件夹目录：")
    # des = "E:\_mvidata/N\一致率/10240"
    # get_txt_file(ori, des)
    # crop("E:\_mvidata/full_test/10240", "E:\_mvidata/full_test/1024", 1024)
    stitch("E:\_mvidata/full_test\detection", "E:\_mvidata/full_test/result")
