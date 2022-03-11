import os
import shutil


# 将文件夹内所有文件路径存到list_name数组
def get_files_ab_path(path):
    list_name = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        list_name.append(file_path)
    return list_name


def del_space(list1):
    for i in range(len(list1)):
        list1[i].rstrip()
    return list1


def get_dir_file(path):
    lists = []
    for dirs in os.listdir(path):
        lists.append(path + "/" + dirs)
    return lists


# 创建文件夹
def generate_path(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)


# 返回不带后缀的文件名列表
def get_just_filename(path):
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
    list_name = get_files_ab_path(ori_path)
    generate_path(des_path)
    file_name = get_just_filename(ori_path)
    path = []
    for i in range(len(list_name)):
        path.append(des_path + "/" + file_name[i])
        generate_path(path[i])
    return path


# 根据文件名生成txt文件
def generate_selection_txt():
    my_path = input("文件夹完整目录：\n")
    print(my_path)
    my_list = get_just_filename(my_path)
    print(my_list)
    with open(my_path + '/file_path.txt', 'w') as f:
        for i in range(len(my_list)):
            f.write(my_list[i] + "\n")
    f.close()


# 根据txt文件筛选出目标文件,记得把txt文件放到同一个目录下
def get_txt_file(txt_path, ori_path):
    my_list = []
    with open(txt_path + "/file_path.txt", "r") as f:
        line = f.readline()
        while line:
            my_list.append(txt_path + "/" + line.strip("\n") + ".ndpi")
            line = f.readline()
    f.close()
    # print(my_list)
    for i in range(len(my_list)):
        if os.path.exists(my_list[i]):
            shutil.copy(my_list[i], ori_path)
        else:
            print(my_list[i])


# txt1为原本的路径，txt2为已经成功写入的路径
def delete_overlap(txt1, txt2):
    list1 = []
    list2 = []
    with open(txt1, "r") as f1:
        line = f1.readline()
        while line:
            list1.append(line)
            line = f1.readline()
    f1.close()
    with open(txt2, "r") as f2:
        line = f2.readline()
        while line:
            list2.append(line)
            line = f2.readline()
    f2.close()
    for element in list2:
        if (element in list1):
            list1.remove(element)
    with open(txt2, "w") as f:
        for i in range(len(list1)):
            f.write(list1[i])
    f.close()


# get_txt_file("F:/2  binsong  3573", "E:\_DATA\data/N")
# generate_selection_txt()
# delete_overlap("F:/2  binsong  3573/file_path.txt","E:\_DATA\data/N/file_path.txt")