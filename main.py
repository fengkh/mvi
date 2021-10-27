import data_op.pretreatment as data_pre


def compress():
    data_pre.compress(ori_path="",
                      des_path="", w=20, h=20)


def cut():
    data_pre.crop(ori_path="C:/Users/fengk\Desktop\新建文件夹",
                  des_path="C:/Users/fengk\Desktop\新建文件夹 (2)", size=1024)


def normalize_size():
    data_pre.normalize_size(ori_path="",
                            des_path="", size=1024)


if __name__ == '__main__':
    # compress()
    cut()
    # normalize_size()
