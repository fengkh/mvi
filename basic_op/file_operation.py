import os


# 将文件夹内所有文件路径存到list_name数组
def get_absolute_path(path):
    list_name = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            get_absolute_path(file_path, list_name)
        else:
            list_name.append(file_path)
    return list_name


# 创建文件夹
def generate_path(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)


# 返回不带后缀的文件名列表
def get_filename(path):
    file_list = os.listdir(path)
    file_name_list = []
    for i in range(len(file_list)):
        file_name = path + '/' + file_list[i]
        # print(file_name)
        file_name_list.append(file_name)
    path = file_name_list
    filesname_list = []
    for i in range(len(path)):
        (filepath, tempfilename) = os.path.split(path[i])
        (filesname, extension) = os.path.splitext(tempfilename)
        filesname_list.append(filesname)
    return filesname_list


# 构造对应的生成子空文件夹
def generate_paths(ori_path, des_path):
    list_name = get_absolute_path(ori_path)
    generate_path(des_path)
    file_name = get_filename(ori_path)
    path = []
    for i in range(len(list_name)):
        path[i] = des_path + "/" + file_name[i]
        generate_path(path[i])
    return path
