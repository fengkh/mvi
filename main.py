import data_op.img_processing as data_pre


def compress():
    return data_pre.compress(ori_path="E:/ndpi",
                             des_path="E:/ndpi_com", w=10, h=10)


def normalize_size():
    data_pre.normalize_size(ori_path="E:/ndpi_com",
                            des_path="E:/ndpi_nor", size=10240)


def crop():
    data_pre.crop(ori_path="E:/ndpi_nor",
                  des_path="E:/ndpi_cut", size=1024)


def stitch():
    return data_pre.stitch(ori_path="E:/ndpi_cut",
                           des_path="E:/ndpi_stitch")


if __name__ == '__main__':
    start_time, file_nums = compress()
    normalize_size()
    crop()
    end_time = stitch()
    print("Time = " + str(int((end_time - start_time) / 60)) + " min, Speed = " + str(
        int((end_time - start_time) / file_nums)) + " s/img")
