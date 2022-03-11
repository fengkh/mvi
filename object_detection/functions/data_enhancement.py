from torchvision import transforms
import system_operation.log as log
from PIL import Image
import system_operation.file as file

img_path = 'E:\code_python\mvi\data\image'
label_path = 'E:\code_python\mvi\data\label'
W = 1000
H = 1000


# 数据增强方法1：水平翻转img的同时生成对应的.txt标签文件
def flip():
    log.log_start(flip.__name__)
    images = file.get_files_ab_path(img_path)
    txts = file.get_files_ab_path(label_path)
    num = len(images)
    counter = num
    # 图片翻转，并重新命名
    f = transforms.RandomHorizontalFlip(p=1.0)
    for i in range(num):
        img = Image.open(images[i])
        img = f(img)
        img.save(img_path + "/" + str(counter).zfill(6) + ".jpg")
        # 生成对应的.txt标签
        new_line = []
        with open(txts[i], "r") as txt:
            lines = txt.readlines()
            for j in range(len(lines)):
                blocks = lines[j].split(" ")
                blocks[1] = str('%.6f' % (1 - float(blocks[1])))
                new_line.append(blocks)
            print(new_line)
            txt.close()
        with open(label_path + "/" + str(counter).zfill(6) + ".txt", "a") as txt:
            for j in range(len(new_line)):
                txt.write(new_line[j][0]+" "+new_line[j][1]+" "+new_line[j][2]+" "+new_line[j][3]+" "+new_line[j][4])
            txt.close()
        counter += 1
    log.log_end(flip.__name__)


if __name__ == '__main__':
    flip()
