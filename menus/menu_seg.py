import data_op.seg_json as dop


def magnify():
    dop.magnify(ori_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\dataset\癌灶分割标注\T&N",
                des_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\dataset\癌灶分割标注/10240", ratio=20)


def json_content():
    dop.json_content(ori_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\dataset\癌灶分割标注/10240",
                     des_path="E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\dataset\癌灶分割标注/10240")


def json_convert():
    dop.json_convert(ori_path="'E:\IoT\项目\肝脏肿瘤入侵识别项目\stage2\dataset\癌灶分割标注\T&N'")


if __name__ == '__main__':
    # magnify()
    # json_content()
    json_convert()
