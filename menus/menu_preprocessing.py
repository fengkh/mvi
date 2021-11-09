import time

import basic_op.log as log
import data_op.preprocessing as dop


def compress():
    dop.compress(ori_path="D:\_DATA\T&N/ndpi_nor",
                               des_path="D:\_DATA\T&N/ndpi_seg", w=20, h=20)


def normalize_size():
    dop.normalize_size(ori_path="D:\_DATA/ndpi_com",
                                     des_path="D:\_DATA/ndpi_nor", size=10240)


def crop():
    dop.crop(ori_path="D:\_DATA/ndpi_nor",
                           des_path="D:\_DATA/ndpi_cut", size=1024)


def stitch():
    dop.stitch(ori_path="E:/ndpi_cut",
                             des_path="E:/ndpi_stitch")


def normalize_color():
    dop.normalize_color(ori_path="E:/ndpi_stitch", des_path="E:/ndpi_color")


if __name__ == '__main__':
    file_nums = 30
    start = time.time()
    log.log_init()
    compress()
    normalize_size()
    crop()
    stitch()
    end = time.time()
    log.log_line()
    log.log_speed(start, end, file_nums)
    log.log_line()
    log.log_show()
    normalize_color()
