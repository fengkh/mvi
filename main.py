import data_op.img_processing as data_pre


def compress():
    data_pre.compress(ori_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\code_test/ndpi",
                      des_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\code_test/ndpi_com", w=10, h=10)


def normalize_size():
    data_pre.normalize_size(ori_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\code_test/ndpi_com",
                            des_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\code_test/ndpi_nor", size=10240)


def cut():
    data_pre.crop(ori_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\code_test/ndpi_nor",
                  des_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\code_test/ndpi_cut", size=1024)


def stitch():
    return data_pre.stitch(ori_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\code_test/ndpi_cut",
                           des_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\code_test/ndpi_stitch")


if __name__ == '__main__':
    compress()
    normalize_size()
    cut()
    stitch()
