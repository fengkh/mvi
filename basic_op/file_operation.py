import os


# 将文件夹内所有文件路径存到list_name数组
def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            list_name.append(file_path)


# 创建文件夹
def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)


# 返回不带后缀的文件名列表
def no_tail(path):
    # 获取文件路径列表
    file_path = dir_name(path)
    # 获取初始无后缀文件名
    return files_name(file_path)


# 获取文件名
def files_name(path):
    filesname_list = []
    for i in range(len(path)):
        (filepath, tempfilename) = os.path.split(path[i])
        (filesname, extension) = os.path.splitext(tempfilename)
        filesname_list.append(filesname)
    return filesname_list


# 遍历文件夹，获取当前文件夹下文件所有路径的列表
def dir_name(path):
    file_list = os.listdir(path)
    file_name_list = []
    for i in range(len(file_list)):
        file_name = path + '/' + file_list[i]
        # print(file_name)
        file_name_list.append(file_name)
    return file_name_list
