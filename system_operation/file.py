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
    my_path = input("请复制完整的文件夹路径:")
    # print(my_path)
    my_list = get_just_filename(my_path)
    print(my_list)
    with open(my_path + '/file_path.txt', 'w') as f:
        for i in range(len(my_list)):
            f.write(my_list[i] + "\n")
        f.close()
    input('生成成功，按任意键关闭')


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
    # print(list1)
    # input()
    with open(txt2, "r") as f2:
        line = f2.readline()
        while line:
            list2.append(line)
            line = f2.readline()
        f2.close()
    # print(list2)
    # input()
    # list1 表示所有的内容，list2表示成功写入的内容
    for element in list2:
        if element in list1:
            list1.remove(element)
    # print(list1)
    # input()
    with open(txt2, "w") as f:
        for i in range(len(list1)):
            f.write(list1[i])
        f.close()


def delete_():
    path = "E:\_mvidata/N\一致率/file_path.txt"
    write_path = "E:\_mvidata/N\一致率/file_path_delete_.txt"
    with open(path, "r") as f:
        with open(write_path, "a+") as w:
            content = f.readlines()
            for i in range(len(content)):
                file_name = content[i].split("_")[0] + "\n"
                w.write(file_name)
            w.close()
        f.close()


def get_json_files(father_path, des_path):
    jsons = []
    for file in os.listdir(father_path):
        path = father_path + "/" + file
        if os.path.isdir(path):
            for file_name in get_files_ab_path(path):
                if file_name.split(".")[-1] == 'json':
                    jsons.append(file_name)
                    shutil.copy(file_name, des_path + "/" + file_name.split("\\")[-1])
                    shutil.copy(file_name.split("json")[0]+"png",des_path + "/" + file_name.split("\\")[-1].split(".")[0]+".png")
    print(len(jsons))

if __name__=='__main__':
    # get_json_files("E:\_mvidata/N/N标注数据", "E:\_mvidata/N\json数据集")
    # delete_()
    # generate_selection_txt()
    delete_overlap("F:/1  3D 1513/file_path.txt", "E:\_mvidata/N\一致率/10240/file_path.txt")
    # get_just_filename("E:\_test\Z1960411-8\\Z1960411-8&10_1.png")
