import data_op.seg_json as dop


def magnify():
    dop.magnify(ori_path="D:\_DATA\分割分辨率测试\TN-Label-test", des_path="D:\_DATA\分割分辨率测试\des", ratio=20)


def json_content():
    dop.json_content(ori_path="D:\_DATA\分割分辨率测试\des", des_path="D:\_DATA\分割分辨率测试\des")


if __name__ == '__main__':
    # magnify()
    json_content()