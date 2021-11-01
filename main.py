import time

import basic_op.log_operation as log
import data_op.img_processing as data_pre


def compress():
    data_pre.compress(ori_path="D:\_DATA\T&N",
                      des_path="D:\_DATA/ndpi_com", w=10, h=10)


def normalize_size():
    data_pre.normalize_size(ori_path="E:/ndpi_com",
                            des_path="E:/ndpi_nor", size=10240)


def crop():
    data_pre.crop(ori_path="E:/ndpi_nor",
                  des_path="E:/ndpi_cut", size=1024)


def stitch():
    data_pre.stitch(ori_path="E:/ndpi_cut",
                    des_path="E:/ndpi_stitch")


def normalize_color():
    data_pre.normalize_color(ori_path="E:/ndpi_stitch", des_path="E:/ndpi_color")


if __name__ == '__main__':
    # log.log_init()
    file_nums = 180
    start_time = time.time()
    compress()
    # normalize_size()
    # crop()
    # stitch()
    # normalize_color()
    end_time = time.time()
    print("Time = " + str(int((end_time - start_time) / 60)) + " min, Speed = " + str(
        int((end_time - start_time) / file_nums)) + " s/img")
