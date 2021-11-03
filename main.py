import time

import basic_op.log_operation as log
import data_op.img_processing as data_pre


def compress():
    data_pre.compress(ori_path="D:\_DATA\T&N",
                      des_path="D:\_DATA/ndpi_com", w=10, h=10)


def normalize_size():
    data_pre.normalize_size(ori_path="D:\_DATA/ndpi_com",
                            des_path="D:\_DATA/ndpi_nor", size=10240)


def crop():
    data_pre.crop(ori_path="D:\_DATA/ndpi_nor",
                  des_path="D:\_DATA/ndpi_cut", size=1024)


def stitch():
    data_pre.stitch(ori_path="E:/ndpi_cut",
                    des_path="E:/ndpi_stitch")


def normalize_color():
    data_pre.normalize_color(ori_path="E:/ndpi_stitch", des_path="E:/ndpi_color")


if __name__ == '__main__':
    start = time.time()
    log.log_init()
    compress()
    normalize_size()
    crop()
    end = time.time()
    log.log_line()
    log.log_speed(start, end, 180)
    log.log_line()
    log.log_show()
    # stitch()
    # normalize_color()
