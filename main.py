import data_op.pretreatment as data_pre


def compress():
    data_pre.compress(ori_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\dataset\compress_test",
                      des_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\dataset\generate_test", w=20, h=20)


def cut():
    data_pre.cut(ori_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\dataset\compress_test",
                 des_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\dataset\generate_test", size=100)


def normalize_size():
    data_pre.normalize_size(ori_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\dataset\compress_test",
                            des_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\dataset\generate_test", size=1024)


if __name__ == '__main__':
    # compress()
    # cut()
    normalize_size()